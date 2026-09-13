# Private Group Coaching Infrastructure

## 说明

用途概述：Build a group coaching and cohort management platform called "Cohort OS" — the operating system for running structured group programs.
中文概述：构建团体教练与班期管理平台 "Cohort OS"：项目搭建器、学员门户、作业提交、教练反馈、自动轮转的同伴互评等功能。
关键词：平台开发、团体教练、班期管理、作业系统、产品需求

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@mmanisaligil](https://github.com/mmanisaligil)
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
Build a group coaching and cohort management platform called "Cohort OS" — the operating system for running structured group programs.

Core features:
- Program builder: coach sets program name, session count, cadence (weekly/bi-weekly), max participants, price, and start date. Each session has a title, a pre-work assignment, and a post-session reflection prompt
- Participant portal: each enrolled participant sees their program timeline, upcoming sessions, submitted assignments, and peer reflections in one dashboard
- Assignment submission: participants submit written or link-based assignments before each session. Coach sees all submissions in one view, can leave written feedback per submission
- Peer feedback rounds: after each session, participants are prompted to give one piece of structured feedback to one other participant (rotates automatically so everyone gives and receives equally)
- Progress tracker: coach dashboard showing assignment completion rate per participant, attendance, and a simple engagement score
- Certificate generation: at program completion, auto-generates a PDF certificate with participant name, program name, coach name, and completion date

Stack: React, Supabase, Stripe Connect for coach payouts, Resend for session reminders and feedback prompts. Clean, professional design — coach-first UX.
```
