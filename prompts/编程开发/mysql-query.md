# Produce MySQL Queries using LLMs

## 说明

用途概述：This prompt tests an LLM's code generation capabilities by prompting it to generate a valid MySQL query by providing information about the database schema.
中文概述：教学示例：给出表结构与查询需求，让 AI 生成对应 MySQL 查询语句
关键词：MySQL、SQL、数据库、查询生成、自然语言转SQL

## 元信息（仓库提供）

- 来源仓库：[dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)
- 贡献者：DAIR.AI
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```markdown
"""
Table departments, columns = [DepartmentId, DepartmentName]
Table students, columns = [DepartmentId, StudentId, StudentName]
Create a MySQL query for all students in the Computer Science Department
"""
```

## 参考链接

- [Prompt Engineering Guide](https://www.promptingguide.ai/introduction/examples#code-generation) (16 March 2023)
