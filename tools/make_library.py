#!/usr/bin/env python3
"""
make_library.py —— 从 prompts/**/*.md 头部解析生成检索库 tools/library.jsonl

每行一条：{path, category, file, title, summary, tags, desc, excerpt}
  - title    ：文件首个 # 标题（通常为英文原名）
  - zh_title ：STARTER.md/HOW-TO.md 引用的中文名（若有）
  - summary  ：文件头 中文概述： 行
  - tags     ：文件头 关键词： 行（按顿号/逗号/空格切分）
  - desc     ：说明块文本（用途概述等，前 300 字）
  - excerpt  ：Prompt 正文前 400 字（去围栏）
用法：python3 tools/make_library.py
"""
import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PROMPTS_DIR = REPO_ROOT / "prompts"
OUT = REPO_ROOT / "tools" / "library.jsonl"
SKIP_NAMES = {"INDEX.md", "README.md"}

# 中文名来源：tools/zh_titles.json（从已删除的 STARTER/HOW-TO 抽取留存）
ZH_FILE = REPO_ROOT / "tools" / "zh_titles.json"


def zh_titles_from_root() -> dict:
    if ZH_FILE.exists():
        return json.loads(ZH_FILE.read_text(encoding="utf-8"))
    return {}


def split_tags(s: str) -> list[str]:
    s = s.strip()
    if not s:
        return []
    tags = re.split(r"[、,，;；/|]", s)
    out = []
    for t in tags:
        t = t.strip()
        # 允许空格分隔的英文词组，拆成单词
        for w in re.split(r"\s+", t):
            if w:
                out.append(w)
    return out


def parse_file(p: Path) -> dict:
    txt = p.read_text(encoding="utf-8", errors="replace")
    title = ""
    summary, tags, desc = "", [], ""
    for ln in txt.splitlines():
        if ln.startswith("# ") and not title:
            title = ln[2:].strip()
        if ln.startswith("中文概述："):
            summary = ln[len("中文概述："):].strip()
        elif ln.startswith("关键词："):
            tags = split_tags(ln[len("关键词："):])
    m = re.search(r"## 说明\s*\n(.*?)(?=\n## |\Z)", txt, re.S)
    if m:
        desc = re.sub(r"\s+", " ", m.group(1)).strip()[:300]
    body = ""
    m = re.search(r"## Prompt 内容\s*\n(.*)", txt, re.S)
    if m:
        body = re.sub(r"```[a-z]*", " ", m.group(1))
        body = re.sub(r"\s+", " ", body).strip()[:400]
    return {
        "path": str(p.relative_to(REPO_ROOT)),
        "category": p.parent.name,
        "file": p.name,
        "title": title,
        "summary": summary,
        "tags": tags,
        "desc": desc,
        "excerpt": body,
    }


def main():
    zh_map = zh_titles_from_root()
    files = sorted(
        p for p in PROMPTS_DIR.rglob("*.md")
        if p.name not in SKIP_NAMES and p.is_file()
    )
    n = 0
    n_sum = 0
    with open(OUT, "w", encoding="utf-8") as f:
        for p in files:
            rec = parse_file(p)
            rel = rec["path"]
            rec["zh_title"] = zh_map.get(rel, "")
            if rec["summary"]:
                n_sum += 1
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            n += 1
    print(f"生成 {OUT}: {n} 条（含中文概述 {n_sum} 条）")


if __name__ == "__main__":
    main()
