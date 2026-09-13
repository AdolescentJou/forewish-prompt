# Clean BibTeX Formatter for Academic Projects

## 说明

用途概述：I am preparing a BibTeX file for an academic project.
中文概述：将参考文献转为统一、合规的BibTeX条目，规范citation key与作者名，并包含doi、url等字段。
关键词：BibTeX、参考文献、citation、学术写作、格式化

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@recep](https://github.com/recep)
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
I am preparing a BibTeX file for an academic project.
Please convert the following references into a single, consistent BibTeX format with these rules:
Use a single citation key format: firstauthorlastname + year (e.g., esteva2017)
Use @article for journal papers and @misc for web tools or demos
Include at least the following fields: title, author, journal (if applicable), year
Additionally, include doi, url, and a short abstract if available
Ensure author names follow BibTeX standards (Last name, First name)
Avoid Turkish characters, uppercase letters, or long citation keys
Output only valid BibTeX entries.
```
