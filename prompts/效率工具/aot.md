# Atom-of-Thought (AoT) Prompting

## 说明

Atom-of-Thought (AoT) Prompting
中文概述：Atom-of-Thought 策略：把问题分解为最小独立原子子问题逐一解决后综合成最终答案。
关键词：AoT、原子分解、分步推理、综合答案

## 元信息（仓库提供）

- 来源仓库：[danielmiessler/Fabric]
- 原始名称：aot
- 类型：技巧
- 面向开发者：是

## Prompt 内容

```text
# Atom-of-Thought (AoT) Prompting

## Strategy

To solve this problem, break it down into the smallest independent 'atomic' sub-problems. For each atomic sub-problem: 1. Label it as 'Atom X: [brief description]' 2. Solve that specific subproblem completely 3. Make sure each atom can be solved independently. After solving all atomic sub-problems, provide a synthesis that combines them into a final answer. Return the final answer in the required format.
```
