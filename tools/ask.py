#!/usr/bin/env python3
"""
ask.py —— prompt 库检索（关键词 + 可选向量语义，双路 RRF 融合）

数据源：tools/library.jsonl（由 make_library.py 生成）
模式：
  keyword   纯关键词（离线，零依赖）
  semantic  纯向量语义（需 tools/index_data/ 向量索引 + API key）
  hybrid    默认：向量语义 top12 与关键词 top12 用 RRF 融合重排
  auto      有向量索引与 key 则 hybrid，否则 keyword

用法：
  python3 tools/ask.py "优化简历通过 ATS 筛选" -k 5
  python3 tools/ask.py "小红书 带货 文案" --json
  python3 tools/ask.py "帮我debug一段Python" -k 3 -c 1     # -c N 打印第 N 名完整 prompt
  python3 tools/ask.py "xxx" --mode semantic               # 强制纯语义
"""
import argparse
import json
import re
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_index import VECTORS_FILE, META_FILE, embed_texts, resolve_api_key  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
LIB = REPO_ROOT / "tools" / "library.jsonl"
RRF_K = 60  # RRF 平滑常数

# 字段权重：名称 -> (字段key, 权重)
FIELDS = [
    ("tags", 4.5),        # 关键词/标签 精确命中权重最高
    ("summary", 2.6),     # 中文概述
    ("zh_title", 2.2),    # 中文名（STARTER/HOW-TO 提供的）
    ("title", 1.6),       # 英文标题
    ("file", 1.6),        # 文件名
    ("category", 0.9),    # 分类
    ("desc", 0.5),        # 英文用途概述
    ("excerpt", 0.35),    # 正文摘要
]

CJK = re.compile(r"[\u4e00-\u9fff]+")
# 英文停用词（关键词检索忽略，避免 me/my/on 之类噪音污染打分）
STOPWORDS = {
    "a", "an", "the", "is", "are", "was", "were", "be", "been", "am",
    "me", "my", "your", "you", "we", "our", "their", "his", "her", "its",
    "on", "in", "at", "by", "to", "of", "for", "with", "from", "and", "or", "as",
    "like", "this", "that", "these", "those", "it", "do", "does", "did", "i",
    "can", "could", "would", "should", "will", "shall", "may", "might", "want",
    "help", "make", "make", "give", "write", "get", "need", "please", "how",
}


def tokenize_query(q: str) -> list:
    """查询 -> 词元列表：[("word","resume"), ("cjk","简历优化"), ...]（过滤英文停用词）"""
    q = q.lower()
    terms = []
    for m in re.finditer(r"[\u4e00-\u9fff]+|[a-z0-9][a-z0-9.'+#\-]*", q):
        seg = m.group(0)
        if CJK.fullmatch(seg):
            terms.append(("cjk", seg))
        elif len(seg) > 2 and seg not in STOPWORDS:
            terms.append(("word", seg))
    return terms


def cjk_bigrams(s: str):
    return {s[i:i + 2] for i in range(len(s) - 1)}


def field_hit_score(term_type: str, term: str, text: str) -> float:
    if not text:
        return 0.0
    text_l = text.lower()
    if term_type == "word":
        if term in text_l:
            if re.search(rf"(?<![a-z0-9]){re.escape(term)}(?![a-z0-9])", text_l):
                return 1.0
            return 0.55
        return 0.0
    if term in text:
        return 1.0
    qb = cjk_bigrams(term)
    if not qb:
        return 1.0 if term in text else 0.0
    hit = sum(1 for b in qb if b in text)
    return 0.6 * hit / len(qb)


# ---------------------------------------------------------------- 关键词检索

def load_library() -> tuple[list[dict], dict]:
    if not LIB.exists():
        sys.exit(f"错误：未找到 {LIB}，请先运行 python3 tools/make_library.py")
    docs = [json.loads(ln) for ln in LIB.read_text(encoding="utf-8").splitlines() if ln.strip()]
    by_path = {d["path"]: d for d in docs}
    return docs, by_path


def keyword_top(docs, query: str, k: int = 12) -> list[tuple[float, dict]]:
    terms = tokenize_query(query)
    scored = []
    for d in docs:
        total = 0.0
        for key, w in FIELDS:
            text = d.get(key) or ""
            if isinstance(text, list):
                text = " ".join(text)
            if not text:
                continue
            for ttype, term in terms:
                s = field_hit_score(ttype, term, text)
                if s:
                    total += w * s
        if total > 0:
            scored.append((total, d))
    scored.sort(key=lambda x: -x[0])
    return scored[:k]


# ---------------------------------------------------------------- 向量语义检索

