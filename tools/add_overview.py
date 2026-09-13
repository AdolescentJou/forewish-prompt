#!/usr/bin/env python3
"""
add_overview.py —— 把中文概述与关键词幂等写回 prompt 文件头部

输入 JSON：一个数组，每项：
  {"file": "prompts/编程开发/linux-terminal.md", "summary": "让 AI 模拟 Linux 终端…", "tags": ["Linux","终端模拟","命令行"]}
插入位置：## 说明 块末尾（兼容 用途概述：… / Fabric 无前缀描述 / 任意描述体）
幂等：文件内已含“中文概述：”行则跳过。
用法：
  python3 tools/add_overview.py samples.json            # 写回
  python3 tools/add_overview.py samples.json --dry-run  # 只打印将要改动
"""
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def insert_overview(content: str, summary: str, tags: list[str]) -> str | None:
    """返回插入后的新内容；若已有中文概述则返回 None。"""
    if "中文概述：" in content:
        return None
    idx = content.find("## 说明")
    if idx == -1:
        # 没有 ## 说明 块：退化到第一个 ## 标题之后插入独立小节
        first_head = content.find("# ")
        if first_head == -1:
            return None
        after = content.find("\n", first_head)
        anchor = after + 1
        head_end_marker = "\n## "
        nxt = content.find(head_end_marker, anchor)
        block_end = nxt if nxt != -1 else len(content)
        block = content[anchor:block_end].strip("\n")
        if not block:
            insert_pos = block_end
            new_block = f"## 说明\n\n中文概述：{summary}\n关键词：{'、'.join(tags)}\n"
            return content[:insert_pos] + "\n" + new_block + "\n" + content[insert_pos:].lstrip("\n")
        return None

    # 说明块从 idx 到下一个二级标题或 EOF
    nxt = content.find("\n## ", idx)
    if nxt == -1:
        prefix = content[idx:].rstrip("\n")
        tail = ""
    else:
        prefix = content[idx:nxt].rstrip("\n")
        tail = content[nxt:].lstrip("\n")
    insert = f"\n中文概述：{summary}\n关键词：{'、'.join(tags)}"
    new_content = content[:idx] + prefix + insert
    if tail:
        new_content += "\n\n" + tail
    else:
        new_content += "\n"
    return new_content


def main():
    dry = "--dry-run" in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print("用法: python3 tools/add_overview.py <data.json> [--dry-run]")
        sys.exit(1)
    data = json.loads(Path(args[0]).read_text(encoding="utf-8"))
    changed = skipped = failed = 0
    for item in data:
        rel = item["file"]
        p = REPO_ROOT / rel
        if not p.exists():
            print(f"!! 不存在: {rel}", file=sys.stderr)
            failed += 1
            continue
        summary = (item.get("summary") or "").strip()
        tags = [t.strip() for t in (item.get("tags") or []) if t.strip()]
        if not summary:
            print(f"!! 缺概述: {rel}", file=sys.stderr)
            failed += 1
            continue
        content = p.read_text(encoding="utf-8")
        new = insert_overview(content, summary, tags)
        if new is None:
            skipped += 1
            continue
        if dry:
            print(f"[dry] {rel}")
        else:
            p.write_text(new, encoding="utf-8")
        changed += 1
    print(f"完成: 写回 {changed}，跳过(已有) {skipped}，失败 {failed}（dry-run={dry}）")


if __name__ == "__main__":
    main()
