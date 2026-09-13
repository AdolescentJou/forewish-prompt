# Spec Interview

## 说明

用途概述：read this${specmd:spec.
中文概述：AI 读取 spec.md 后用提问工具深度访谈技术实现与 UI/UX，持续到问完并写入规格文件。
关键词：需求访谈、spec、提问工具、技术设计、UI/UX、规格文档

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：marcosnunesmbs@gmail.com
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
read this${specmd:spec.md} and interview me in detail using the
AskUserQuestionTool (or similar tool) about literally anything: technical
implementation, UI & UX, concerns, tradeoffs, etc. but make
sure the questions are not obvious

be very in-depth and continue interviewing me continually until
it's complete, then write the spec to the file
```
