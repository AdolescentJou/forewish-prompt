# de

## 说明

用途概述：Analyze the uploaded project report: ${"D:\de\Document from jd.
中文概述：让 AI 分析项目报告与现有原型，生成提示词以指导重做移动应用的完整专业原型
关键词：原型设计、移动应用、提示词生成、UI 重设计、Claude

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：jd5293214@gmail.com
- 类型：结构化(JSON/模版)（原始类型 STRUCTURED）
- 面向开发者：否

## Prompt 内容

```text
Analyze the uploaded project report: ${"D:\de\Document from jd.pdf"}

Analyze the existing prototype: ${"D:\de\canvas"}

Use the additional project documents: ${"D:\de\Document from jd"}

Redesign the complete prototype based on these documents.



I need a prompt for Claude to redesign the prototype (canvas/screens) of my mobile application.

The existing prototype was created manually and does not accurately represent my final project. I want to create a completely new, professional, modern, and logical prototype based on my actual application.

My project resources:

- Google Drive (Project Report, Canvas, Documents, APK, etc.): https://drive.google.com/drive/folders/1pYP_QEiu2Wd7KucZYoOcJWQ07qnCCgn_
- GitHub Repository (Complete Source Code): https://github.com/kadarkadikadey/CITIZEN-107

Generate a detailed Claude prompt that instructs Claude to:

1. Analyze my GitHub repository to understand the complete application.
2. Use the project report and other documents from Google Drive for additional context.
3. Ignore the existing manual prototype and redesign it from scratch according to the actual implemented features.
4. Create a user flow that matches the real application.
5. Design every screen required in the application, including authentication, dashboard, emergency features, help directory, medical resources, profile, settings, and any other necessary screens found in the project.
6. Ensure the navigation flow is logical, clean, and user-friendly.
7. Use modern Material Design UI principles with a professional color scheme and consistent components.
8. Include all user interactions, screen transitions, buttons, forms, dialogs, and navigation between screens.
9. Generate a complete prototype/canvas that can be directly recreated in design tools like Figma or Canva.
10. Do not assume features that are not present in the project. Base every screen and flow only on the actual implementation in the GitHub repository and project documents.

The final output should be a comprehensive prototype redesign prompt that I can directly use in Claude to generate an accurate application prototype.
```
