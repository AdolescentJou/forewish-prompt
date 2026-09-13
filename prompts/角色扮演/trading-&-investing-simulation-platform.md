# Trading & Investing Simulation Platform

## 说明

用途概述：Build a paper trading simulation platform called "Paper" — a realistic, risk-free environment for learning to trade and invest.
中文概述：AI 构建纸面交易模拟平台 Paper：以 10 万美元虚拟资金实时模拟买卖股票 ETF，产出盈亏面板、强制交易日志与行为分析。
关键词：Paper trading、投资模拟、虚拟资金、绩效面板、交易日志、行为分析

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@mmanisaligil](https://github.com/mmanisaligil)
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
Build a paper trading simulation platform called "Paper" — a realistic, risk-free environment for learning to trade and invest.

Core features:
- Portfolio setup: user starts with $100,000 in virtual cash. Real-time stock and ETF prices via Yahoo Finance or Alpha Vantage API
- Trade execution: market and limit orders supported. Simulate 0.1% slippage on market orders. Commission of $1 per trade (realistic friction without being punitive)
- Performance dashboard: P&L chart (daily), total return, annualized return, win rate, average gain and loss, Sharpe ratio, and current sector exposure — all updated with each trade. Built with recharts
- Trade journal: required field on every position close — "What was my thesis entering this trade? What happened? What will I do differently?" Three fields, each max 200 characters. Cannot close a position without completing the journal
- Behavioral analysis: [LLM API] analyzes the last 20 trade journal entries and identifies recurring behavioral patterns — "You consistently exit winning positions early when they approach round-number price levels" — surfaced monthly
- Leaderboard: optional, weekly-resetting leaderboard among friend groups — ranked by risk-adjusted return, not raw P&L

Stack: React, Yahoo Finance or Alpha Vantage for market data, [LLM API] for behavioral analysis, recharts. Terminal-inspired design — data dense, no decorative elements.
```
