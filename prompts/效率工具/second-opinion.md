# Second Opinion

## 说明

用途概述：--- name: second-opinion description: Second Opinion from Codex and Gemini CLI for Claude Code --- # Second Opinion When invoked: 1.
中文概述：AI 并行启动 gemini-consultant 与 codex-consultant 两个子代理，汇总双方对编程问题的看法、异同并给出建议。
关键词：second opinion、Gemini、Codex CLI、子代理、Claude Code

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@ilkerulusoy](https://github.com/ilkerulusoy)
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
---
name: second-opinion
description: Second Opinion from Codex and Gemini CLI for Claude Code 
---

# Second Opinion

When invoked:

1. **Summarize the problem** from conversation context (~100 words)

2. **Spawn both subagents in parallel** using Task tool:
   - `gemini-consultant` with the problem summary
   - `codex-consultant` with the problem summary

3. **Present combined results** showing:
   - Gemini's perspective
   - Codex's perspective  
   - Where they agree/differ
   - Recommended approach

## CLI Commands Used by Subagents

```bash
gemini -p "I'm working on a coding problem... [problem]"
codex exec "I'm working on a coding problem... [problem]"
```
```
