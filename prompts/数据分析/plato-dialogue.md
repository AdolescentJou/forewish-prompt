# Evaluate Plato's Dialogue

## 说明

用途概述：The following prompt tests an LLM's ability to perform evaluation on the outputs of two different models as if it was a teacher. First, two models (e.g., ChatGPT & GPT-4) are prompted to using the following prompt: ``` Plato’s Gorgias is a critique of rhetoric and sophistic oratory, where he makes the point that not only is it not a proper form of art, but the use of rhetoric and oratory can often be harmful and malicious. Can you write a dialogue by Plato where instead he criticizes the use of autoregressive language models? ``` Then, those outputs are evaluated using the evaluation prompt below.
中文概述：教学示例：让 AI 以教师视角对比两个大模型对同一问题的输出，辅助评估回答质量
关键词：模型对比、输出评估、教师视角、prompt教学、LLM评测

## 元信息（仓库提供）

- 来源仓库：[dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)
- 贡献者：DAIR.AI
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```
Can you compare the two outputs below as if you were a teacher?

Output from ChatGPT: {output 1}

Output from GPT-4: {output 2}
```

## 参考链接

- [Sparks of Artificial General Intelligence: Early experiments with GPT-4](https://arxiv.org/abs/2303.12712) (13 April 2023)
