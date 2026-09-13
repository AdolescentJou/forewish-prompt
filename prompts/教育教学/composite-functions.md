# Evaluating Composite Functions

## 说明

用途概述：This prompt tests an LLM's mathematical capabilities by prompting it to evaluate a given composition function.
中文概述：数学推理题：已知反函数 f⁻¹ 的若干取值，求复合函数 f(f(f(6))) 的值，用于检验 LLM 数学能力
关键词：数学推理、Composite Function、反函数、LLM 评测

## 元信息（仓库提供）

- 来源仓库：[dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)
- 贡献者：DAIR.AI
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
Suppose $$g(x) = f^{-1}(x), g(0) = 5, g(4) = 7, g(3) = 2, g(7) = 9, g(9) = 6$$ what is $$f(f(f(6)))$$?
```

## 参考链接

- [Sparks of Artificial General Intelligence: Early experiments with GPT-4](https://arxiv.org/abs/2303.12712) (13 April 2023)
