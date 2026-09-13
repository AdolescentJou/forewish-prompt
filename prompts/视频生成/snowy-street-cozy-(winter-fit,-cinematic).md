# Snowy Street Cozy (winter fit, cinematic)

## 说明

用途概述：{ "category": "SNOWY_STREET_WINTER_CANDID", "identity_lock": { "enabled": true, "priority": "ABSOLUTE_MAX", "instruction": "Lock identity to reference image exactly.
中文概述：以JSON生成雪街冬日抓拍：identity lock严格锁定参考人物身份、面部与冬季穿搭细节
关键词：identity lock、雪景、winter、人像、抓拍、JSON

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：dorukkurtoglu@gmail.com
- 类型：结构化(JSON/模版)（原始类型 STRUCTURED）
- 面向开发者：否

## Prompt 内容

```text
{
  "category": "SNOWY_STREET_WINTER_CANDID",
  "identity_lock": {
    "enabled": true,
    "priority": "ABSOLUTE_MAX",
    "instruction": "Lock identity to reference image exactly. Adult 21+ only."
  },
  "subject": {
    "demographics": "Adult woman, 21-29, match reference identity.",
    "hair": {
      "color": "Match reference.",
      "style": "Hair tucked into scarf/coat with a few strands visible",
      "texture": "Natural strands, slight static flyaways",
      "movement": "Minimal movement; cold air realism"
    },
    "face": {
      "eyes": "Exact reference eyes; slight squint from cold",
      "skin_details": "Natural texture; slight redness on cheeks (subtle, realistic)",
      "micro_details": "Preserve marks"
    },
    "clothing": {
      "outerwear": "Winter coat + scarf + beanie (no logos/text)",
      "fabric": "Wool knit texture visible; tiny snow specks on coat"
    },
    "accessories": {
      "jewelry": [
        "Silver hoops optional (may be hidden by scarf)"
      ]
    }
  },
  "pose": {
    "type": "Outdoor candid",
    "orientation": "Half-body",
    "hands": "Hands holding scarf near chin (gloves optional, unbranded)",
    "gaze": "Direct eye contact, cozy smile",
    "expression": "Warm, playful"
  },
  "setting": {
    "environment": "Snowy street at dusk",
    "background_elements": [
      "Falling snowflakes (fine particles, not fog)",
      "Streetlight bokeh",
      "Soft silhouettes blurred (no identifiable faces)"
    ],
    "depth": "Face sharp; background creamy bokeh"
  },
  "camera": {
    "shot_type": "Half-body winter portrait",
    "angle": "Eye level",
    "focal_length_equivalent": "35-50mm pro OR 26mm phone night mode",
    "framing": "4:5",
    "focus": "Eyes sharp; snowflakes softly blurred"
  },
  "lighting": {
    "source": "Streetlights + ambient dusk",
    "direction": "Soft top/side glow",
    "highlights": "Warm highlights on hair/cheeks",
    "shadows": "Soft, cinematic winter contrast"
  },
  "mood_and_expression": {
    "tone": "Cozy, cinematic, cute-relatable",
    "atmosphere": "Winter candid"
  },
  "style_and_realism": {
    "style": "Photoreal lifestyle",
    "imperfections": "Low-light grain allowed"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "resolution": "High",
    "noise": "Moderate low-light grain",
    "mode_variants": {
      "amateur": "Phone night-mode feel: mild grain, slight tilt, imperfect framing",
      "pro": "Cleaner cinematic exposure, controlled highlights, shallow DOF"
    }
  },
  "constraints": {
    "adult_only": true,
    "single_subject_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true
  },
  "negative_prompt": [
    "fog machine",
    "smoke",
    "identity drift",
    "face morphing",
    "extra fingers",
    "warped hands",
    "readable text",
    "logos",
    "watermark",
    "plastic skin",
    "over-smoothing"
  ]
}
```
