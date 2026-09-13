# AI Grounding Prompt

## 说明

用途概述：1. Base your answer ONLY on the uploaded documents.
中文概述：让 AI 仅依据上传文档作答，每条结论附文档页码引用，找不到即如实标注不猜测
关键词：RAG、文档问答、引用溯源、事实核查、grounding

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@RoShinAU](https://github.com/RoShinAU)
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
1. Base your answer ONLY on the uploaded documents. Nothing else.
2. If info isn't found, say "Not found." Don't guess.
3. For each claim, cite: [Document, Page/Section, Quote]
4. If uncertain, mark as [Unverified]
5. [Your question]

Re-scan the document. For each claim, give me the exact quote that supports it,  If you can't find a quote, take the claim back.
```
