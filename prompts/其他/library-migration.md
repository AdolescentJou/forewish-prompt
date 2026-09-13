# library migration

## 说明

用途概述：🔴 1. Data Access & Connection Management These are critical because they affect performance, scalability, and outages.
中文概述：Java 库迁移建议清单：Redis 客户端用 Lettuce/Valkey Glide，连接池选 HikariCP，ORM 用 Hibernate 6+/Spring Data JPA。
关键词：Java、库迁移、Redis/Lettuce、HikariCP、Hibernate

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：abhinavme1004@gmail.com
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
🔴 1. Data Access & Connection Management
These are critical because they affect performance, scalability, and outages.

🔹 Redis
❌ Jedis (older pattern, topology issues)

✅ Lettuce (reactive, auto-reconnect)

✅ Valkey Glide (AWS recommended)

🔹 JDBC Connection Pool
❌ Apache DBCP

❌ C3P0

✅ HikariCP (default in Spring Boot, fastest, stable)

 

🔹 ORM / Persistence
❌ Old Hibernate 4.x

❌ MyBatis legacy configs

✅ Hibernate 6+

✅ Spring Data JPA latest
```
