# TCRE Framework - AI Prompt Engineer

## 说明

用途概述：I want to create a highly effective AI prompt using the TCRE framework (Task, Context, References, Evaluate/Iterate).
中文概述：让 AI 按 TCRE 框架逐步提问收集要素后生成、评估并改进一个高效提示词
关键词：Prompt工程、TCRE、结构化提问、评估迭代、5Whys

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@kenicodes](https://github.com/kenicodes)
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
I want to create a highly effective AI prompt using the TCRE framework (Task, Context, References, Evaluate/Iterate). My goal is to **${insert_objective}.

Step 1: Ask me multiple structured, specific questions—one at a time—to gather all essential input for each TCRE component, also using the 5 Whys technique when helpful to uncover deeper context and intent.

Step 2: Once you’ve gathered enough information, generate the best version of the final prompt.

Step 3: Evaluate the prompt using the TCRE framework, briefly explaining how it satisfies each element.

Step 4: Suggest specific, actionable improvements to enhance clarity, completeness, or impact.

If anything is unclear or you need more context or examples, please ask follow-up questions before proceeding. You may apply best practices from prompt engineering where helpful.
```
