# Strict Markdown-Only Output Enforcement

## 说明

用途概述：Send the entire response as ONE uninterrupted ```markdown fenced block only.
中文概述：强制 AI 整段回复只含一个不间断的 markdown fenced block，块外零文字
关键词：输出约束、markdown、output-format、格式强制

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@maxhayim](https://github.com/maxhayim)
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
Send the entire response as ONE uninterrupted ```markdown fenced block only. No prose before or after. No nested code blocks. No formatting outside the block.
```
