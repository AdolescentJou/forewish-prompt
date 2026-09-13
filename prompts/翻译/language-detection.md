# Language Detection

## 说明

用途概述：**Important - Language Detection:** - **Primary method:** If location metadata is available (e.
中文概述：规定对话语言检测规则：优先用 locale 元数据，否则按首次回复语言确定并全程沿用
关键词：语言检测、Locale、元数据、对话语言、回退策略

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@s-celles](https://github.com/s-celles)
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
**Important - Language Detection:** 

- **Primary method:** If location metadata is available (e.g., user locale, browser language, or system language settings), use it to determine the conversation language from the start.

- **Fallback method:** If no metadata is available, detect the language of my first response and continue the entire conversation in that language.
```
