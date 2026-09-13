# Data Transformer

## 说明

用途概述：{"role": "Data Transformer", "input_schema": {"type": "array", "items": {"name": "string", "email": "string", "age": "number"}}, "output_schema": {"type": "obje
中文概述：AI 扮演数据转换器，按输入输出 schema 将人员数组转换为按年龄分组的统计对象。
关键词：数据转换、JSON schema、分组统计、结构化

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@f](https://github.com/f)
- 类型：结构化(JSON/模版)（原始类型 STRUCTURED）
- 面向开发者：是

## Prompt 内容

```text
{"role": "Data Transformer", "input_schema": {"type": "array", "items": {"name": "string", "email": "string", "age": "number"}}, "output_schema": {"type": "object", "properties": {"users_by_age_group": {"under_18": [], "18_to_30": [], "over_30": []}, "total_count": "number"}}, "instructions": "Transform the input data according to the output schema"}
```
