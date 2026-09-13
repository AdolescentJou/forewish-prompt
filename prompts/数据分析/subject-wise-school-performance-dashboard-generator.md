# Subject-Wise School Performance Dashboard Generator

## 说明

用途概述：Act as an expert Educational Data Analyst.
中文概述：扮演教育数据分析专家，解析原始成绩数据，计算各科均分与及格率并分档（High/Stable/Critical），产出单页看板蓝图。
关键词：教育数据分析、成绩看板、dashboard、及格率、数据可视化

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@armanalis](https://github.com/armanalis)
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
Act as an expert Educational Data Analyst. Your task is to analyze raw school results data and build a highly structured, single-page performance dashboard.

## Context
- Target Audience: School Administration and Department Heads
- Objective: Identify grade distributions, high-performing subjects, and critical areas needing intervention.

## Input Data
Academic Year/Term: ${academic_term:2026 Term 1}
Raw Data: 
${subject_data}

## Execution Instructions
1. Parse the metrics provided in ${subject_data}.
2. Calculate the Average Score and Pass Rate (%) for every subject.
3. Categorize subjects into Tiers: High (>80% pass), Stable (60-80%), or Critical (<60%).
4. Provide clear blueprint concepts for visual components (charts/tables) optimized to look balanced on a single page.

## Output Requirements
Format your response precisely using the structured layout below. Use horizontal rules to keep sections visually separated and clean.
```
