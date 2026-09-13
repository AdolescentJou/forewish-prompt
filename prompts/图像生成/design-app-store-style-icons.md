# Design App Store Style Icons

## 说明

用途概述：Reconstruct the central object of the given 2D image as a true 3D wireframe model.
中文概述：把给定 2D 图像的中心物体重建为真实 3D 线框模型，输出 Apple App Store 风格、无文字的发光线框图标。
关键词：app icon、3D wireframe、iOS设计、图像重建、WWDC风格

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@zekkontro](https://github.com/zekkontro)
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
Reconstruct the central object of the given 2D image as a true 3D wireframe model.

- Interpret the 2D shape as volumetric geometry and extrude it into depth.

- Build visible 3D structure with wireframe mesh lines wrapping around the form (front, sides, and curvature).

- Use thin, precise, glowing white wireframe lines only, no solid surfaces, no flat fills.

- Apple App Store style icon, premium iOS design language, WWDC-inspired.

- Rounded square app icon, centered and symmetrical.

- Soft blue gradient background, subtle glow.

- Clean orthographic front view with clear depth cues (z-axis wireframe).

- High-resolution, futuristic UI icon.

- No text, no logos, no illustration style


Negatives:

2D flat design, flat icon, illustration, lighting-only depth, fake 3D, gradients on object, shading, shadows, cartoon style, sketch, photorealism, textures, noise, grain
```
