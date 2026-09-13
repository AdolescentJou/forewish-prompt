#!/usr/bin/env python3
"""
verify_chunks.py —— 校验子代理产出的 chunk JSON 质量与完整性

用法：python3 tools/verify_chunks.py [chunk_id ...]   （缺省校验全部已产出）
输出：每个 chunk 的行数/缺失文件/非法项/超长概述/标签数异常；最后给汇总。
"""
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CHUNKS_DIR = REPO_ROOT / "tools" / "chunks"
OVERVIEWS_DIR = REPO_ROOT / "tools" / "overviews"
MANIFEST = json.loads((CHUNKS_DIR / "manifest.json").read_text(encoding="utf-8"))
SUMMARY_MAX = 80  # 放宽到 80 字符作硬限（人工概述约 45 字内）


def cjk_len(s: str) -> int:
    return len(re.findall(r"[\u4e00-\u9fff]", s))


def check_chunk(cid: int) -> dict:
    rec = next((m for m in MANIFEST if m["chunk"] == cid), None)
    if rec is None:
        return {"chunk": cid, "error": "manifest 中不存在"}
    files = rec["files"]
    out = OVERVIEWS_DIR / f"chunk_{cid:03d}.json"
    if not out.exists():
        return {"chunk": cid, "error": "输出文件不存在", "expect": len(files)}
    try:
        items = json.loads(out.read_text(encoding="utf-8"))
    except Exception as e:
        return {"chunk": cid, "error": f"JSON 解析失败: {e}"}
    if not isinstance(items, list):
        return {"chunk": cid, "error": "不是数组"}
    got = {it.get("file") for it in items}
    expect = set(files)
    missing = expect - got
    extra = got - expect
    problems = []
    dup = len(items) - len(got)
    if dup > 0:
        problems.append(f"重复条目 {dup} 个")
    for it in items:
        f = it.get("file")
        s = (it.get("summary") or "").strip()
        tags = it.get("tags") or []
        if not s:
            problems.append(f"[{f}] 概述为空")
        elif len(s) > SUMMARY_MAX:
            problems.append(f"[{f}] 概述超长({len(s)}字): {s[:30]}…")
        elif cjk_len(s) == 0:
            problems.append(f"[{f}] 概述无中文: {s[:30]}")
        if not (3 <= len(tags) <= 6):
            problems.append(f"[{f}] 标签数异常({len(tags)})")
        elif any(not t.strip() for t in tags):
            problems.append(f"[{f}] 含空标签")
        if f and not (REPO_ROOT / f).exists():
            problems.append(f"[{f}] 文件不存在")
    return {
        "chunk": cid, "category": rec["category"], "expect": len(files),
        "got": len(items), "missing": sorted(missing), "extra": sorted(extra),
        "problems": problems,
    }


def main():
    ids = [int(a) for a in sys.argv[1:]] if len(sys.argv) > 1 else None
    results = []
    for m in MANIFEST:
        cid = m["chunk"]
        if ids and cid not in ids:
            continue
        if (OVERVIEWS_DIR / f"chunk_{cid:03d}.json").exists():
            results.append(check_chunk(cid))
    if not results:
        print("尚无任何 chunk 产出")
        return
    n_ok = 0
    for r in sorted(results, key=lambda x: x["chunk"]):
        if "error" in r:
            print(f"chunk_{r['chunk']:03d}  ✗ {r['error']}" + (f"（应含 {r.get('expect')} 条）" if "expect" in r else ""))
            continue
        flag = "✓" if not (r["missing"] or r["extra"] or r["problems"]) else "!"
        if flag == "✓":
            n_ok += 1
        print(f"chunk_{r['chunk']:03d}  {flag} {r['category']} 期望{r['expect']}/实收{r['got']}"
              + (f" 缺{len(r['missing'])} 多{len(r['extra'])} 问题{len(r['problems'])}" if flag == "!" else ""))
        for p in r["problems"][:5]:
            print(f"      - {p}")
    total = sum(r.get("got", 0) for r in results if "error" not in r)
    print(f"\n汇总: 已核验 {len(results)} 批，通过 {n_ok} 批，累计条目 {total}")


if __name__ == "__main__":
    main()
