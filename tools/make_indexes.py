#!/usr/bin/env python3
"""
make_indexes.py —— 刷新 prompts/README.md 的分类计数与链接（默认）

已按需求移除默认生成 TOTAL.md / 分类 INDEX.md 的行为（相关文件已删除）。
如确需重新生成，可显式：
  python3 tools/make_indexes.py --total     # 重建根目录 TOTAL.md
  python3 tools/make_indexes.py --index     # 重建各分类 INDEX.md
用法：python3 tools/make_indexes.py
"""
import json
import re
import urllib.parse
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PROMPTS_DIR = REPO_ROOT / "prompts"
SKIP_NAMES = {"INDEX.md", "README.md"}


def parse_md(p: Path) -> dict:
    txt = p.read_text(encoding="utf-8", errors="replace")
    title = summary = typ = source = ""
    for ln in txt.splitlines():
        if ln.startswith("# ") and not title:
            title = ln[2:].strip()
        elif ln.startswith("中文概述："):
            summary = ln[len("中文概述："):].strip()
        elif ln.startswith("- 类型："):
            typ = ln[len("- 类型："):].strip()
        elif ln.startswith("- 来源仓库："):
            m = re.search(r"\[([^\]]+)\]", ln)
            source = m.group(1) if m else ln[len("- 来源仓库："):].strip()
    if not typ:
        typ = "prompt"
    if not source:
        # 兜底：Fabric 原始名称行 / 其他
        m = re.search(r"- 原始名称：(.+)", txt)
        source = f"Fabric({m.group(1).strip()})" if m else "-"
    return {"title": title or Path(p).stem, "summary": summary, "type": typ, "source": source}


def collect() -> dict[str, list]:
    """分类 -> 按文件名排序的条目列表（相对 prompts/ 的路径）"""
    out = defaultdict(list)
    for p in sorted(PROMPTS_DIR.rglob("*.md")):
        if p.name in SKIP_NAMES or not p.is_file():
            continue
        rel = str(p.relative_to(PROMPTS_DIR))
        meta = parse_md(p)
        out[p.parent.name].append({"rel": rel, "name": p.name, **meta})
    for v in out.values():
        v.sort(key=lambda x: x["name"].lower())
    return out


def type_label(t: str) -> str:
    # 复用现有目录习惯：纯文本/结构化等原样；其余归一为 prompt
    if "纯文本" in t or "结构化" in t or "图像" in t or "prompt" in t.lower():
        return f"【{t}】" if not t.startswith("【") else t
    return "【prompt】"


def write_category_indexes(data: dict) -> None:
    for cat, items in data.items():
        d = PROMPTS_DIR / cat
        lines = [f"# {cat} 分类目录\n", f"共 {len(items)} 条 prompt。\n", "## prompt\n"]
        for it in items:
            link = urllib.parse.quote(it["name"])
            summ = it["summary"] or ""
            title = it["title"]
            line = f"- {type_label(it['type'])}[{title}]({link})"
            if summ:
                line += f" ｜ {summ}"
            lines.append(line)
        lines.append("\n[← 返回上级目录 README](../README.md)\n")
        (d / "INDEX.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"已重建 {len(data)} 个分类 INDEX.md")


def write_total(data: dict) -> None:
    total = sum(len(v) for v in data.values())
    order = sorted(data, key=lambda c: -len(data[c]))
    lines = [
        "# 全量 Prompt 目录（TOTAL）\n",
        f"共 {total} 条 prompt。每条含中文概述与关键词，可直接在本文内用中文全文搜索。\n",
        "> 本文件由 tools/make_indexes.py 自动生成；新增 prompt 后重跑即可。\n",
    ]
    for cat in order:
        items = data[cat]
        lines.append(f"\n## {cat}（{len(items)} 条）\n")
        for it in items:
            rel_enc = urllib.parse.quote(it["rel"])
            src = f"来源：{it['source']}"
            parts = [f"- {type_label(it['type'])}[{it['title']}](prompts/{rel_enc})", it["title"], src]
            if it["summary"]:
                parts.append(it["summary"])
            lines.append(" ｜ ".join(parts))
    (REPO_ROOT / "TOTAL.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"已重建 TOTAL.md（{total} 条）")


def refresh_readme(data: dict) -> None:
    rp = PROMPTS_DIR / "README.md"
    if not rp.exists():
        return
    txt = rp.read_text(encoding="utf-8")
    total = sum(len(v) for v in data.values())
    # 头部总数：共 NNNN 条
    txt = re.sub(r"共 \d+ 条", f"共 {total} 条", txt, count=1)
    for cat, items in data.items():
        # 链接指向分类目录（已不再用 INDEX.md），并刷新条数
        txt = re.sub(
            rf"\[{cat}\]\([^)]*\)\s*（\d+ 条）",
            f"[{cat}]({cat}/)（{len(items)} 条）",
            txt,
        )
    rp.write_text(txt, encoding="utf-8")
    print("已刷新 prompts/README.md 计数与链接")


def main():
    import argparse
    ap = argparse.ArgumentParser(description="刷新索引（默认只更新 README）")
    ap.add_argument("--total", action="store_true", help="额外重建根目录 TOTAL.md")
    ap.add_argument("--index", action="store_true", help="额外重建各分类 INDEX.md")
    args = ap.parse_args()

    data = collect()
    if args.total:
        write_total(data)
    if args.index:
        write_category_indexes(data)
    refresh_readme(data)
    print("完成")


if __name__ == "__main__":
    main()
