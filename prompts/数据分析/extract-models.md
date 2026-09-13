# Extract Model Names from Papers

## 说明

用途概述：The following prompt tests an LLM's capabilities to perform an information extraction task which involves extracting model names from machine learning paper abstracts.
中文概述：LLM 信息抽取测试任务：从机器学习论文摘要提取模型名，以 ["model_name"] 数组输出，找不到则返回 ["NA"]。
关键词：信息抽取、LLM、模型名、extraction、论文摘要

## 元信息（仓库提供）

- 来源仓库：[dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)
- 贡献者：DAIR.AI
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```markdown
Your task is to extract model names from machine learning paper abstracts. Your response is an array of the model names in the format [\"model_name\"]. If you don't find model names in the abstract or you are not sure, return [\"NA\"]

Abstract: Large Language Models (LLMs), such as ChatGPT and GPT-4, have revolutionized natural language processing research and demonstrated potential in Artificial General Intelligence (AGI). However, the expensive training and deployment of LLMs present challenges to transparent and open academic research. To address these issues, this project open-sources the Chinese LLaMA and Alpaca…
```

## 参考链接

- [Prompt Engineering Guide](https://www.promptingguide.ai/introduction/examples#information-extraction) (16 March 2023)
