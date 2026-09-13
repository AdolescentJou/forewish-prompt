# Design Brief

## 说明

用途概述：This is a ${page_type:dashboard} of a modern ${focus:government audit} app called ${brand:AuditFlow}.
中文概述：让 AI 分析界面截图并产出面向开发者的设计简报：明暗模式、响应式断点与色板，JSONC 输出
关键词：UI设计、设计交付、design brief、Tailwind、响应式

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：farias.andreluiz@gmail.com
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
This is a ${page_type:dashboard} of a modern ${focus:government audit} app called ${brand:AuditFlow}.

Thoroughly analyze the UI in this screenshot and describe it in as much detail as you can to hand over from a UI designer to a developer. The brief should cover both light and dark mode and contain responsive breakpoints matching Tailwind CSS v4.3 defaults.

Output characteristics as structured JSONC.

For colors, extract a rough palette and only detail accents and complex media. The goal is to use only 2 palettes: primary and secondary similar to Tailwind colors. Alongside these 2, you can define any number of grays and accent colors for more complex UI (gradients, shadows, SVGs, etc.).

End with a prompt explaining how to implement the UI for a developer, but don't mention any tech specs; only a brief of the UI to be implemented and the token rules + usage. Output the prompt as a Markdown code block.

The output should be two code blocks: one for the design brief and one for the JSONC design specification.
```
