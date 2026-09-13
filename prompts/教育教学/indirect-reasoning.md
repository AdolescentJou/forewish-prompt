# Indirect Reasoning with LLMs

## 说明

用途概述：[Zhang et al. (2024)](https://arxiv.org/abs/2402.03667) recently proposed an indirect reasoning method to strengthen the reasoning power of LLMs. It employs the logic of contrapositives and contradictions to tackle IR tasks such as factual reasoning and mathematic proof. It consists of two key steps: 1) enhance the comprehensibility of LLMs by augmenting data and rules (i.e., logical equivalence of contrapositive), and 2) design prompt templates to stimulate LLMs to implement indirect reasoning based on proof by contradiction. Experiments on LLMs like GPT-3.5-turbo and Gemini-pro show that the proposed method enhances the overall accuracy of factual reasoning by 27.33% and mathematic proof by 31.43% compared to traditional direct reasoning methods. Below is an example of zero-shot template for proof-by-contradiction.
中文概述：分步模板引导 LLM 用逆否命题与矛盾逻辑做间接推理(indirect reasoning)，用于数学证明等任务
关键词：间接推理、Indirect Reasoning、逆否命题、数学证明、LLM

## 元信息（仓库提供）

- 来源仓库：[dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)
- 贡献者：DAIR.AI
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```
If a+|a|=0, try to prove that a<0.

Step 1: List the conditions and questions in the original proposition.

Step 2: Merge the conditions listed in Step 1 into one. Define it as wj.

Step 3: Let us think it step by step. Please consider all possibilities. If the intersection between wj (defined in Step 2) and the negation of the question is not empty at least in one possibility, the original proposition is false. Otherwise, the original proposition is true.

Answer:
```

## 参考链接

- [Large Language Models as an Indirect Reasoner: Contrapositive and Contradiction for Automated Reasoning](https://arxiv.org/abs/2402.03667) (06 February 2024)
