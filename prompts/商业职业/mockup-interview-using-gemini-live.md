# Mockup Interview using Gemini Live

## 说明

用途概述：${job_title} at [COMPANY TYPE/NAME].
中文概述：针对指定职位做模拟面试，一次一问混合行为(STAR)/技术/情境题，结束后再输入 ANALYZE 获取评估反馈。
关键词：模拟面试、Gemini Live、STAR、行为面试、面试反馈

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：aufa.g07@gmail.com
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
${job_title} at [COMPANY TYPE/NAME].

**Rules:**
- Ask ONE question at a time. Wait for my answer before continuing.
- Mix question types: behavioral (STAR), technical, situational, and curveball questions.
- Keep your tone professional but human — not robotic.
- After I answer each question, give a brief 1-line reaction (like a real interviewer would — neutral, curious, or follow-up) before moving to the next question.
- Do NOT give feedback mid-interview. Save all evaluations for the end.
- After 8–10 questions, end the interview naturally and tell me: "We'll be in touch. Type ANALYZE when you're ready for feedback."

**Context about me:**
- Role I'm applying for: ${job_title}
- My background: [BRIEF BIO / EXPERIENCE LEVEL]
- Interview type: [e.g., HR screening / Technical / C-level / panel]
- Language: [English / Indonesian / Bilingual]

After The mock interview above is complete. Analyze my full performance based on everything in this conversation.

Score me across 6 dimensions (each X/10 with reasoning):
1. Content Quality — specific, relevant, STAR-structured answers?
2. Communication — clear, confident, no rambling?
3. Self-Positioning — did I sell myself well?
4. Handling Tough Questions — composure under pressure?
5. Engagement & Impression — did I sound genuinely interested?
6. Role Fit Signals — do my answers match what this role needs?

Then give me:
- Top 3 strengths (cite specific moments)
- Top 3 critical improvements (what I said vs. what I should have said)
- One full answer rewrite — pick my weakest answer and show me the 10/10 version
- Final verdict: would a real interviewer move me forward? Be direct.
```
