# Photo-to-Isometric: Reality Slice Generator

## 说明

用途概述：{ "prompt": "Create an ultra realistic isometric diorama based strictly on the uploaded image.
中文概述：解析上传照片的建筑与街道元素,重建为 45° isometric 超写实微缩街区切片 diorama
关键词：图像生成、isometric、diorama、照片转 3D、tilt-shift

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@mehmetaltugakgul](https://github.com/mehmetaltugakgul)
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
{
  "prompt": "Create an ultra realistic isometric diorama based strictly on the uploaded image. Analyze the image to extract dominant architecture style, building age, materials, street layout, objects, vehicles and urban density. Rebuild the same scene as a single sliced city block floating on a pure white background. Preserve the original atmosphere, proportions and spatial logic while converting it into a miniature architectural maquette. Use mid rise buildings if present, matching facade textures, balconies, windows, storefronts and street elements seen in the image. Keep only elements visible in the source image. Remove anything not present. Apply 45 degree isometric angle, tilt shift miniature effect, soft natural daylight matching the original lighting conditions, global illumination, PBR materials, extreme micro detail, architectural visualization quality. Clean studio lighting. No sky, no horizon.",
  "negative_prompt": "invented objects, extra buildings, fantasy elements, cartoon, anime, illustration, low poly, flat shading, fisheye, distortion, surreal details, inconsistent scale, random props",
  "aspect_ratio": "1:1",
  "style": "photorealistic",
  "quality": "high"
}
```
