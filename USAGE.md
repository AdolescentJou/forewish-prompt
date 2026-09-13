# forewish-prompt 使用指南

个人 Prompt 收藏库（2431 条 + 工具链）。**你想干什么 → 直接问我**，
我用离线检索帮你精准定位模板；也可以自己命令行检索。

## 我怎么帮你找 prompt

直接提问即可，例如：
- “我想优化简历通过 ATS 筛选，有模板吗？”
- “帮我写小红书带货文案”
- “让 AI 扮演面试官模拟面试”
- “把这段英文润色得更地道”

我会：跑本地检索 → 核对最相关文件 → 把「中文概述 + 文件 + 完整模板」发给你，
必要时帮你组合、改写、按你的场景定制。

## 命令行检索（可选）

```bash
# 首次或概述更新后重建检索库
python3 tools/make_library.py

# 检索：默认「关键词 + 向量语义 双路融合」，向量索引存在且有 key 时自动启用
python3 tools/ask.py "优化简历通过 ATS 筛选" -k 5
python3 tools/ask.py "小红书 带货 文案" -k 3 --json
python3 tools/ask.py "give me feedback on my code" -k 3 -c 1   # -c N 打印第 N 名完整 prompt

# 指定模式（对比/调试用）
python3 tools/ask.py "xxx" --mode keyword    # 纯关键词（离线）
python3 tools/ask.py "xxx" --mode semantic   # 纯向量语义
python3 tools/ask.py "xxx" --mode hybrid     # 双路融合（默认）
```

### 向量检索（语义升级，默认已启用）

embedding 走 OpenAI 兼容网关，本库配置为美团桑基网关：
- key 写入 `tools/.openai_key`（已 gitignore，绝不入库）；
- 网关 base 写入 `tools/.openai_base`（或环境变量 `OPENAI_BASE_URL`）；
- 模型默认 `text-embedding-3-small`（环境变量 `OPENAI_EMBED_MODEL` 可改）。

```bash
# 构建向量索引（tools/index_data/，gitignore；增量：只处理新增/改动文件）
python3 tools/build_index.py
python3 tools/build_index.py --rebuild    # 全量重建
```

两种检索的差异：关键词=字面命中（离线免费）；向量=语义相似（同义/意译也能搜到，
如 “give me feedback on my code” ↔ 概述里的“代码评审”）。`ask.py` 默认把两路结果
做**加权 RRF 融合**取长补短。注意两路分数不可比（关键词是加权命中分、向量是 0~1 余弦），
看相对次序即可。

## 文件都在哪

| 路径 | 内容 |
|---|---|
| `prompts/<分类>/<名字>.md` | 每个 prompt 一个文件；头部含 `中文概述` 与 `关键词`（检索与浏览都靠它） |
| `prompts/README.md` | 18 个分类入口与计数 |
| `tools/library.jsonl` | 机器检索库（由各文件头部生成） |
| `tools/zh_titles.json` | 289 条人工中文标题留存（原 STARTER/HOW-TO 抽取） |

## 分类速览

其他(701) · 编程开发(529) · 图像生成(213) · 文章写作(140) · 效率工具(138) ·
商业职业(114) · 数据分析(108) · 搜索研究(99) · 生活健康(87) · 教育教学(73) ·
文案营销(71) · 角色扮演(56) · 视频生成(33) · 游戏娱乐(33) · 翻译(12) ·
语言学习(12) · 音乐创作(12) · 成人内容(3)

## 新增 / 修改 prompt 后如何维护

```bash
# 1) 新文件补一行中文概述（也可让我代写）
#    在文件 ## 说明 块内加：
#    中文概述：让 AI 扮演…，做…，产出…
#    关键词：标签1、标签2、标签3

# 2) 重建检索库 + 刷新 README 计数
python3 tools/make_library.py
python3 tools/make_indexes.py
#    （如确需重建 TOTAL.md / 分类 INDEX.md：加 --total / --index）
```

## 工具一览（tools/）

| 脚本 | 作用 |
|---|---|
| `ask.py` | 离线中文/英文检索（主入口） |
| `make_library.py` | 由 md 头部生成 `library.jsonl` |
| `make_indexes.py` | 刷新 README 计数（--total/--index 可选重建） |
| `add_overview.py` | 把 中文概述+关键词 幂等写回文件 |
| `consume_overviews.py` | 批量安全写回子代理产出 |
| `dedupe.py` | 重复文件检测（报告在 tools/reports/） |
| `split_chunks.py` | 批量概述用的分块工具（内部） |
| `build_index.py` / `search.py` | 可选：OpenAI 向量语义索引与检索 |
