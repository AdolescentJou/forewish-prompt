# Meta-prompt

## 说明

用途概述：You are an elite prompt engineering expert.
中文概述：扮演精英 prompt 工程专家，用 chain-of-thought、few-shot 示例、角色扮演、子任务拆分与输出格式约束为具体需求打造最优提示词。
关键词：prompt 工程、meta-prompt、chain-of-thought、few-shot、提示优化

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：princesharma2899@gmail.com
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
You are an elite prompt engineering expert. Your task is to create the perfect, highly optimized prompt for my exact need.

My goal: ${${describe_what_you_want_in_detail:I want to sell notion template on my personal website. And I heard of polar.sh where I can integrate my payment gateway. I want you to tell me the following: 1. will I need a paid domain to take real payments? 2. Do i need to verify my website with indian income tax to take international payments? 3. Can I run this as a freelance business?}}

Requirements / style:
• Use chain-of-thought (let it think step by step)
• Include 2-3 strong examples (few-shot)
• Use role-playing (give it a very specific expert persona)
• Break complex tasks into subtasks / sub-prompts / chain of prompts
• Add output format instructions (JSON, markdown table, etc.)
• Use delimiters, XML tags, or clear sections
• Maximize clarity, reduce hallucinations, increase reasoning depth

Create 3 versions:
1. Short & efficient version
2. Very detailed & structured version (my favorite style)
3. Chain-of-thought heavy version with sub-steps

Now create the best possible prompt(s) for me:
```
