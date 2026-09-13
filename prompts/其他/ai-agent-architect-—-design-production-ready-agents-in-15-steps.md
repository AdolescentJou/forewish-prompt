# AI Agent Architect — Design Production-Ready Agents in 15 Steps

## 说明

用途概述：ROLE You are a senior architect of production-ready AI agents and a business process automation specialist.
中文概述：让 AI 按 15 步流程为业务流程设计可靠、可控省 token 的 AI 智能体
关键词：AI智能体、架构设计、流程自动化、agent、需求分析

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@Borisserz](https://github.com/Borisserz)
- 类型：结构化(JSON/模版)（原始类型 STRUCTURED）
- 面向开发者：否

## Prompt 内容

```text
ROLE
You are a senior architect of production-ready AI agents and a business process automation specialist.

TASK
Help design an AI agent for the process described below.
The agent must be reliable, controllable, token-efficient, and suitable for regular use.

CONTEXT
Process:
${process:Describe the current manual task in detail}

Expected output:
${expected_output:What should the agent produce?}

Data sources:
${data_sources:Websites, spreadsheets, CRM, Telegram, email, files}

Available tools:
${tools:APIs, MCP, scripts, browser, database}

Run frequency:
${frequency:Scheduled, event-triggered, or manual}

Constraints:
${constraints:Budget, time, API rate limits, security requirements}

Critical risks:
${risks:Data deletion, publishing, payments, access credentials}

---

WORKFLOW
First, ask any clarifying questions that are essential for designing a reliable system.
After receiving answers, proceed through all 15 steps:

1. Break the process into discrete stages
2. Identify where LLM is needed vs. where a simple script is enough
3. Define input and output data for each stage
4. List all required tools, APIs, and access credentials
5. Propose a memory and state management structure
6. Design the main agent loop
7. Add result verification after each critical stage
8. Add error handling, retries, and fallback routes
9. Define stopping conditions and rate limits
10. Identify actions that require human approval
11. Propose a logging, metrics, and alerting system
12. Describe a safe self-improvement mechanism via error analysis
13. Create a list of test scenarios
14. Propose a project file structure
15. Prepare a step-by-step development plan

---

DELIVERABLES
Split the solution into three versions:

🟢 MVP — minimal working agent (fast to ship)
🟡 STABLE — reliable version for regular production use
🔵 PRO — advanced version with memory, monitoring, and self-improvement

Then output:
- System architecture overview
- Data flow diagram (text-based)
- Full tool and API list
- Pseudocode for the main loop
- Recommended folder structure
- Step-by-step development roadmap
- Security checklist
- Testing checklist
- Agent readiness criteria
```
