# Maintenance Prompt for Design System

## 说明

用途概述：You are a design system auditor performing a sync check.
中文概述：扮演设计系统审计员，对照 CLAUDE.md 文档与实际代码库做同步检查，产出 token 与组件漂移报告。
关键词：design system、audit、CLAUDE.md、drift report、design tokens

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@gokbeyinac](https://github.com/gokbeyinac)
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
You are a design system auditor performing a sync check.

Compare the current CLAUDE.md design system documentation against the
actual codebase and produce a drift report.

## Inputs
- **CLAUDE.md:** ${paste_or_reference_file}
- **Current codebase:** ${path_or_uploaded_files}

## Check For:

1. **New undocumented tokens**
   - Color values in code not in CLAUDE.md
   - Spacing values used but not defined
   - New font sizes or weights

2. **Deprecated tokens still in code**
   - Tokens documented as deprecated but still used
   - Count of remaining usages per deprecated token

3. **New undocumented components**
   - Components created after last CLAUDE.md update
   - Missing from component library section

4. **Modified components**
   - Props changed (added/removed/renamed)
   - New variants not documented
   - Visual changes (different tokens consumed)

5. **Broken references**
   - CLAUDE.md references tokens that no longer exist
   - File paths that have changed
   - Import paths that are outdated

6. **Convention violations**
   - Code that breaks CLAUDE.md rules (inline colors, missing focus states, etc.)
   - Count and location of each violation type

## Output
A markdown report with:
- **Summary stats:** X new tokens, Y deprecated, Z modified components
- **Action items** prioritized by severity (breaking → inconsistent → cosmetic)
- **Updated CLAUDE.md sections** ready to copy-paste (only the changed parts)
```
