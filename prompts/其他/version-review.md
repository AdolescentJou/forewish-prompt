# Version Review

## 说明

用途概述：There has been mulitple changes, improvements and new features since the last version tag 1.
中文概述：让 AI 对比版本标签做全面代码评审：查硬编码漏翻译、简化重构并做安全审查
关键词：代码评审、版本对比、i18n、重构、安全审查

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@DoguD](https://github.com/DoguD)
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
There has been mulitple changes, improvements and new features since the last version tag 1.0.3.
  I want you to performa a full-scale review. Go through every file that has been changed while looking at the git logs to understand the intention.
  - What I want you to do is for the app side see if there is any new hardcoded string or a string that has been only added to English and missing from the Turkish one, if you find any fix it.
  - Again for the app side go through all the new changes and see if there is anything that could be simplifed, for example if there are identical style definitions merge them following the best practices. In general if any best practice nudges you to
  simplify a section, do so.
  - Perform a full security review on the app side.
```