def load_vector_index():
    if not VECTORS_FILE.exists() or not META_FILE.exists():
        return None
    metas = [json.loads(ln) for ln in META_FILE.read_text(encoding="utf-8").splitlines() if ln.strip()]
    vecs = np.load(VECTORS_FILE)
    if len(metas) != len(vecs):
        return None
    return metas, vecs


def semantic_top(vi, query: str, k: int = 12, api_key: str = "") -> list[tuple[float, dict]]:
    metas, vecs = vi
    qv = np.asarray(embed_texts([query], api_key)[0], dtype=np.float32)
    qv = qv / (np.linalg.norm(qv) or 1.0)
    scores = vecs @ qv
    top = np.argsort(-scores)[:k]
    return [(float(scores[i]), metas[i]) for i in top]


# ---------------------------------------------------------------- RRF 融合

RRF_K_KW = 160   # 关键词路：分母大→贡献平缓，避免少量词命中喧宾夺主
RRF_K_SEM = 40   # 语义路：分母小→贡献陡峭，语义强信号主导排序


def rrf_merge(kw: list[tuple[float, dict]], sem: list[tuple[float, dict]], k_out: int):
    """关键词与语义两路排序结果按（不同权重的）倒数排名融合"""
    acc: dict[str, float] = {}
    src: dict[str, dict] = {}
    for rank, (_, d) in enumerate(kw, start=1):
        p = d["path"]
        acc[p] = acc.get(p, 0.0) + 1.0 / (RRF_K_KW + rank)
        src.setdefault(p, d)
    for rank, (_, m) in enumerate(sem, start=1):
        p = m["path"]
        acc[p] = acc.get(p, 0.0) + 1.0 / (RRF_K_SEM + rank)
        src.setdefault(p, m)
    ordered = sorted(acc.items(), key=lambda x: -x[1])
    return [(score, src[p]) for p, score in ordered[:k_out]]


# ---------------------------------------------------------------- 主流程

def main():
    ap = argparse.ArgumentParser(description="prompt 库检索（关键词+向量语义融合）")
    ap.add_argument("query", help="用中文/英文描述你想做的事")
    ap.add_argument("-k", type=int, default=5)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("-c", type=int, metavar="N", help="打印第 N 个结果的完整 prompt")
    ap.add_argument("--mode", choices=["auto", "keyword", "semantic", "hybrid"], default="auto")
    args = ap.parse_args()

    docs, by_path = load_library()
    api_key = resolve_api_key()
    vi = load_vector_index() if args.mode in ("auto", "semantic", "hybrid") else None
    has_vec = vi is not None and bool(api_key)

    if args.mode == "semantic" and not has_vec:
        sys.exit("纯语义模式需要向量索引与 API key：先 python3 tools/build_index.py 并配置 key")

    mode = args.mode
    if mode == "auto":
        mode = "hybrid" if has_vec else "keyword"

    kw = keyword_top(docs, args.query, k=12) if mode in ("keyword", "hybrid") else []
    if mode == "hybrid" and has_vec:
        sem = semantic_top(vi, args.query, k=12, api_key=api_key)
        results = rrf_merge(kw, sem, args.k)
        via = "混合(关键词+向量)"
    elif mode == "semantic":
        sem = semantic_top(vi, args.query, k=args.k + 5, api_key=api_key)
        results = [(s, by_path.get(m["path"], m)) for s, m in sem][: args.k]
        via = "向量语义"
    else:
        results = [(s, d) for s, d in kw[: args.k]]
        via = "关键词" + ("" if has_vec else "（无向量索引）")

    if args.json:
        out = [{
            "rank": i + 1, "score": round(s, 3),
            "path": d["path"], "category": d.get("category", ""),
            "zh_title": d.get("zh_title", ""), "title": d.get("title", ""),
            "summary": d.get("summary", ""), "tags": d.get("tags", []),
        } for i, (s, d) in enumerate(results)]
        print(json.dumps(out, ensure_ascii=False, indent=1))
        return

    print(f'检索: "{args.query}"  模式: {via}  →  {len(results)} 条\n' + "=" * 64)
    for i, (s, d) in enumerate(results, 1):
        name = d.get("zh_title") or d.get("title") or d.get("file")
        print(f"\n[{i}] {name}  (相关度 {s:.2f})")
        if d.get("zh_title") and d.get("title"):
            print(f"    英文名: {d['title']}")
        print(f"    分类: {d.get('category', '')}   路径: {d['path']}")
        if d.get("summary"):
            print(f"    中文概述: {d['summary']}")
        if d.get("tags"):
            print(f"    关键词: {'、'.join(d['tags'])}")
        if args.c == i:
            p = REPO_ROOT / d["path"]
            print(f"\n    >>> 完整文件 {p}:\n")
            print(p.read_text(encoding="utf-8", errors="replace")[:2000])


if __name__ == "__main__":
    main()
