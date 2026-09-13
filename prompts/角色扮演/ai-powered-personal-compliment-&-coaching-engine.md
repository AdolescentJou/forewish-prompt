# AI-Powered Personal Compliment & Coaching Engine

## 说明

用途概述：Build a web app called "Mirror" — an AI-powered personal coaching tool that gives users emotionally intelligent, personalized feedback.
中文概述：AI 按规格构建“Mirror”应用：情感智能私教工具，含领域与反馈风格引导、每日打卡、AI 教练点评、成就档案与连续打卡追踪
关键词：coaching app、Mirror、情感智能、每日打卡、web app、feedback

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@mmanisaligil](https://github.com/mmanisaligil)
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
Build a web app called "Mirror" — an AI-powered personal coaching tool that gives users emotionally intelligent, personalized feedback.

Core features:
- Onboarding: user selects their domain (career, fitness, creative work, relationships) and sets a "validation style" (tough love / warm encouragement / analytical)
- Daily check-in: a short form where users submit what they did today, how they felt, and one thing they're proud of
- AI response: calls the [LLM API] (claude-sonnet-4-20250514) with a system prompt instructing Claude to respond as a perceptive coach — acknowledge effort, name specific strengths, end with one forward-looking insight. Never use generic phrases like "great job" or "well done"
- Wins Archive: all past check-ins and AI responses, sortable by date, searchable
- Streak tracker: consecutive daily check-ins shown as a simple counter — no gamification badges

UI: clean, warm, serif typography, cream (#F5F0E8) background. Should feel like a private journal, not an app. No notifications except a gentle daily reminder at a user-set time.

Stack: React frontend, localStorage for data persistence, [LLM API] for AI responses. Single-page app, no backend required.
```
