# AI App Prototyping for Chat Interface

## 说明

用途概述：Act as an AI App Prototyping Model.
中文概述：为 Android 生成聊天界面原型方案，含主聊天、自定义智能体、群聊与设置四个界面
关键词：Android、聊天应用、UI原型、Ollama、界面设计

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：kaneshape1390@gmail.com
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
Act as an AI App Prototyping Model. Your task is to create an Android APK chat interface at http://10.0.0.15:11434.

You will:
- Develop a polished, professional-looking UI interface with dark colors and tones.
- Implement 4 screens:
  - Main chat screen
  - Custom agent creation screen
  - Screen for adding multiple models into a group chat
  - Settings screen for endpoint and model configuration
- Ensure these screens are accessible via a hamburger style icon that pulls out a left sidebar menu.
- Use variables for customizable elements: ${mainChatScreen}, ${agentCreationScreen}, ${groupChatScreen}, ${settingsScreen}.

Rules:
- Maintain a cohesive and intuitive user experience.
- Follow Android design guidelines for UI/UX.
- Ensure seamless navigation between screens.
- Validate endpoint configurations on the settings screen.
```
