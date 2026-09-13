# The Missing Woman

## 说明

用途概述：image-generation: main: "An 1980s-style woman walking with a cat beside her, both in the foreground.
中文概述：生成 80 年代着装女子带猫夜行街道的图像，结构化列出服装、街景、布光、负向词等参数
关键词：图像生成、photorealistic、80年代、negative-prompt、人物设定

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@hamitabis](https://github.com/hamitabis)
- 类型：结构化(JSON/模版)（原始类型 STRUCTURED）
- 面向开发者：否

## Prompt 内容

```text
image-generation:
  main: "An 1980s-style woman walking with a cat beside her, both in the foreground."
  clothes: "worn jacket, blanket and old pants."
  faces: "Not visible or turned away"

  environment:
    streets: "Tree-lined, single-story houses, dead-end street."
    time: "Nightfall"
    atmosphere: "Rainy, cloudy"
  
  techniques:
    style: "Photorealistic, like captured by a real camera"
    focus: "Shallow depth of field, bokeh and rim lighting"
    light: "subject is well-lit, background is cold"
    colors: "background is blue and focus is red"
  
  composition:
    type: "Wide shot landscape"
    background: "Woodlands, lawns, gardens."
  
  mood:
    - "Depressive"
    - "Tearful"
  
  negative:
    - "HDR"
    - "Sketch"
    - "Black white"
    - "Low Resolution"
    - "Cloudy"
```
