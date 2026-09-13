#!/usr/bin/env python3
"""
split_chunks.py —— 为全量中文概述生成做准备：分块打包

1. 扫描 prompts/**/*.md 中尚未包含“中文概述：”的 prompt 文件
2. 按分类分组，每批 <= MAX_FILES 个文件
3. 为每批生成紧凑摘录包 tools/chunks/chunk_XXX.txt（子代理只读这一个文件即可撰写）
4. 输出 tools/chunks/manifest.json（每批的文件清单）

用法：python3 tools/split_chunks.py
"""
import json
import re
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PROMPTS_DIR = REPO_ROOT / "prompts"
CHUNKS_DIR = REPO_ROOT / "tools" / "chunks"
OVERVIEWS_DIR = REPO_ROOT / "tools" / "overviews"
MAX_FILES = int(__import__("os").environ.get("CHUNK_SIZE", "40"))
SKIP_NAMES = {"INDEX.md", "README.md"}


def covered_files() -> set[str]:
    """已产出概述的文件：任一 overviews/*.json 中的 file，或文件内已含 中文概述："""
    covered = set()
    if OVERVIEWS_DIR.exists():
        for jf in OVERVIEWS_DIR.glob("*.json"):
            try:
                for it in json.loads(jf.read_text(encoding="utf-8")):
                    covered.add(str(it.get("file")))
            except Exception:
                pass
    return covered


def has_overview(p: Path) -> bool:
    return "中文概述：" in p.read_text(encoding="utf-8", errors="replace")


def build_excerpt(p: Path) -> str:
    txt = p.read_text(encoding="utf-8", errors="replace")
    lines = txt.splitlines()
    title = ""
    for ln in lines:
        if ln.startswith("# "):
            title = ln[2:].strip()
            break
    # 说明块（第一个 ## 之后、下一个 ## 之前）
    desc = ""
    m = re.search(r"## ([^\n]+)\n(.*?)(?=\n## |\Z)", txt, re.S)
    if m and m.group(1).strip() in ("说明",):
        desc = re.sub(r"\s+", " ", m.group(2)).strip()[:500]
    # 正文（## Prompt 内容 之后）
    body = ""
    m = re.search(r"## Prompt 内容\s*\n(.*)", txt, re.S)
    if m:
        body = re.sub(r"```[a-z]*", " ", m.group(1))
        body = re.sub(r"\s+", " ", body).strip()[:900]
    excerpt = f"标题: {title}\n说明: {desc}\n正文(节选): {body}"
    return excerpt


def main():
    covered = covered_files()
    files = sorted(
        p for p in PROMPTS_DIR.rglob("*.md")
        if p.name not in SKIP_NAMES and p.is_file()
        and str(p.relative_to(REPO_ROOT)) not in covered
        and not has_overview(p)
    )
    print(f"待处理文件: {len(files)}（已覆盖 {len(covered)} 个）")

    by_cat = defaultdict(list)
    for p in files:
        by_cat[p.parent.name].append(p)

    CHUNKS_DIR.mkdir(parents=True, exist_ok=True)
    # 清理旧分块
    for old in CHUNKS_DIR.glob("chunk_*.txt"):
        old.unlink()

    chunks = []
    idx = 0
    for cat in sorted(by_cat, key=lambda c: -len(by_cat[c])):
        cat_files = by_cat[cat]
        for i in range(0, len(cat_files), MAX_FILES):
            batch = cat_files[i:i + MAX_FILES]
            record = {
                "chunk": idx,
                "category": cat,
                "files": [str(p.relative_to(REPO_ROOT)) for p in batch],
            }
            chunks.append(record)
            bundle = "\n\n".join(
                f"@文件: {str(p.relative_to(REPO_ROOT))}\n{build_excerpt(p)}"
                for p in batch
            )
            (CHUNKS_DIR / f"chunk_{idx:03d}.txt").write_text(bundle, encoding="utf-8")
            idx += 1

    (CHUNKS_DIR / "manifest.json").write_text(
        json.dumps(chunks, ensure_ascii=False, indent=1), encoding="utf-8"
    )
    print(f"生成 {len(chunks)} 个分块:")
    for c in chunks:
        print(f"  chunk_{c['chunk']:03d}  {c['category']}  {len(c['files'])} 文件")


if __name__ == "__main__":
    main()
