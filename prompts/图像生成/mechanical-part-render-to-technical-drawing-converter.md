# Mechanical Part Render to Technical Drawing Converter

## 说明

用途概述：{ "task": "image_to_image", "description": "Convert a 3D mechanical part render into a fully dimensioned manufacturing drawing", "input_image": "3d_render_of_pipe_or_mechanical_part.
中文概述：AI 作为 image-to-image 转换器，将 3D 机械零件渲染图转为带完整毫米尺寸标注的 ISO 多视图制造工程图纸。
关键词：engineering-drawing、机械制图、image-to-image、SDXL、尺寸标注

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@senoldak](https://github.com/senoldak)
- 类型：结构化(JSON/模版)（原始类型 STRUCTURED）
- 面向开发者：否

## Prompt 内容

```text
{
  "task": "image_to_image",
  "description": "Convert a 3D mechanical part render into a fully dimensioned manufacturing drawing",
  "input_image": "3d_render_of_pipe_or_mechanical_part.png",
  "prompt": "mechanical engineering drawing, multi-view orthographic projection, front view, top view, side view and section view, fully dimensioned technical drawing, precise numeric measurements in millimeters, diameter symbols, radius annotations, hole count notation, center lines, section hatching, consistent line weights, ISO mechanical drafting standard, black ink on white background, manufacturing-ready documentation",
  "negative_prompt": "artistic style, perspective view, soft shading, textures, realistic lighting, colors, decorative rendering, sketch, hand-drawn look, incomplete dimensions",
  "settings": {
    "model": "sdxl",
    "sampler": "DPM++ 2M Karras",
    "steps": 40,
    "cfg_scale": 6,
    "denoising_strength": 0.5,
    "resolution": {
      "width": 1024,
      "height": 1024
    }
  },
  "output_expectation": "ISO-style mechanical drawing with clear dimensions suitable for CNC, casting, or fabrication reference"
}
```
