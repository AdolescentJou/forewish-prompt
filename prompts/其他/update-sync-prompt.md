# Update/Sync Prompt

## 说明

用途概述：You are updating an existing FORME.
中文概述：对照代码库现状更新 FORME.md 文档，差异分析后只给出受影响章节的替换文本
关键词：文档更新、diff分析、代码库、FORME.md、维护

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@gokbeyinac](https://github.com/gokbeyinac)
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
You are updating an existing FORME.md documentation file to reflect
changes in the codebase since it was last written.

## Inputs
- **Current FORGME.md:** ${paste_or_reference_file}
- **Updated codebase:** ${upload_files_or_provide_path}
- **Known changes (if any):** [e.g., "We added Stripe integration and switched from REST to tRPC" — or "I don't know what changed, figure it out"]

## Your Tasks

1. **Diff Analysis:** Compare the documentation against the current code.
   Identify what's new, what changed, and what's been removed.

2. **Impact Assessment:** For each change, determine:
   - Which FORME.md sections are affected
   - Whether the change is cosmetic (file renamed) or structural (new data flow)
   - Whether existing analogies still hold or need updating

3. **Produce Updates:** For each affected section:
   - Write the REPLACEMENT text (not the whole document, just the changed parts)
   - Mark clearly: ${section_name} → [REPLACE FROM "..." TO "..."]
   - Maintain the same tone, analogy system, and style as the original

4. **New Additions:** If there are entirely new systems/features:
   - Write new subsections following the same structure and voice
   - Integrate them into the right location in the document
   - Update the Big Picture section if the overall system description changed

5. **Changelog Entry:** Add a dated entry at the top of the document:
   "### Updated ${date} — [one-line summary of what changed]"

## Rules
- Do NOT rewrite sections that haven't changed
- Do NOT break existing analogies unless the underlying system changed
- If a technology was replaced, update the "crew" analogy (or equivalent)
- Keep the same voice — if the original is casual, stay casual
- Flag anything you're uncertain about: "I noticed [X] but couldn't determine if [Y]"
```
