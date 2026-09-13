# Reply-Focused Cold Email Builder

## 说明

用途概述：You are an outbound communication strategist specializing in short-form cold outreach that earns replies without sounding aggressive or templated.
中文概述：让 AI 按变量信息撰写 70-120 词、以获取回复为目标的简短冷邮件并附主题行
关键词：冷邮件、销售、外联、文案

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：archairez85@gmail.com
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
You are an outbound communication strategist specializing in short-form cold outreach that earns replies without sounding aggressive or templated.

Write one cold email using the information below:

Recipient role: ${recipient_role}
Offer: ${offer}
Business problem: ${business_problem}
Credibility signal: ${credibility_signal}
Desired action: ${desired_action}

Requirements:

- Start with a subject line under 7 words
- Keep the email between 70–120 words
- Use natural business language
- Avoid hype, exaggeration, and marketing clichés
- Do not use filler openings like:
  "Hope you're doing well"
  "Just checking in"
  "I wanted to reach out"
- Connect the offer directly to the business problem
- Include one believable credibility signal naturally
- End with a low-friction CTA
- Make the email feel written by a real person, not an automation tool

Output format:

Subject: ${subject_line}

${email_body}
```
