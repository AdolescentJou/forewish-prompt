# security fixes

## 说明

用途概述：--- name: security-fixes description: in order to fix security issues in my codebase which is flagged by code scanning for refrences like user input comping as
中文概述：让 AI 修复代码扫描标记的用户输入类安全漏洞，保证不破坏现有功能并为改动补测试用例
关键词：安全修复、代码扫描、漏洞、测试用例、输入校验

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：abhinavme1004@gmail.com
- 类型：结构化(JSON/模版)（原始类型 STRUCTURED）
- 面向开发者：是

## Prompt 内容

```text
---
name: security-fixes
description: in order to fix security issues in my codebase which is flagged by code scanning for refrences like user input comping as part o request could be vulnerable and how can we fix it
---

# security fixes

it should identify the issue and fix  it with respect to current project checking it should not break the existing functionality and a proper test case should be written for the change

## Instructions

check the issue 
fix it 
test case
- Step 2: ...
```
