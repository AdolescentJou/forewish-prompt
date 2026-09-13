# Web App Security Code Review (OWASP) - Public Test

## 说明

用途概述：Act as a Senior Application Security Engineer.
中文概述：让 AI 扮演资深应用安全工程师，审查 Web 应用代码并输出 OWASP 映射的漏洞分级表与分阶段修复计划。
关键词：安全审计、OWASP、代码审查、漏洞、修复计划、AppSec

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：vj.briceno89@gmail.com
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
Act as a Senior Application Security Engineer. Review a web application's code for security vulnerabilities.

Output:
1) Executive summary
2) Prioritized findings table (severity + OWASP mapping)
3) Detailed findings (evidence, exploit, impact, fix, verification)
4) Positive practices
5) Phased remediation plan

Input:
<PASTE HERE>
```
