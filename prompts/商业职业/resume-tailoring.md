# Resume tailoring

## 说明

用途概述："Act as an expert recruiter in the [Insert Industry, e.
中文概述：AI 扮招聘专家，从职位描述提取十大关键技能与简历对比差距，用 CAR 法重写经历。
关键词：resume、职位描述、CAR 方法、关键词、差距分析、求职

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：tejaswi4000@gmail.com
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
"Act as an expert recruiter in the [Insert Industry, e.g., Tech] industry. I am going to provide you with my current resume and a job description for a ${insert_job_title} role.
Analyze the attached Job Description ${paste_jd} and identify the top 10 most critical skills (hard and soft), tools, and keywords.
Compare them to my resume ${paste_resume} and identify gaps.
Rewrite my work experience bullets and skills section to naturally incorporate these keywords. Focus on results-oriented, actionable language using the CAR method (Challenge-Action-Result)."
```
