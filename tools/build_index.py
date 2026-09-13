#!/usr/bin/env python3
"""
build_index.py —— 为 prompts/ 库构建向量索引

流程：
  1. 扫描 prompts/**/*.md（跳过 INDEX.md）
  2. 从 STARTER.md / HOW-TO.md 解析已有的中文标题与点评（若有）
  3. 组装索引文档（分类 + 标题 + 中文标注 + 正文摘要）
  4. 调用 OpenAI text-embedding-3-small 向量化（增量：只处理新增/变更文件）
  5. 保存到 tools/index_data/（vectors.npy + meta.jsonl）

用法：
  export OPENAI_API_KEY=sk-xxx
  python3 tools/build_index.py            # 增量更新
  python3 tools/build_index.py --rebuild  # 全量重建
  python3 tools/build_index.py --dry-run  # 只统计，不调 API
"""
import argparse
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parent.parent
PROMPTS_DIR = REPO_ROOT / "prompts"
DATA_DIR = Path(__file__).resolve().parent / "index_data"
VECTORS_FILE = DATA_DIR / "vectors.npy"
META_FILE = DATA_DIR / "meta.jsonl"

API_URL = "https://api.openai.com/v1/embeddings"
MODEL = os.environ.get("OPENAI_EMBED_MODEL", "text-embedding-3-small")
BATCH_SIZE = 64
CONTENT_EXCERPT = 800  # 正文摘要字符数
KEY_FILE = Path(__file__).resolve().parent / ".openai_key"
BASE_FILE = Path(__file__).resolve().parent / ".openai_base"


def api_endpoint() -> str:
    """embedding 端点：默认 OpenAI；可用环境变量 OPENAI_BASE_URL 或 tools/.openai_base 指定兼容网关"""
    base = os.environ.get("OPENAI_BASE_URL", "").strip()
    if not base and BASE_FILE.exists():
        base = BASE_FILE.read_text(encoding="utf-8").strip()
    if base:
        return base.rstrip("/") + "/embeddings"
    return API_URL


def resolve_api_key() -> str:
    """API key 来源：环境变量 OPENAI_API_KEY > tools/.openai_key（不入库）"""
    key = os.environ.get("OPENAI_API_KEY", "").strip()
    if key:
        return key
    if KEY_FILE.exists():
        return KEY_FILE.read_text(encoding="utf-8").strip()
    return ""

# ---------------------------------------------------------------- 中文标注解析

LINK_RE = re.compile(
    r"- 【(?P<kind>[^】]*)】\[(?P<zh_title>[^\]]*)\]\((?P<link>[^)]+)\)"
    r"(?:\s*｜\s*(?P<orig_title>[^｜\n]*))?(?:\s*｜\s*(?P<desc>[^｜\n]*))?"
)


def parse_annotation_files() -> dict:
    """解析 STARTER.md 与 HOW-TO.md，返回 {相对路径: {zh_title, desc}}"""
    annotations = {}
    for name in ("STARTER.md", "HOW-TO.md"):
        f = REPO_ROOT / name
        if not f.exists():
            continue
        for line in f.read_text(encoding="utf-8").splitlines():
            m = LINK_RE.match(line.strip())
            if not m:
                continue
            rel = urllib.parse.unquote(m.group("link"))
            info = annotations.setdefault(rel, {})
            if m.group("zh_title"):
                info.setdefault("zh_title", m.group("zh_title").strip())
            desc = (m.group("desc") or "").strip()
            # STARTER 的点评比 HOW-TO 的短标签信息量大，优先保留更长的
            if desc and len(desc) > len(info.get("desc", "")):
                info["desc"] = desc
    return annotations


# ---------------------------------------------------------------- 文档组装

def slug_to_title(filename: str) -> str:
    stem = Path(filename).stem
    stem = re.sub(r"[-_]+", " ", stem)
    return stem.strip().capitalize()


def load_library_map() -> dict:
    """读取 tools/library.jsonl（若存在）→ {path: rec}，用于生成更语义化的索引文本"""
    lib = REPO_ROOT / "tools" / "library.jsonl"
    out = {}
    if lib.exists():
        for ln in lib.read_text(encoding="utf-8").splitlines():
            if ln.strip():
                rec = json.loads(ln)
                out[rec["path"]] = rec
    return out


def build_index_doc(category: str, path: Path, ann: dict, lib: dict | None = None) -> tuple[str, str]:
    """返回 (index_text, content_excerpt)

    优先用 library.jsonl 的语义化字段（概述/关键词/标题/摘要）拼索引文本，
    比纯英文原文更利于中英混合语义检索；无 library 时回退到旧逻辑。
    """
    rel = str(path.relative_to(REPO_ROOT))
    if lib and rel in lib:
        rec = lib[rel]
        parts = [f"分类: {category}"]
        if rec.get("summary"):
            parts.append(f"中文概述: {rec['summary']}")
        if rec.get("zh_title"):
            parts.append(f"中文标题: {rec['zh_title']}")
        if rec.get("tags"):
            parts.append(f"关键词: {'、'.join(rec['tags'])}")
        parts.append(f"标题: {rec.get('title') or slug_to_title(path.name)}")
        if rec.get("desc"):
            parts.append(f"简介: {rec['desc']}")
        if rec.get("excerpt"):
            parts.append(f"正文: {rec['excerpt']}")
        excerpt = " ".join(x for x in (rec.get("summary"), rec.get("excerpt")) if x)
        return "\n".join(parts), excerpt[:CONTENT_EXCERPT]

    content = path.read_text(encoding="utf-8", errors="replace")
    # 去掉 markdown 标记噪声，保留文字
    text = re.sub(r"[#*`>\[\]()|_-]+", " ", content)
    text = re.sub(r"\s+", " ", text).strip()
    excerpt = text[:CONTENT_EXCERPT]

    parts = [f"分类: {category}"]
    if ann.get("zh_title"):
        parts.append(f"中文标题: {ann['zh_title']}")
    parts.append(f"标题: {slug_to_title(path.name)}")
    if ann.get("desc"):
        parts.append(f"简介: {ann['desc']}")
    parts.append(f"正文: {excerpt}")
    return "\n".join(parts), excerpt


