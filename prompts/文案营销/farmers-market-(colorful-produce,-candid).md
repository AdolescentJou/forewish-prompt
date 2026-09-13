# Farmers Market (colorful produce, candid)

## 说明

用途概述：{ "category": "FARMERS_MARKET_PRODUCE_CANDID", "identity_lock": { "enabled": true, "priority": "ABSOLUTE_MAX", "instruction": "Lock identity to reference image exactly.
中文概述：图像生成规范：锁定参照人物身份的成年女性，在农贸市场拎农产品袋自然行走的写实随拍场景。
关键词：图像prompt、identity_lock、写实照片、farmers market、人像

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：dorukkurtoglu@gmail.com
- 类型：结构化(JSON/模版)（原始类型 STRUCTURED）
- 面向开发者：否

## Prompt 内容

```text
{
  "category": "FARMERS_MARKET_PRODUCE_CANDID",
  "identity_lock": {
    "enabled": true,
    "priority": "ABSOLUTE_MAX",
    "instruction": "Lock identity to reference image exactly. Adult 21+ only. No face changes."
  },
  "subject": {
    "demographics": "Adult woman, 21-29, match reference identity.",
    "hair": {
      "color": "Match reference.",
      "style": "Loose waves, tucked behind ear",
      "texture": "Strands visible, mild flyaways",
      "movement": "Natural movement while walking"
    },
    "face": {
      "eyes": "Exact reference eyes; bright daylight catchlights",
      "skin_details": "Pores visible, natural sunlit texture",
      "micro_details": "Preserve marks"
    },
    "clothing": {
      "outfit": "Casual black top + light jacket (no logos/text)",
      "fabric": "Cotton/denim weave visible"
    },
    "accessories": {
      "bag": "Canvas tote (no logos)",
      "jewelry": ["Small silver hoops"],
      "props": ["Paper bag of produce (unbranded)"]
    }
  },
  "pose": {
    "type": "Walking candid",
    "orientation": "Half-body",
    "hands": "One hand holding produce bag, other adjusting tote strap",
    "gaze": "Looking at camera mid-laugh",
    "expression": "Bright, natural smile"
  },
  "setting": {
    "environment": "Outdoor farmers market",
    "background_elements": [
      "Colorful fruit/vegetable stalls (no readable signs)",
      "Soft crowd blur (no identifiable faces)",
      "Sunlight dappling"
    ],
    "depth": "Subject sharp; background lively bokeh"
  },
  "camera": {
    "shot_type": "Half-body lifestyle",
    "angle": "Eye level",
    "focal_length_equivalent": "26mm phone or 35mm editorial",
    "framing": "4:5, subject off-center",
    "focus": "Face sharp; background soft"
  },
  "lighting": {
    "source": "Natural daylight",
    "direction": "Soft front/side",
    "highlights": "Natural facial highlights",
    "shadows": "Soft under-chin"
  },
  "mood_and_expression": {
    "tone": "Fresh, happy, relatable",
    "atmosphere": "Weekend candid"
  },
  "style_and_realism": {
    "style": "Photorealistic IG lifestyle",
    "imperfections": "Minor motion blur in produce bag edges allowed"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "resolution": "High",
    "noise": "Low",
    "mode_variants": {
      "amateur": "Slightly shaky candid framing, mild HDR, imperfect crop",
      "pro": "Clean editorial exposure, crisp detail, shallow DOF"
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
    "readable text", "logos", "watermark",
    "identity drift", "face morphing",
    "extra fingers", "warped hands",
    "plastic skin", "over-smoothing"
  ]
}
```
