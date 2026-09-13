#!/usr/bin/env python3
"""
search.py —— 语义检索 prompt 库

用法：
  export OPENAI_API_KEY=sk-xxx
  python3 tools/search.py "我想优化简历通过 ATS 筛选"
  python3 tools/search.py "帮我debug一段Python代码" -k 8
  python3 tools/search.py "做菜" --json     # 输出 JSON（供程序调用）
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_index import MODEL, VECTORS_FILE, META_FILE, embed_texts, resolve_api_key  # noqa: E402


def load_index():
    if not VECTORS_FILE.exists() or not META_FILE.exists():
        print("错误：索引不存在，请先运行 python3 tools/build_index.py", file=sys.stderr)
        sys.exit(1)
    with open(META_FILE, encoding="utf-8") as f:
        metas = [json.loads(line) for line in f if line.strip()]
    vecs = np.load(VECTORS_FILE)
    return metas, vecs


def search(query: str, k: int = 5, api_key: str = "") -> list[dict]:
    metas, vecs = load_index()
    qv = np.asarray(embed_texts([query], api_key)[0], dtype=np.float32)
    qv = qv / (np.linalg.norm(qv) or 1.0)
    scores = vecs @ qv  # 已归一化，点积 = 余弦相似度
    top = np.argsort(-scores)[:k]
    return [
        {**metas[i], "score": round(float(scores[i]), 4)}
        for i in top
    ]


def main():
    parser = argparse.ArgumentParser(description="prompt 库语义检索")
    parser.add_argument("query", help="自然语言描述你想做的事情，中英文均可")
    parser.add_argument("-k", type=int, default=5, help="返回 Top-K 条结果（默认 5）")
    parser.add_argument("--json", action="store_true", help="以 JSON 输出")
    args = parser.parse_args()

    api_key = resolve_api_key()
    if not api_key:
        print("错误：未找到 API key。请 export OPENAI_API_KEY=sk-xxx 或写入 tools/.openai_key", file=sys.stderr)
        sys.exit(1)

    results = search(args.query, args.k, api_key)

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return

    print(f'检索: "{args.query}"  共 {len(results)} 条结果\n' + "=" * 60)
    for r, item in enumerate(results, 1):
        title = item["zh_title"] or item["title"]
        print(f"\n[{r}] {title}   (相关度 {item['score']:.3f})")
        print(f"    分类: {item['category']}")
        print(f"    文件: {item['path']}")
        if item.get("summary"):
            print(f"    中文概述: {item['summary']}")
        if item.get("tags"):
            print(f"    关键词: {'、'.join(item['tags'])}")
        elif item.get("desc"):
            print(f"    简介: {item['desc']}")
        else:
            print(f"    摘要: {item['excerpt'][:80]}...")


if __name__ == "__main__":
    main()
