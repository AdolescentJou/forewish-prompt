# Comprehensive POS Application Development with FIFO and Reporting

## 说明

用途概述：--- name: comprehensive-pos-application-development-with-fifo-and-reporting description: Develop a full-featured Point of Sales (POS) application integrating in
中文概述：让 AI 扮演软件开发工程师，生成含库存管理与 FIFO 成本核算及日报表的收银 POS 应用
关键词：POS、FIFO、库存管理、销售报表、收银系统

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@lalsproject](https://github.com/lalsproject)
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
---
name: comprehensive-pos-application-development-with-fifo-and-reporting
description: Develop a full-featured Point of Sales (POS) application integrating inventory management, FIFO costing, and daily sales reporting.
---

# Comprehensive POS Application Development with FIFO and Reporting

Act as a Software Developer. You are tasked with creating a comprehensive Point of Sales (POS) application with integrated daily sales reporting functionality.

Your task is to develop:
- **Core POS Features:**
  - Product inventory management with buy price and sell price tracking
  - Sales transaction processing
  - Real-time inventory updates
  - User-friendly interface for cashiers

- **FIFO Implementation:**
  - Implement First-In-First-Out inventory management
  - Track product batches with purchase dates
  - Automatically sell oldest stock first
  - Maintain accurate cost calculations based on FIFO methodology

- **Daily Sales Report Features:**
  - Generate comprehensive daily sales reports including:
    - Total daily sales revenue
    - Total daily profit (calculated as: sell price - buy price using FIFO costing)
    - Number of transactions
    - Best-selling products
    - Inventory levels after sales

**Technical Specifications:**
- Use a modern programming language (${language:next js})
- Include a database design for storing products, transactions, and inventory batches
- Implement proper error handling and data validation
- Create a clean, intuitive user interface
- Include sample data for demonstration

**Deliverables:**
1. Complete source code with comments
2. Database schema/structure
3. Installation and setup instructions
4. Sample screenshots or demo of key features
5. Brief documentation explaining the FIFO implementation

Ensure the application is production-ready with proper data persistence and can handle multiple daily transactions efficiently.
```
