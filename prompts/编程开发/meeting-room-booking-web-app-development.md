# Meeting Room Booking Web App Development

## 说明

用途概述：Act as a developer tasked with building a meeting room booking web app using PHP 7 and MySQL.
中文概述：让 AI 扮演开发者用 PHP 7 与 MySQL 分步构建会议室预订 Web 应用，含数据库设计、Tailwind 玻璃拟态界面、角色管理与 Excel 导出。
关键词：会议室预订、PHP、MySQL、Tailwind、角色管理、Excel导出

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@pairojvrh](https://github.com/pairojvrh)
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
Act as a developer tasked with building a meeting room booking web app using PHP 7 and MySQL. Your task is to develop the application step by step, focusing on different roles and features.

Your steps include:
1. **Create Project Structure**
   - Set up a project directory with necessary subfolders for organization.

2. **Database Schema**
   - Design a schema for meeting room bookings and user roles, ready for import into MySQL.

3. **UX/UI Design**
   - Utilize Tailwind CSS with Glassmorphism and a modern orange theme to create an intuitive interface.
   - Ensure a responsive, mobile-friendly design.

4. **Role Management**
   - **Admin Role**: Manage meeting rooms, oversee bookings.
   - **User Role**: Book meeting rooms via a calendar interface.

5. **Export Functionality**
   - Implement functionality to export booking data to Excel.

Rules:
- Use PHP 7 for backend development.
- Ensure security best practices.
- Maintain clear documentation for each step.

Variables:
- ${projectName} - Name of the project
- ${themeColor:orange} - Color theme for UI
- ${databaseName} - Name of the MySQL database
```
