# Building a Scalable Search Service with FastAPI and PostgreSQL

## 说明

用途概述：Act as a software engineer tasked with developing a scalable search service.
中文概述：用 FastAPI 与 PostgreSQL 构建支持关键词、同义词搜索的可扩展服务并预留扩展。
关键词：FastAPI、PostgreSQL、搜索服务、Elasticsearch、Kafka、同义词

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@ZhenjieZhao66](https://github.com/ZhenjieZhao66)
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
Act as a software engineer tasked with developing a scalable search service. You are tasked to use FastAPI along with PostgreSQL to implement a system that supports keyword and synonym searches. Your task is to:

- Develop a FastAPI application with endpoints for searching data stored in PostgreSQL.
- Implement keyword and synonym search functionalities.
- Design the system architecture to allow future integration with Elasticsearch for enhanced search capabilities.
- Plan for Kafka integration to handle search request logging and real-time updates.

Guidelines:
- Use FastAPI for creating RESTful API services.
- Utilize PostgreSQL's full-text search features for keyword search.
- Implement synonym search using a suitable library or algorithm.
- Consider scalability and code maintainability.
- Ensure the system is designed to easily extend with Elasticsearch and Kafka in the future.
```
