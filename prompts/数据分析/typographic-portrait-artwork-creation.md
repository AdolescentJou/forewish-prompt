# Typographic Portrait Artwork Creation

## 说明

用途概述：Transform the provided portrait into a 9:16 vertical typographic artwork built exclusively from repeated name text.
中文概述：将输入肖像转为9:16竖版纯文字排版作品，仅用均匀小号重复姓名文本构成面部细节，禁用任何线条图形。
关键词：typography、文字排版、肖像艺术、纯文字、竖版设计、微排版

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@senoldak](https://github.com/senoldak)
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
Transform the provided portrait into a 9:16 vertical typographic artwork built exclusively from repeated name text.

STRICT RULES:
- The image must be composed ONLY of text (e.g., "MUSTAFA KEMAL ATATÜRK").
- No lines, no strokes, no outlines, no shapes, no shading, no gradients.
- Do NOT draw anything. Do NOT use any brush or illustration effect.
- No stamp borders or shapes — only pure text.
- Every visible detail must come from the text itself.

TEXT CONSTRAINT:
- ALL text must be small and consistent in size.
- Do NOT use large or oversized text anywhere.
- Font size should remain uniform across the entire image.
- The text should feel like fine grain / micro-typography.

Preserve the exact facial identity and proportions from the input image.

COMPOSITION:
- Slightly zoomed-out portrait (not close-up).
- Include full head with some negative space around.

REGIONAL CONTROL:
- Forehead area should be clean or extremely sparse.
- Focus density on eyes, nose, mouth, jawline.

SHADING METHOD:
- Create depth ONLY by changing text density (not size).
- Dark areas = very dense text repetition.
- Light areas = sparse text placement.
- No gradient effects — density alone must simulate light and shadow.

Arrange text with slight variations in rotation and spacing, but keep it controlled and clean.

Style:
minimal, high-contrast black text on light background, elegant and editorial.

No extra text outside the repeated name. No logos. No decorative elements.

The result should look like a refined typographic portrait where shadows are created purely through text density, with zero size variation.
```
