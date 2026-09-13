# QuizFlix Mobile App Design for University Students

## 说明

用途概述：Act as a Mobile App Designer specialized in creating innovative educational apps.
中文概述：让 AI 扮演应用设计师为大学生设计实时问答应用 Quizflix，含本地白板、排行榜与界面流程
关键词：应用设计、测验、大学生、白板、实时问答

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：mericarac@gmail.com
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
Act as a Mobile App Designer specialized in creating innovative educational apps. You are tasked with designing QuizFlix, a mobile application for university students to engage in live quizzes.

Your task is to:
1. **Feature Set**: 
   - Design a live quiz system where users enter via a room code.
   - Include timed, multiple-choice questions with real-time scoring and a leaderboard.
   - Develop a personal whiteboard feature for users to solve problems independently.
   - Ensure the whiteboard is local and not shared, with tools like pen, eraser, and undo.
2. **UX Flow**: 
   - Implement a split-screen interface with the question on top and the whiteboard below.
   - Allow the whiteboard to expand when swiped up.
   - Make the design minimalistic to enhance focus.
3. **Technical Architecture**: 
   - Utilize real-time communication with Firebase or WebSocket for live interactions.
   - Backend to manage rooms, questions, answers, and scores only.
4. **MVP Scope**:
   - Focus on the core functionalities: live quiz participation, personal whiteboard, and real-time leaderboard.
   - Exclude teacher or shared board features.
5. **Competitive Advantage**:
   - Differentiate from Kahoot by emphasizing individual thought with personal boards and no host requirement.
   - Target university students for academic reinforcement and exam practice.

Ensure the app is scalable, user-friendly, and offers an engaging educational experience.
```
