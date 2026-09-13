# Academic Paper Figure Generator - Nano Banana Pro

## 说明

用途概述：Create a professional academic figure for scientific publication using the following guidelines: ${figure_type:Type of figure (architecture diagram, flowchart,
中文概述：按类型、主题、风格等变量生成符合学术期刊规范的论文配图，要求清晰、对比度高并支持指定分辨率。
关键词：论文配图、academic figure、科学可视化、图像生成、期刊规范

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@AnanasRuler](https://github.com/AnanasRuler)
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
Create a professional academic figure for scientific publication using the following guidelines:

${figure_type:Type of figure (architecture diagram, flowchart, data visualization, conceptual model, experimental setup)}
${subject:Specific subject or topic}
${style:Visual style preference (minimal, detailed, technical, conceptual)}

Guidelines:
- Use clean, professional design suitable for academic journals
- Ensure high contrast and readability
- Include clear labels and legends when needed
- Use consistent color scheme (typically blues, grays, and accent colors)
- Maintain scientific accuracy
- Optimize for the specified resolution (${resolution:2K})
- Consider the target publication format

Generate a ${aspect_ratio:16:9} aspect ratio image that effectively communicates the ${subject} concept to an academic audience.
```
