#!/usr/bin/env python3
"""
consume_overviews.py —— 安全地把 tools/overviews/*.json 写回 prompts 文件

- 逐个解析 overviews 中的 chunk JSON
- 解析失败或写回失败的文件保留，绝不删除
- 写回成功后删除该源 JSON
用法：python3 tools/consume_overviews.py
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from add_overview import insert_overview  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
OVERVIEWS_DIR = REPO_ROOT / "tools" / "overviews"


def main():
    total_ok = total_skip = 0
    for jf in sorted(OVERVIEWS_DIR.glob("chunk_*.json")):
        try:
            items = json.loads(jf.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"!! {jf.name} 解析失败，保留: {e}")
            continue
        n_ok = n_skip = n_bad = 0
        problems = []
        for it in items:
            rel = it.get("file")
            p = REPO_ROOT / rel if rel else None
            if not p or not p.exists():
                problems.append(f"[{rel}] 文件不存在")
                n_bad += 1
                continue
            content = p.read_text(encoding="utf-8")
            new = insert_overview(content, (it.get("summary") or "").strip(),
                                  [t.strip() for t in (it.get("tags") or []) if t.strip()])
            if new is None:
                n_skip += 1
            else:
                p.write_text(new, encoding="utf-8")
                n_ok += 1
        if problems:
            print(f"!! {jf.name} 存在 {len(problems)} 个问题（保留文件）:")
            for pr in problems[:5]:
                print(f"    {pr}")
            continue
        # 全部成功（或全跳过）才删除源文件
        jf.unlink()
        total_ok += n_ok
        total_skip += n_skip
        print(f"OK {jf.name}: 写回 {n_ok}，跳过 {n_skip}")
    print(f"完成: 累计写回 {total_ok}，跳过 {total_skip}")


if __name__ == "__main__":
    main()
