#!/usr/bin/env python3
"""
dedupe.py —— 检测 prompts/ 库中的重复文件，输出报告供人工确认

三个检测层次：
  A. md5(原始内容) 相同            -> 完全重复，直接可合并
  B. 规范化正文（去空白/代码围栏/大小写差异后）相同 -> 实质重复，可合并
  C. 归一化英文标题相同但内容不同    -> 仅疑似（撞名），报告不自动合并

合并原则（在报告中给出建议保留哪个文件）：
  1. 被 STARTER.md / HOW-TO.md 引用的文件优先保留
  2. 否则保留 Prompt 正文更长的
  3. 否则保留分类更具体的（排除"其他"）

输出：tools/reports/duplicates.md
用法：
  python3 tools/dedupe.py            # 检测并输出报告
"""
import hashlib
import json
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PROMPTS_DIR = REPO_ROOT / "prompts"
REPORT_FILE = REPO_ROOT / "tools" / "reports" / "duplicates.md"

SKIP_NAMES = {"INDEX.md", "README.md"}


def rel(p: Path) -> str:
    return str(p.relative_to(REPO_ROOT))


def raw_md5(content: bytes) -> str:
    return hashlib.md5(content).hexdigest()


def normalize_text(s: str) -> str:
    """正文规范化：去 markdown 围栏/标记、空白、常见噪声，统一小写。"""
    s = re.sub(r"```[a-z]*", " ", s)
    s = re.sub(r"[#*>`\[\]()|_\-]+", " ", s)
    s = unicodedata.normalize("NFKC", s)
    s = re.sub(r"\s+", " ", s).strip().lower()
    return s


def normalize_title(stem: str) -> str:
    """文件名 stem 归一化：去分隔符与扩展编号噪声。"""
    s = re.sub(r"[-_.\s]+", " ", stem).strip().lower()
    s = re.sub(r"\s+", " ", s)
    return s


def title_of(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace").splitlines()[0].lstrip("#").strip()


def extract_prompt_body(path: Path) -> str:
    """取 ## Prompt 内容 之后的正文（规范前）"""
    txt = path.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"## Prompt 内容\s*\n", txt)
    return txt[m.end():] if m else txt


def refs_from_root_files() -> tuple[set, dict]:
    """解析 STARTER.md/HOW-TO.md 中的文件引用；返回 (被引路径集合, 路径->引用信息)"""
    refd = set()
    info = defaultdict(list)
    for name in ("STARTER.md", "HOW-TO.md"):
        f = REPO_ROOT / name
        if not f.exists():
            continue
        for line in f.read_text(encoding="utf-8").splitlines():
            for m in re.finditer(r"\]\(([^)]+)\)", line):
                link = m.group(1)
                if link.startswith(("http", "#")):
                    continue
                # 解码 url 编码的相对路径
                from urllib.parse import unquote
                p = unquote(link).lstrip("./")
                refd.add(p)
                info[p].append(name)
    return refd, info


def main():
    files = sorted(
        p for p in PROMPTS_DIR.rglob("*.md")
        if p.name not in SKIP_NAMES and p.is_file()
    )
    print(f"扫描到 {len(files)} 个 prompt 文件")

    refd, ref_info = refs_from_root_files()
    print(f"STARTER/HOW-TO 引用 {len(refd)} 个文件")

    # ---------- 层次 A / B ----------
    groups_raw: dict[str, list] = defaultdict(list)   # md5 -> files
    groups_norm: dict[str, list] = defaultdict(list)  # normalized body -> files
    body_cache: dict[str, str] = {}

    for p in files:
        relp = rel(p)
        content = p.read_bytes()
        groups_raw[raw_md5(content)].append(relp)
        norm = normalize_text(extract_prompt_body(p))
        body_cache[relp] = norm
        if norm:
            groups_norm[norm].append(relp)

    dupA = [v for v in groups_raw.values() if len(v) > 1]
    dupB_raw = [v for v in groups_norm.values() if len(v) > 1]

    # B 组与 A 组去重（同内容的 md5 组算 A 就够了，避免重复报告）
    a_sets = [frozenset(g) for g in dupA]
    dupB = []
    for g in dupB_raw:
        gs = frozenset(g)
        if any(gs.issubset(a) for a in a_sets):
            continue
        dupB.append(sorted(g))
    dupA = sorted(dupA)
    print(f"A 完全重复组: {len(dupA)}，B 实质重复组: {len(dupB)}")

    # ---------- 层次 C：标题撞名 ----------
    title_map: dict[str, list] = defaultdict(list)
    for p in files:
        title_map[normalize_title(p.stem)].append(rel(p))
    dupC = sorted([sorted(v) for v in title_map.values() if len(v) > 1])
    print(f"C 标题撞名组: {len(dupC)}")

    # ---------- 保留建议 ----------
    def pick_keep(group: list[str]) -> str:
        """按 引用优先 -> 正文更长 -> 分类更具体 选保留文件"""
        def score(rp: str):
            p = REPO_ROOT / rp
            s = 0
            if rp in refd:
                s += 1000
            s += min(len(body_cache.get(rp, "")), 20000)
            # 分类具体度：其他 扣分
            if "/其他/" in rp:
                s -= 50
            return s
        return max(group, key=score)

    # ---------- 生成报告 ----------
    lines = []
    lines.append("# 重复检测报告\n")
    lines.append(f"- 扫描文件数：{len(files)}")
    lines.append(f"- A 完全重复组：{len(dupA)} 组，涉及文件 {sum(len(g) for g in dupA)} 个")
    lines.append(f"- B 实质重复组：{len(dupB)} 组，涉及文件 {sum(len(g) for g in dupB)} 个")
    lines.append(f"- C 标题撞名组（仅提示）：{len(dupC)} 组\n")
    lines.append("> A/B 组是**建议合并删除**的候选；C 组仅提示，不默认删除。"
                 "每组首行 = 建议保留文件。合并删除需逐批人工确认。\n")

    for label, groups in (("A. 完全重复", dupA), ("B. 实质重复", dupB)):
        lines.append(f"\n## {label}\n")
        for i, g in enumerate(groups, 1):
            keep = pick_keep(g)
            lines.append(f"### 组{i}（{len(g)} 个文件）")
            lines.append(f"- 保留：`{keep}`" + ("（STARTER/HOW-TO 已引用）" if keep in refd else ""))
            for rp in g:
                if rp != keep:
                    lines.append(f"- 删除候选：`{rp}`")
            lines.append("")

    lines.append("\n## C. 标题撞名（内容不同，仅提示，不删除）\n")
    for g in dupC:
        for rp in g:
            lines.append(f"- `{rp}`")
        lines.append("")

    REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)
    REPORT_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"报告已生成：{REPORT_FILE}")

    # ---------- 简单统计 ----------
    del_total = sum(len(g) - 1 for g in dupA) + sum(len(g) - 1 for g in dupB)
    print(f"若全部确认：可删除 {del_total} 个重复文件（剩 {len(files) - del_total} 个）")
    # 顶层分类 × 文件数
    cat_counts = defaultdict(int)
    for rp in files:
        cat_counts[Path(rp).parent.name] += 1
    print("分类文件数：", dict(sorted(cat_counts.items(), key=lambda x: -x[1])))


if __name__ == "__main__":
    main()
