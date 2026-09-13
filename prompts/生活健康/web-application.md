# Web Application

## 说明

用途概述：--- name: web-application description: Optimize the prompt for an advanced AI web application builder to develop a fully functional ${applicationType:travel booking} web application.
中文概述：AI 扮演 Web 应用构建器，按技术栈/功能/部署/期限步骤开发生产级完整应用（如旅行预订）并上线。
关键词：web application、builder、tech stack、deployment、travel booking

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@SherSingh-EMart](https://github.com/SherSingh-EMart)
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
---
name: web-application
description: Optimize the prompt for an advanced AI web application builder to develop a fully functional ${applicationType:travel booking} web application. The application should be ${environment:production}-ready and deployed as the sole web app for the business.
---

# Web Application 

Describe what this skill does and how the agent should use it.

## Instructions

- Step 1: Select the desired ${technologyStack} technology stack for the application based on the user's preferred hosting space, ${hostingSpace}.
- Step 2: Outline the key features such as ${features:booking system, payment gateway}.
- Step 3: Ensure deployment is suitable for the ${environment:production} environment.
- Step 4: Set a timeline for project completion by ${deadline}.
```
