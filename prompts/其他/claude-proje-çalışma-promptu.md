# Claude - Proje çalışma promptu

## 说明

用途概述：Plan a redesign for this web page before making any edits.
中文概述：让 AI 先审计网页并产出改版设计方案，再按步骤实施
关键词：网页改版、UI/UX、设计系统、改版计划、前端

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：hakanak54@gmail.com
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：是

## Prompt 内容

```text
Plan a redesign for this web page before making any edits.

Goal:
Improve visual hierarchy, clarity, trust, and conversion
while keeping the current tech stack.

Your process:
1. Inspect the existing codebase, components, styles, tokens, and layout primitives.
2. Identify UX/UI issues in the current implementation.
3. Ask clarifying questions if brand/style/conversion intent is unclear.
4. Produce a design-first implementation plan in markdown.

Include:
- Current-state audit
- Main usability and visual design issues
- Proposed information architecture
- Section-by-section page plan
- Component inventory
- Reuse vs extend vs create decisions
- Design token changes needed
- Responsive behavior notes
- Accessibility considerations
- Step-by-step implementation order
- Risks and open questions

Constraints:
- Reuse existing components where possible
- Keep design system consistency
- Do not implement yet
```
