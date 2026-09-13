# Grocery Aisle (relatable, comedic-candid)

## 说明

用途概述：{ "category": "GROCERY_AISLE_RELATABLE_CANDID", "identity_lock": { "enabled": true, "priority": "ABSOLUTE_MAX", "instruction": "Keep exact reference identity.
中文概述：把参考人物改绘成超市过道生活化随手拍风格的女性照片，锁定原身份
关键词：图像编辑、生活照、随手拍、人物写真、超市

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：dorukkurtoglu@gmail.com
- 类型：结构化(JSON/模版)（原始类型 STRUCTURED）
- 面向开发者：否

## Prompt 内容

```text
{
  "category": "GROCERY_AISLE_RELATABLE_CANDID",
  "identity_lock": {
    "enabled": true,
    "priority": "ABSOLUTE_MAX",
    "instruction": "Keep exact reference identity. Adult 21+ only."
  },
  "subject": {
    "demographics": "Adult woman, 21-29, match reference identity.",
    "hair": {
      "color": "Match reference.",
      "style": "Casual ponytail or loose waves",
      "texture": "Real strands, flyaways",
      "movement": "Minimal"
    },
    "face": {
      "eyes": "Exact reference; playful eye contact",
      "skin_details": "Natural texture; no smoothing",
      "micro_details": "Preserve marks"
    },
    "clothing": {
      "outfit": "Casual black hoodie or jacket (no logos/text)",
      "fabric": "Cotton weave visible; slight wrinkles"
    },
    "accessories": {
      "props": [
        "Shopping basket (unbranded)"
      ]
    }
  },
  "pose": {
    "type": "Candid mid-aisle",
    "orientation": "Half-body",
    "hands": "One hand holding basket; other holding a plain-label item with NO readable text",
    "gaze": "Direct eye contact",
    "expression": "Funny 'caught in the act' smirk"
  },
  "setting": {
    "environment": "Grocery aisle",
    "background_elements": [
      "Shelves blurred with NO readable packaging text",
      "Fluorescent overhead lighting",
      "Clean reflective floor"
    ],
    "depth": "Face sharp; shelves softened"
  },
  "camera": {
    "shot_type": "Half-body candid",
    "angle": "Eye level",
    "focal_length_equivalent": "24-28mm phone wide",
    "framing": "4:5, slightly imperfect composition",
    "focus": "Eyes sharp; item slightly out of focus to avoid readable text"
  },
  "lighting": {
    "source": "Overhead fluorescent",
    "direction": "Top-down with mild fill",
    "highlights": "Realistic shine, not plastic",
    "shadows": "Soft under-chin"
  },
  "mood_and_expression": {
    "tone": "Relatable, playful, candid",
    "atmosphere": "Everyday life"
  },
  "style_and_realism": {
    "style": "Photoreal UGC",
    "imperfections": "Mild noise and imperfect WB"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "resolution": "High",
    "noise": "Mild",
    "mode_variants": {
      "amateur": "Phone candid, slightly crooked, mild HDR",
      "pro": "Cleaner exposure, sharper detail, controlled highlights"
    }
  },
  "constraints": {
    "adult_only": true,
    "single_subject_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true,
    "no_readable_packaging": true
  },
  "negative_prompt": [
    "readable labels",
    "logos",
    "watermark",
    "identity drift",
    "face morphing",
    "extra fingers",
    "warped hands",
    "plastic skin",
    "over-smoothing"
  ]
}
```
