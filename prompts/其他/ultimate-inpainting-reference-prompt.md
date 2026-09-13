# Ultimate Inpainting / Reference Prompt

## 说明

用途概述：A luxurious warm interior scene based on the provided reference image.
中文概述：依据参考图生成豪华暖色调室内场景，严格保持大理石材质与构图比例
关键词：图像生成、室内设计、inpainting、材质还原、参考图

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：rehamhabib.rh@gmail.com
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
A luxurious warm interior scene based on the provided reference image. Maintain exact composition, proportions, and camera angle.

Kitchen bar:
	•	Countertop must strictly use the provided marble reference image.
	•	Match exact color, pattern, veining, and realistic scale relative to the bar.
	•	Do not stylize, alter, or reinterpret the marble.
	•	Marble should integrate naturally with bar edges, reflections, and ambient lighting.

Bar base: warm natural wood.

Accent wall: vertical strip cladding in light gray, fully rounded cylindrical profiles (round, not square, no sharp edges).

Wall division:
	•	Vertically:
	•	Upper section: top 2/3 of wall height, strips 0.5 cm diameter
	•	Lower section: bottom 1/3 of wall height, strips 1 cm diameter
	•	Horizontally (along wall width):
	•	Upper section spans first two-thirds of wall width
	•	Lower section spans remaining one-third
	•	Smooth transitions, precise spacing, architectural accuracy.

Flooring: polished white Carrara marble.
Warm ambient lighting, soft indirect hidden lighting, cozy yet luxurious Italian-style high-end interior. Ultra-realistic architectural visualization.

Strict instructions for AI: exact material matching, follow reference image exactly, maintain proportions, do not reinterpret or create new patterns, marble must appear natural and realistic in scale.

⸻

Midjourney / Inpainting Parameters:

--v 6 --style raw --ar 3:4 --quality 2 --iw 2 --no artistic interpretation
```
