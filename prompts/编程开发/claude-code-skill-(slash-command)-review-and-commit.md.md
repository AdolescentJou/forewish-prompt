# Claude Code Skill (Slash Command): review-and-commit.md

## 说明

用途概述：--- allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*) description: Create a git commit --- ## Context - Current git status: !
中文概述：Claude Code 斜杠命令技能：审查现有改动并按常规提交格式创建 git commit。
关键词：Claude Code、斜杠命令、git commit、代码审查、常规提交

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@DoguD](https://github.com/DoguD)
- 类型：结构化(JSON/模版)（原始类型 STRUCTURED）
- 面向开发者：否

## Prompt 内容

```text
---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*)
description: Create a git commit
---

## Context

- Current git status: !`git status`
- Current git diff (staged and unstaged changes): !`git diff HEAD`
- Current branch: !`git branch --show-current`
- Recent commits: !`git log --oneline -10`

## Your task

Review the existing changes and then create a git commit following the conventional commit format. If you think there are more than one distinct change you can create multiple commits.
```
