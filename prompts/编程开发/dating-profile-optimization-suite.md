# Dating Profile Optimization Suite

## 说明

用途概述：Build a web app called "First Impression" — a dating profile audit and optimization tool.
中文概述：让 AI 构建交友资料审计优化 Web 应用，含照片评分、简历重写、开场白生成与评分仪表盘。
关键词：交友资料、Web 应用、照片评分、文案重写、评分看板

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@mmanisaligil](https://github.com/mmanisaligil)
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
Build a web app called "First Impression" — a dating profile audit and optimization tool.

Core features:
- Photo audit: user describes their photos (up to 6) — AI scores each on energy, approachability, social proof, and uniqueness. Returns a ranked order recommendation with one-line reasoning per photo
- Bio rewriter: user pastes current bio, clicks "Optimize", receives 3 rewritten versions in distinct tones (playful / authentic / direct). Each version includes a word count and a predicted "swipe right rate" label (Low / Medium / High)
- Icebreaker generator: user describes a match's profile in a few sentences — AI generates 5 personalized openers ranked by predicted response rate, each with a one-line explanation of why it works
- Profile score dashboard: a 0–100 composite score across bio quality, photo strength, and opener effectiveness — updates live
- Export: formatted PDF of all assets titled "My Profile Package"

Stack: React, [LLM API] for all AI calls, jsPDF for export. Mobile-first UI with a card-based layout — warm colors, modern dating app feel.
```
