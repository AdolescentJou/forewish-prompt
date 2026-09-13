# TGscrape

## 说明

用途概述：Input Data: [PASTE RAW TELEGRAM EXPORTS, THREADS, OR CHAT LOGS HERE]Analysis Objectives:Event Extraction: What exactly happened?
中文概述：对粘贴的 Telegram 导出日志做情报分析：事件提取、影响评估、KIG 情报缺口与分级行动清单
关键词：Telegram、OSINT、情报分析、事件提取、行动清单

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：kennynah85@gmail.com
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
Input Data: [PASTE RAW TELEGRAM EXPORTS, THREADS, OR CHAT LOGS HERE]Analysis Objectives:Event Extraction: What exactly happened? (Who, what, when, where, and why).Impact Assessment: What is the immediate or potential consequence of this information?Actionability: What should be done about this? Identify concrete next steps or decisions required.Output Structure:Format your response exactly as follows using Markdown:🚨 Executive SummaryProvide a 2-3 sentence summary of the critical events and current operational state based on the feeds.🔑 Key Intelligence Gaps (KIG)What critical information is currently missing that prevents a complete assessment?📋 Actionable Tasks & DirectivesList concrete, prioritized tasks for the team/user to execute based on this intel.Priority 1: ${task} - [Rationale/Risk of inaction]Priority 2: ${task} - [Rationale/Risk of inaction]🌍 Geopolitical / Market Context (If Applicable)Briefly explain the broader context, sentiment shifts, or emerging trends.Narrative 1: ${detail}Narrative 2: ${detail}
```
