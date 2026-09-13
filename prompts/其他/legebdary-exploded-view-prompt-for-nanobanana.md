# Legebdary Exploded View Prompt For nanobanana

## 说明

用途概述：{ "name": "My Workflow", "steps": [] }{ "promptDetails": { "description": "Ultra-detailed exploded technical infographic of {OBJECT_NAME}, shown in a 3/4 front isometric view.
中文概述：生成物体 3/4 等角爆炸分解技术信息图：部件分离悬浮、白色引线与编号标注、暗灰影棚背景。
关键词：爆炸视图、exploded view、技术信息图、isometric、产品拆解

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：stiva1979@gmail.com
- 类型：结构化(JSON/模版)（原始类型 STRUCTURED）
- 面向开发者：否

## Prompt 内容

```text
{
  "name": "My Workflow",
  "steps": []
}{
  "promptDetails": {
    "description": "Ultra-detailed exploded technical infographic of {OBJECT_NAME}, shown in a 3/4 front isometric view. The object is partially transparent and opened, with its key internal and external components separated and floating around the main body in a clean exploded-view layout. Show all major parts typical for {OBJECT_NAME}: outer shell/panels, structural frame, primary electronics/boards, power system/battery or PSU, ports/connectors, display or interface elements if present, input controls/buttons, mechanical modules (motors/gears/fans/hinges) if applicable, speakers/microphones if applicable, cables/flex ribbons, screws/brackets, and EMI/thermal shielding. Use thin white callout leader lines and numbered labels in a minimalist sans-serif font. Background: smooth dark gray studio backdrop. Lighting: soft, even, high-end product render lighting with subtle reflections. Style: photoreal 3D CAD render, industrial design presentation, high contrast, razor-sharp, 8K, clean composition, no clutter.",
    "styleTags": [
      "Exploded View",
      "Technical Infographic",
      "Photoreal 3D CAD Render",
      "Industrial Design Presentation",
      "Minimalist Labels",
      "Dark Studio Background"
    ]
  },
  "negativePrompt": "no people, no messy layout, no extra components, no brand logos, no text blur, no cartoon, no low-poly, no watermark, no distorted perspective, no heavy noise",
  "generationHints": {
    "aspectRatio": "2:3",
    "detailLevel": "ultra",
    "stylization": "low-medium",
    "camera": {
      "angle": "3/4 front isometric",
      "lens": "product render perspective"
    },
    "lighting": "soft even studio lighting, subtle reflections",
    "background": "smooth dark gray seamless backdrop"
  }
}
```
