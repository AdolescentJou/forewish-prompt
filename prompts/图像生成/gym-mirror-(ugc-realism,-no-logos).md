# Gym Mirror (UGC realism, no logos)

## 说明

用途概述：{ "category": "GYM_MIRROR_UGC", "subject": { "demographics": "Adult woman, 21-27, Turkish-looking, athletic.
中文概述：AI 按结构化规格生成写实 UGC 健身镜前自拍：21-27 岁土耳其裔女性、无 logo 运动装、镜中眼神交流。
关键词：UGC、健身自拍、gym-mirror、realism、人像规格

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：dorukkurtoglu@gmail.com
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
{
  "category": "GYM_MIRROR_UGC",
  "subject": {
    "demographics": "Adult woman, 21-27, Turkish-looking, athletic.",
    "hair": {
      "color": "Dark brown",
      "style": "High ponytail, slightly messy",
      "texture": "Strands visible, sweat-touched flyaways",
      "movement": "A few strands cling near forehead"
    },
    "face": {
      "eyes": "Bright, energized",
      "skin_details": "Real pores, subtle sweat sheen",
      "makeup": "Minimal, natural"
    },
    "clothing": {
      "outfit": "Minimal activewear set (no logos/text)",
      "fit": "Realistic athletic fit, subtle fabric tension",
      "texture": "Fabric knit visible"
    },
    "accessories": {
      "jewelry": ["Small silver hoops (optional)"]
    }
  },
  "pose": {
    "type": "Mirror workout selfie vibe (phone not shown directly)",
    "orientation": "Half-body",
    "hands": "One arm relaxed, the other lightly flexed (natural, not extreme)",
    "gaze": "Mirror eye contact",
    "expression": "Small proud smile"
  },
  "setting": {
    "environment": "Gym locker area",
    "background_elements": [
      "Mirrors with realistic smudges",
      "Soft fluorescent overhead lighting",
      "Equipment blurred"
    ],
    "depth": "Face + torso sharp; background softened"
  },
  "camera": {
    "shot_type": "Half-body mirror portrait",
    "angle": "Slightly high angle typical of casual selfie",
    "focal_length_equivalent": "24-28mm phone wide",
    "framing": "4:5",
    "focus": "Sharp on face, slightly softer on background"
  },
  "lighting": {
    "source": "Fluorescent overhead gym lighting",
    "direction": "Top-down with mild fill from mirrors",
    "highlights": "Realistic sweat sheen highlights",
    "shadows": "Soft under chin"
  },
  "mood_and_expression": {
    "tone": "Motivated, relatable, candid",
    "expression": "Proud and friendly"
  },
  "style_and_realism": {
    "style": "Photoreal UGC",
    "imperfections": "Mild noise, imperfect WB"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "noise": "Mild",
    "motion_blur": "Minimal"
  },
  "constraints": {
    "adult_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true
  },
  "negative_prompt": [
    "brand logos", "readable text",
    "extra fingers", "warped mirror",
    "plastic skin", "cgi look"
  ]
}
```
