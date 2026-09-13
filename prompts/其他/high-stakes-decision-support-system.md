# High-Stakes Decision Support System

## 说明

用途概述：Build a high-stakes decision support system called "Pivot" — a structured thinking tool for major life and business decisions.
中文概述：让 AI 构建重大决策支持工具 Pivot，用澄清提问加六个分析框架辅助人生商业决策
关键词：决策支持、结构化思考、分析框架、人生规划、工具构建

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@mmanisaligil](https://github.com/mmanisaligil)
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
Build a high-stakes decision support system called "Pivot" — a structured thinking tool for major life and business decisions.
This is distinct from a simple pros/cons list. The value is in the structured analytical process, not the output document.
Core features:
- Decision intake: user describes the decision (what they're choosing between), their constraints (time, money, relationships, obligations), their stated values (top 3), their current leaning, and their deadline
- Mandatory clarifying questions: [LLM API] generates 5 questions designed to surface hidden assumptions and unstated trade-offs in the user's specific decision. User must answer all 5 before proceeding. The quality of these questions is the quality of the product
- Six analytical frames (each run as a separate API call, shown in tabs):
  (1) Expected value — probability-weighted outcomes under each option  (2) Regret minimization — which option you're least likely to regret at age 80  (3) Values coherence — which option is most consistent with stated values, with specific evidence  (4) Reversibility index — how easily each option can be undone if it's wrong  (5) Second-order effects — what follows from each option in 6 months and 3 years  (6) Advice to a friend — if a trusted friend described this exact situation, what would you tell them?
- Devil's advocate brief: a separate analysis arguing as strongly as possible against the user's current leaning — shown after the 6 frames
- Decision record: stored with all analysis and the final decision made. User updates with actual outcome at 90 days and 1 year

Stack: React, [LLM API] with one carefully crafted prompt per analytical frame, localStorage. Focused, serious design — no gamification, no encouragement. This handles real decisions.
```
