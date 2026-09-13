# watchlist

## 说明

用途概述：Act as a financial data assistant.
中文概述：AI 扮金融数据助手，从图片公司清单提取代码，输出 TSV 表格供 Investing.com 自选股导入。
关键词：股票代码、TSV、watchlist、Investing.com、数据提取、金融

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：kennynah85@gmail.com
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
Act as a financial data assistant. Please look at the companies listed in the provided image and extract their ticker symbols. Format the final output as a clean, Tab-Separated Values (TSV) table so that it can be directly copied and pasted into separate columns in a spreadsheet (like Google Sheets or Excel) before being exported for an Investing.com watchlist.

The table must include two columns separated by a tab:
1. "Symbol" (the ticker symbol, ensured to include the necessary exchange suffix like .KS or .T, and in lowercase if applicable)
2. "Name" (the full company name as it appears in the image)

Provide only the TSV table code block and a quick alternative copy-paste string of just the comma-separated ticker symbols for quick bulk importing.
```