# ---------------------------------------------------------------- OpenAI API

def embed_texts(texts: list[str], api_key: str) -> list[list[float]]:
    """分批调用 embedding API，返回向量列表（带重试）"""
    all_vecs = []
    for i in range(0, len(texts), BATCH_SIZE):
        batch = texts[i : i + BATCH_SIZE]
        payload = json.dumps({"model": MODEL, "input": batch}).encode("utf-8")
        for attempt in range(5):
            try:
                req = urllib.request.Request(
                    api_endpoint(),
                    data=payload,
                    headers={
                        "Authorization": f"Bearer {api_key}",
                        "Content-Type": "application/json",
                    },
                    method="POST",
                )
                with urllib.request.urlopen(req, timeout=120) as resp:
                    data = json.loads(resp.read().decode("utf-8"))
                break
            except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError) as e:
                wait = 2 ** attempt
                print(f"  API 请求失败（{e}），{wait}s 后重试 ({attempt + 1}/5)", file=sys.stderr)
                time.sleep(wait)
        else:
            raise RuntimeError("API 连续 5 次调用失败，中止")
        # 按 index 还原顺序
        batch_vecs = [None] * len(batch)
        for item in data["data"]:
            batch_vecs[item["index"]] = item["embedding"]
        all_vecs.extend(batch_vecs)
        print(f"  已向量化 {min(i + BATCH_SIZE, len(texts))}/{len(texts)}")
    return all_vecs


# ---------------------------------------------------------------- 主流程

def content_hash(path: Path) -> str:
    return hashlib.md5(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description="构建 prompt 库向量索引")
    parser.add_argument("--rebuild", action="store_true", help="忽略已有索引，全量重建")
    parser.add_argument("--dry-run", action="store_true", help="只统计待处理文件，不调用 API")
    args = parser.parse_args()

    api_key = resolve_api_key()
    if not api_key and not args.dry_run:
        print("错误：未找到 API key。请 export OPENAI_API_KEY=sk-xxx 或写入 tools/.openai_key", file=sys.stderr)
        sys.exit(1)

    annotations = parse_annotation_files()
    print(f"从 STARTER.md / HOW-TO.md 解析到 {len(annotations)} 条中文标注")
    lib = load_library_map()
    print(f"加载 library.jsonl 语义字段 {len(lib)} 条")

    files = sorted(
        p for p in PROMPTS_DIR.rglob("*.md")
        if p.name not in ("INDEX.md", "README.md") and p.is_file()
    )
    print(f"扫描到 {len(files)} 个 prompt 文件")

    # 加载已有索引（增量模式）
    old_metas, old_vecs = [], None
    if not args.rebuild and META_FILE.exists() and VECTORS_FILE.exists():
        with open(META_FILE, encoding="utf-8") as f:
            old_metas = [json.loads(line) for line in f if line.strip()]
        old_vecs = np.load(VECTORS_FILE)
        if len(old_metas) != len(old_vecs):
            print("警告：已有索引数据不一致，执行全量重建", file=sys.stderr)
            old_metas, old_vecs = [], None

    old_index = {m["path"]: i for i, m in enumerate(old_metas)}
    keep_metas, keep_vecs, to_process = [], [], []
    for p in files:
        rel = str(p.relative_to(REPO_ROOT))
        h = content_hash(p)
        idx = old_index.get(rel)
        if idx is not None and old_vecs is not None and old_metas[idx]["hash"] == h:
            keep_metas.append(old_metas[idx])
            keep_vecs.append(old_vecs[idx])
        else:
            to_process.append((rel, p, h))

    print(f"复用已有向量 {len(keep_metas)} 条，待向量化 {len(to_process)} 条")
    if args.dry_run:
        return

    new_metas, new_vecs = [], []
    if to_process:
        docs = []
        for rel, p, h in to_process:
            ann = annotations.get(rel, {})
            rec = (lib or {}).get(rel, {})
            index_text, excerpt = build_index_doc(p.parent.name, p, ann, lib)
            docs.append(index_text)
            new_metas.append({
                "path": rel,
                "category": p.parent.name,
                "zh_title": rec.get("zh_title") or ann.get("zh_title", ""),
                "title": rec.get("title") or slug_to_title(p.name),
                "summary": rec.get("summary", ""),
                "tags": rec.get("tags", []),
                "desc": rec.get("desc") or ann.get("desc", ""),
                "excerpt": excerpt,
                "hash": h,
            })
        print("开始调用 embedding API ...")
        vecs = embed_texts(docs, api_key)
        new_vecs = [np.asarray(v, dtype=np.float32) for v in vecs]

    all_metas = keep_metas + new_metas
    all_vec_list = keep_vecs + new_vecs
    mat = np.vstack([np.asarray(v, dtype=np.float32) for v in all_vec_list])
    # L2 归一化，检索时直接点积即余弦相似度
    norms = np.linalg.norm(mat, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    mat = (mat / norms).astype(np.float32)

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    np.save(VECTORS_FILE, mat)
    with open(META_FILE, "w", encoding="utf-8") as f:
        for m in all_metas:
            f.write(json.dumps(m, ensure_ascii=False) + "\n")
    print(f"完成：共索引 {len(all_metas)} 条，向量矩阵 {mat.shape}，保存至 {DATA_DIR}")


if __name__ == "__main__":
    main()
