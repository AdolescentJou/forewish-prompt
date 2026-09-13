# SEO diagnosis

## 说明

用途概述：${instruction} Based on the homepage HTML source code I provide, perform a quick diagnostic for a B2B manufacturing client targeting overseas markets.
中文概述：AI 基于首页 HTML 源码对面向海外市场的 B2B 制造网站做 200 词内快速 SEO 诊断，指出技术栈与关键问题。
关键词：SEO诊断、HTML源码、B2B网站、海外SEO、技术栈

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@Bornduck](https://github.com/Bornduck)
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
${instruction}
Based on the homepage HTML source code I provide, perform a quick diagnostic for a B2B manufacturing client targeting overseas markets. Output must be under 200 words.

1️⃣ Tech Stack Snapshot:
- Identify backend language (e.g., PHP, ASP), frontend libraries (e.g., jQuery version), CMS/framework clues, and analytics tools (e.g., GA, Okki).
- Flag 1 clearly outdated or risky component (e.g., jQuery 1.x, deprecated UA tracking).

2️⃣ SEO Critical Issues:
- Highlight max 3 high-impact problems visible in the source (e.g., missing viewport, empty meta description, content hidden in HTML comments, non-responsive layout).
- For each, briefly state the business impact on overseas organic traffic or conversions.

✅ Output Format:
• 1 sentence acknowledging a strength (if any)
• 3 bullet points: ${issue} → [Impact on global SEO/UX]
• 1 low-pressure closing line (e.g., "Happy to share a full audit if helpful.")

Tone: Professional, constructive, no sales pressure. Assume the client is a Chinese manufacturer expanding globally.
```
