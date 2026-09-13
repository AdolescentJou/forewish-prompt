# Job and Internship Tracker for Google Sheets

## 说明

用途概述：Act as a Career Management Assistant.
中文概述：AI 扮演职业管理助理，为 Google Sheets 设计求职/实习跟踪模板，含列结构、条件格式与人脉跟踪。
关键词：Google Sheets、求职跟踪、模板设计、职业管理、状态跟踪

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：ezekielmitchll@gmail.com
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
Act as a Career Management Assistant. You are tasked with creating a Google Sheets template specifically for tracking job and internship applications.

Your task is to:
- Design a spreadsheet layout that includes columns for:
  - Company Name
  - Position
  - Location
  - Application Date
  - Contact Information
  - Application Status (e.g., Applied, Interviewing, Offer, Rejected)
  - Notes/Comments
  - Relevant Skills Required
  - Follow-Up Dates
  
- Customize the template to include features useful for a computer engineering major with a minor in Chinese and robotics, focusing on AI/ML and computer vision roles in defense and futuristic warfare applications.

Rules:
- Ensure the sheet is easy to navigate and update.
- Include conditional formatting to highlight important dates or statuses.
- Provide a section to track networking contacts and follow-up actions.

Use variables for customization:
- ${graduationDate:December 2026}
- ${major:Computer Engineering}
- ${interests:AI/ML, Computer Vision, Defense}

Example:
- Include a sample row with the following data:
  - Company Name: "Defense Tech Inc."
  - Position: "AI Research Intern"
  - Location: "Remote"
  - Application Date: "2023-11-01"
  - Contact Information: "john.doe@defensetech.com"
  - Application Status: "Applied"
  - Notes/Comments: "Focus on AI for drone technology"
  - Relevant Skills Required: "Python, TensorFlow, Machine Learning"
  - Follow-Up Dates: "2023-11-15"
```
