# Protocol 2084: The Alleyway Hack

## 说明

用途概述：{ "prompt": "You will perform an image edit transforming the male subject into a fugitive netrunner in a gritty, high-tech future.
中文概述：让 AI 将男性人像编辑成赛博朋克雨巷中的逃犯 netrunner，产出电影级写实图像
关键词：图像编辑、赛博朋克、写实、电影感

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@ersinkoc](https://github.com/ersinkoc)
- 类型：结构化(JSON/模版)（原始类型 STRUCTURED）
- 面向开发者：否

## Prompt 内容

```text
{
  "prompt": "You will perform an image edit transforming the male subject into a fugitive netrunner in a gritty, high-tech future. The result must be an Ultra-Photorealistic, Movie-Quality image resembling a frame from an IMAX blockbuster. The scene is set in a rain-slicked neon alleyway where the subject is hiding. Ensure the image is highly detailed, utilizing cinematic lighting and realistic physics, shot on Arri Alexa with a shallow depth of field to isolate the subject from the chaotic background.",
  "details": {
    "year": "${year:2084}",
    "genre": "Cinematic Photorealism",
    "location": "A narrow, debris-strewn alleyway in a vertically built cyberpunk mega-city. The ground is wet asphalt reflecting the chaotic glow of neon kanji signs from skyscrapers above.",
    "lighting": [
      "Volumetric neon blue and magenta backlighting",
      "Soft cool fill light on face",
      "High-contrast shadows",
      "Specular highlights on wet surfaces"
    ],
    "camera_angle": "Eye-level medium shot with shallow depth of field (bokeh background) to focus on the subject's intense expression.",
    "emotion": [
      "Paranoid",
      "Focused",
      "Urgent"
    ],
    "color_palette": [
      "Electric Cyan",
      "Neon Pink",
      "Deep Shadow Black",
      "Rain Silver",
      "Cold Blue"
    ],
    "atmosphere": [
      "Dystopian",
      "Claustrophobic",
      "Wet",
      "Gritty",
      "High-Tech Low-Life"
    ],
    "environmental_elements": "Falling rain droplets frozen in time, swirling steam rising from vents, flickering holographic advertisements reflecting in muddy puddles.",
    "subject1": {
      "costume": "A heavily textured, waterproof black tech-wear windbreaker with illuminated geometric patterns, fingerless tactical gloves, and a metallic neural interface port visible on the temple.",
      "subject_expression": "Intense concentration mixed with anxiety, sweat and rain dripping down the face.",
      "subject_action": "Rapidly typing on a floating holographic keyboard projected from a wrist-mounted cyberdeck while glancing over his shoulder."
    },
    "negative_prompt": {
      "exclude_visuals": [
        "daylight",
        "sunshine",
        "blue sky",
        "clean surfaces",
        "dryness",
        "warm lighting"
      ],
      "exclude_styles": [
        "cartoon",
        "anime",
        "3D render",
        "painting",
        "low resolution",
        "blurry",
        "sketch"
      ],
      "exclude_colors": [
        "warm sepia",
        "pastels",
        "bright white",
        "beige"
      ],
      "exclude_objects": [
        "cars",
        "trees",
        "pets",
        "flowers"
      ]
    }
  }
}
```
