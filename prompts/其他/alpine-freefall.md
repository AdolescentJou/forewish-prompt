# Alpine Freefall

## 说明

用途概述：{ "title": "Alpine Freefall", "description": "A high-octane, wide-angle action shot capturing the exhilarating rush of a freestyle skier mid-descent on a steep mountain peak.
中文概述：把照片人物处理成 GoPro 鱼眼视角高山滑雪俯冲的写实自拍图，保留本人特征
关键词：图像编辑、GoPro视角、滑雪、运动摄影、照片处理

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@ersinkoc](https://github.com/ersinkoc)
- 类型：结构化(JSON/模版)（原始类型 STRUCTURED）
- 面向开发者：否

## Prompt 内容

```text
{
  "title": "Alpine Freefall",
  "description": "A high-octane, wide-angle action shot capturing the exhilarating rush of a freestyle skier mid-descent on a steep mountain peak.",
  "prompt": "You will perform an image edit using the person from the provided photo as the main subject. Preserve her core likeness. Create a hyper-realistic GoPro selfie-style image of Subject 1 speeding down a high-altitude ski slope. The image should feature the signature fisheye distortion, capturing the curvature of the horizon and the intense speed of the descent, with the subject holding the camera pole to frame herself against the dropping vertical drop.",
  "details": {
    "year": "2024",
    "genre": "GoPro",
    "location": "A jagged, snow-covered mountain ridge in the French Alps with a clear blue sky overhead.",
    "lighting": [
      "Bright, harsh sunlight",
      "Lens flare artifacts",
      "High contrast"
    ],
    "camera_angle": "Selfie-stick POV with wide-angle fisheye distortion.",
    "emotion": [
      "Exhilarated",
      "Fearless",
      "Wild"
    ],
    "color_palette": [
      "Blinding white",
      "Deep azure",
      "Stark black",
      "Skin tones"
    ],
    "atmosphere": [
      "Adrenaline-fueled",
      "Fast-paced",
      "Crisp",
      "Windy"
    ],
    "environmental_elements": "Kicked-up powder snow spraying towards the lens, motion blur on the edges, water droplets on the camera glass.",
    "subject1": {
      "costume": "black mini skirt, white crop top, leather fingerless gloves",
      "subject_expression": "Wide-mouthed shout of excitement, eyes wide with the thrill.",
      "subject_action": "ski"
    },
    "negative_prompt": {
      "exclude_visuals": [
        "studio lighting",
        "calm",
        "static pose",
        "indoor settings",
        "trees"
      ],
      "exclude_styles": [
        "oil painting",
        "sketch",
        "warm vintage",
        "soft focus"
      ],
      "exclude_colors": [
        "sepia",
        "muted tones",
        "pastel"
      ],
      "exclude_objects": [
        "ski lift",
        "crowd",
        "buildings"
      ]
    }
  }
}
```
