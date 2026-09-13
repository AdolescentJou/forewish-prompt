# forewish-prompt

个人 AI Prompt 收藏与管理库：**2400+ 个高质量 prompt 模板 + 中文检索工具链**。

数据整合自 [f/prompts.chat](https://github.com/f/prompts.chat)（Awesome ChatGPT Prompts）、
[dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) 与
[danielmiessler/Fabric](https://github.com/danielmiessler/Fabric)，按用途整理为 18 个中文分类，
并为每个文件生成了一行**中文概述**与**中英关键词**（写在每个 md 的头部）。

## 怎么用

- 最快的方式：**直接问我**（把本库当作我的知识库）——“我想优化简历过 ATS / 写小红书带货文案 /
  模拟面试 / 润色英文”，我会在库里检索并把最相关模板+中文概述发给你。
- 或命令行：`python3 tools/ask.py "你想做的事"`（详见 [USAGE.md](USAGE.md)）。

## 目录结构

```
forewish-prompt/
├── prompts/            # 2431 个 prompt 文件（18 个中文分类，每个文件头部含中文概述/关键词）
│   ├── 编程开发/  图像生成/  文章写作/  效率工具/  商业职业/  ……
│   └── README.md       # 分类入口与计数
├── tools/              # 工具链（ask/make_library/build_index/…）
│   ├── library.jsonl   # 检索库（由各文件头部生成）
│   └── zh_titles.json  # 289 条人工中文标题留存
├── USAGE.md            # 使用与维护指南
└── README.md
```

> 原 STARTER.md / HOW-TO.md / TOTAL.md 与各分类 INDEX.md 已按需求删除
> （git 历史中可随时找回），检索统一走 ask.py 或直接问我。

## 维护

新增或修改 prompt 后，在文件 `## 说明` 块补上：
```markdown
中文概述：让 AI 扮演…，做…，产出…
关键词：标签1、标签2、标签3
```
然后运行 `python3 tools/make_library.py` 重建检索库（新文件会自动进索引）；
`python3 tools/make_indexes.py` 刷新 README 计数。（也可以让我代劳。）

> 本仓库为 git 仓库，所有批量改动均可回滚。
