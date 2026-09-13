# Subway Platform (street candid, moody)

## 说明

用途概述：{ "category": "SUBWAY_PLATFORM_STREET_CANDID", "identity_lock": { "enabled": true, "priority": "ABSOLUTE_MAX", "instruction": "Use reference image identity exactly.
中文概述：AI 按参考图绝对锁定人物身份(成人、保留面部特征不加美化)，生成地铁站台街头随拍情绪风人像图并细化发丝、皮肤与服装规格。
关键词：图像生成、街头随拍、identity_lock、写实人像、moody

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：dorukkurtoglu@gmail.com
- 类型：结构化(JSON/模版)（原始类型 STRUCTURED）
- 面向开发者：否

## Prompt 内容

```text
{
  "category": "SUBWAY_PLATFORM_STREET_CANDID",
  "identity_lock": {
    "enabled": true,
    "priority": "ABSOLUTE_MAX",
    "instruction": "Use reference image identity exactly. Adult 21+. Preserve face proportions and marks. No beautification."
  },
  "subject": {
    "demographics": "Adult woman, 21-29, match reference identity.",
    "hair": {
      "color": "Match reference.",
      "style": "Low ponytail or loose waves tucked behind scarf",
      "texture": "Real strands; slight frizz; flyaways",
      "movement": "Minimal movement, platform breeze subtle"
    },
    "face": {
      "eyes": "Exact reference; reflective catchlights",
      "skin_details": "Pores visible, realistic shadows",
      "micro_details": "Preserve marks"
    },
    "clothing": {
      "outerwear": "Minimal black coat or jacket (no logos/text)",
      "extras": "Scarf optional (no patterns with text)",
      "fabric": "Wool texture visible"
    },
    "accessories": {
      "jewelry": ["Small silver hoops (optional)"],
      "bag": "Simple tote/shoulder bag (no logos)"
    }
  },
  "pose": {
    "type": "Candid waiting",
    "orientation": "Half-body standing near platform edge (safe distance)",
    "head_position": "Slight tilt, calm posture",
    "hands": "One hand holding bag strap, other in pocket",
    "gaze": "Looking toward camera with neutral confidence",
    "expression": "Calm, slightly serious"
  },
  "setting": {
    "environment": "Subway platform",
    "background_elements": [
      "Overhead fluorescent lights",
      "Train blur in background (no readable signage)",
      "Platform tiles with realistic wear"
    ],
    "depth": "Face sharp; background softened"
  },
  "camera": {
    "shot_type": "Street-style portrait",
    "angle": "Eye level",
    "focal_length_equivalent": "35mm editorial OR 26mm phone",
    "framing": "4:5, leading lines from platform",
    "focus": "Eyes sharp, background motion blur allowed"
  },
  "lighting": {
    "source": "Fluorescent overhead + ambient",
    "direction": "Top-down with mild fill",
    "highlights": "Realistic shine on hair/skin",
    "shadows": "Soft, slightly cool subway contrast"
  },
  "mood_and_expression": {
    "tone": "Moody, urban, confident",
    "atmosphere": "Real city commute candid"
  },
  "style_and_realism": {
    "style": "Photoreal street portrait",
    "imperfections": "Noise + slight motion blur in background"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "resolution": "High",
    "noise": "Moderate low-light grain",
    "mode_variants": {
      "amateur": "Phone-like HDR, mild grain, imperfect framing",
      "pro": "Cleaner exposure, controlled highlights, crisp subject separation"
    }
  },
  "constraints": {
    "adult_only": true,
    "single_subject_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true,
    "no_readable_signage": true
  },
  "negative_prompt": [
    "readable signs", "logos", "watermark",
    "identity drift", "face morphing",
    "extra fingers", "warped hands",
    "cgi", "plastic skin", "over-smoothing"
  ]
}
```
