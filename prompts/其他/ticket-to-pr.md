# ticket-to-pr

## 说明

用途概述：--- name: ticket-to-pr description: Full development lifecycle for a Jira ticket.
中文概述：定义 skill：从 Jira ticket 取需求、OpenSpec 设计、实现验证并开启 Bitbucket PR。
关键词：skill、Jira、开发流程、OpenSpec、Bitbucket PR

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：rsdarab@gmail.com
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
---
name: ticket-to-pr
description: Full development lifecycle for a Jira ticket. Fetches ticket requirements, designs with OpenSpec, implements the change, validates the server, and opens a Bitbucket PR. Use when starting a new feature or bug fix driven by a Jira ticket.
---

# ticket-to-pr

Before continuing to the next step in the skill, ensure that you confirm with the user that the work completed in that step is correct and sufficient. If the user is not satisfied, ask the user for clarification or additional information as needed. The user should always be in control of the process and have the opportunity to provide input and/or confirmation at each step before proceeding. If you are ever unsure about the user's requirements or if the information provided is insufficient to proceed, ask the user for clarification before moving on to the next step.

## Instructions

- Step 1: ...
- Step 2: ...
```
