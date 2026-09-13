# Analyze Incident

## 说明

Efficiently extract and organize key details from cybersecurity breach articles, focusing on attack type, vulnerable components, attacker and target info, incident details, and remediation steps.
中文概述：让 AI 从网络安全入侵报道中提取攻击类型、被攻组件、攻击者与补救措施等关键信息
关键词：网络安全、事件分析、信息提取、威胁情报

## 元信息（仓库提供）

- 来源仓库：[danielmiessler/Fabric]
- 原始名称：analyze_incident
- 类型：prompt
- 面向开发者：是

## Prompt 内容

```text
Cybersecurity Hack Article Analysis: Efficient Data Extraction

Objective: To swiftly and effectively gather essential information from articles about cybersecurity breaches, prioritizing conciseness and order.

Instructions:
For each article, extract the specified information below, presenting it in an organized and succinct format. Ensure to directly utilize the article's content without making inferential conclusions.

- Attack Date: YYYY-MM-DD
- Summary: A concise overview in one sentence.
- Key Details:
    - Attack Type: Main method used (e.g., "Ransomware").
    - Vulnerable Component: The exploited element (e.g., "Email system").
    - Attacker Information: 
        - Name/Organization: When available (e.g., "APT28").
        - Country of Origin: If identified (e.g., "China").
    - Target Information:
        - Name: The targeted entity.
        - Country: Location of impact (e.g., "USA").
        - Size: Entity size (e.g., "Large enterprise").
        - Industry: Affected sector (e.g., "Healthcare").
    - Incident Details:
        - CVE's: Identified CVEs (e.g., CVE-XXX, CVE-XXX).
        - Accounts Compromised: Quantity (e.g., "5000").
        - Business Impact: Brief description (e.g., "Operational disruption").
        - Impact Explanation: In one sentence.
        - Root Cause: Principal reason (e.g., "Unpatched software").
- Analysis & Recommendations:
    - MITRE ATT&CK Analysis: Applicable tactics/techniques (e.g., "T1566, T1486").
    - Atomic Red Team Atomics: Recommended tests (e.g., "T1566.001").
    - Remediation:
        - Recommendation: Summary of action (e.g., "Implement MFA").
        - Action Plan: Stepwise approach (e.g., "1. Update software, 2. Train staff").
    - Lessons Learned: Brief insights gained that could prevent future incidents.
```
