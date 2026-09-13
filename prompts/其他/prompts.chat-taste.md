# prompts.chat taste

## 说明

用途概述：# Taste # github-actions - Use `actions/checkout@v6` and `actions/setup-node@v6` (not v4) in GitHub Actions workflows.
中文概述：以带置信度的 taste 清单输出 prompts.chat 项目编码约定：GitHub Actions 版本、Next.js/Prisma 架构与工具选型。
关键词：taste、项目编码规范、GitHub Actions、Next.js、Prisma

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@f](https://github.com/f)
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：是

## Prompt 内容

```text
# Taste

# github-actions
- Use `actions/checkout@v6` and `actions/setup-node@v6` (not v4) in GitHub Actions workflows. Confidence: 0.65
- Use Node.js version 24 in GitHub Actions workflows (not 20). Confidence: 0.65

# project
- This project is **prompts.chat** — a full-stack social platform for AI prompts (evolved from the "Awesome ChatGPT Prompts" GitHub repo). Confidence: 0.95
- Package manager is npm (not pnpm or yarn). Confidence: 0.95

# architecture
- Use Next.js App Router with React Server Components by default; add `"use client"` only for interactive components. Confidence: 0.95
- Use Prisma ORM with PostgreSQL for all database access via the singleton at `src/lib/db.ts`. Confidence: 0.95
- Use the plugin registry pattern for auth, storage, and media generator integrations. Confidence: 0.90
- Use `revalidateTag()` for cache invalidation after mutations. Confidence: 0.90

# typescript
- Use TypeScript 5 in strict mode throughout the project. Confidence: 0.95

# styling
- Use Tailwind CSS 4 + Radix UI + shadcn/ui for all UI components. Confidence: 0.95
- Use the `cn()` utility for conditional/merged Tailwind class names. Confidence: 0.90

# api
- Validate all API route inputs with Zod schemas. Confidence: 0.95
- There are 61 API routes under `src/app/api/` plus the MCP server at `src/pages/api/mcp.ts`. Confidence: 0.90

# i18n
- Use `useTranslations()` (client) and `getTranslations()` (server) from next-intl for all user-facing strings. Confidence: 0.95
- Support 17 locales with RTL support for Arabic, Hebrew, and Farsi. Confidence: 0.90

# database
- Use soft deletes (`deletedAt` field) on Prompt and Comment models — never hard-delete these records. Confidence: 0.95
```
