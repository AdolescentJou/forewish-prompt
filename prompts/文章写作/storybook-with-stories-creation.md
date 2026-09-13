# Storybook with stories creation

## 说明

用途概述：Act you as a storybook professional: prompt for creating a storybook with basic stories in a modular way, with professional folder structure based on given scre
中文概述：AI 扮演 storybook 专家，按截图用 scss/tsx 模块化搭建带 stories 的专业目录结构组件库。
关键词：Storybook、组件库、scss、tsx、模块化目录

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：venoogopal@gmail.com
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
Act you as a storybook professional: prompt for creating a storybook with basic stories in a modular way, with professional folder structure based on given screenshot, use scss for styling and tsx for scripting in below structure.

src

│

├── foundations

│   ├── colors

│   ├── typography

│   ├── spacing

│   ├── shadows

│   └── breakpoints

│

├── components

│   ├── Button

│   ├── Input

│   ├── Select

│   ├── Checkbox

│   ├── Radio

│   ├── Modal

│   ├── Card

│   └── Tooltip

│

├── patterns

│   ├── Header

│   ├── Sidebar

│   ├── SearchBar

│   └── Navigation

│

├── tokens

│

├── styles

│

└── index.ts
```
