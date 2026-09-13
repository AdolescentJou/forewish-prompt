# Default Meeting Summary

## 说明

用途概述：You are a helpful assistant.
中文概述：AI 把会议记录总结为 1-2 段并列出含责任人的行动项，按指定语言输出。
关键词：会议总结、meeting summary、行动项、action items、多语言

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：elmehdibenyoussef@gmail.com
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
You are a helpful assistant. The following is a meeting transcript. Please: 

1. Summarize the meeting in 1–2 paragraphs. 
2. List clear and concise action items (include who is responsible if available). 

Return format: 
Summary: <summary> 
Action Items: 
- [ ] item 1 
- [ ] item 2

Make sure the summary is in ${language}

=======Transcript=======

==========================
```
