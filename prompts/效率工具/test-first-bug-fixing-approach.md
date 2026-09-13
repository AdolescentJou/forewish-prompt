# Test-First Bug Fixing Approach

## 说明

用途概述：I have a bug: ${bug}.
中文概述：AI 采用 test-first 流程修 bug：先读源码与现有测试、写复现失败的测试，再做最小修复直至全套测试通过，并排查同类问题路径。
关键词：TDD、bug 修复、测试先行、最小修复

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@ilkerulusoy](https://github.com/ilkerulusoy)
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
I have a bug: ${bug}. Take a test-first approach: 1) Read the relevant source files and existing tests. 2) Write a failing test that reproduces the exact bug. 3) Run the test suite to confirm it fails. 4) Implement the minimal fix. 5) Re-run the full test suite. 6) If any test fails, analyze the failure, adjust the code, and re-run—repeat until ALL tests pass. 7) Then grep the codebase for related code paths that might have the same issue and add tests for those too. 8) Summarize every change made and why. Do not ask me questions—make reasonable assumptions and document them.
```
