# Restaurant Candle Close-up (intimate, not explicit)

## 说明

用途概述：{ "category": "CANDLELIT_RESTAURANT_CLOSEUP", "subject": { "demographics": "Adult woman, 21-29, Turkish-looking.
中文概述：生成烛光餐厅中女性特写的写实人像，暖调烛光、虚化光斑背景与自然肤质
关键词：图像生成、人像、烛光、餐厅、特写、写实

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：dorukkurtoglu@gmail.com
- 类型：结构化(JSON/模版)（原始类型 STRUCTURED）
- 面向开发者：否

## Prompt 内容

```text
{
  "category": "CANDLELIT_RESTAURANT_CLOSEUP",
  "subject": {
    "demographics": "Adult woman, 21-29, Turkish-looking.",
    "hair": {
      "color": "Dark brown",
      "style": "Loose, softly styled",
      "texture": "Real strands, gentle shine"
    },
    "face": {
      "eyes": "Soft eye contact, warm highlights",
      "makeup": "Natural glam, subtle liner",
      "skin_details": "Real pores, warm glow from candle"
    },
    "clothing": {
      "outfit": "Simple elegant black top/dress (no logos)"
    },
    "accessories": {
      "jewelry": ["Silver hoops"]
    }
  },
  "pose": {
    "type": "Close-up seated",
    "orientation": "Face toward camera",
    "hands": "One hand supporting chin, fingers relaxed",
    "gaze": "Direct eye contact",
    "expression": "Calm confident micro-smile"
  },
  "setting": {
    "environment": "Restaurant table",
    "background_elements": [
      "Candle flame bokeh",
      "Glass reflections",
      "Soft background blur (no readable signage)"
    ],
    "depth": "Face sharp, background creamy"
  },
  "camera": {
    "shot_type": "Close-up portrait",
    "angle": "Eye-level",
    "focal_length_equivalent": "50-85mm pro feel or 26mm phone variant",
    "framing": "4:5, tight crop",
    "focus": "Eyes extremely sharp"
  },
  "lighting": {
    "source": "Candle + warm ambient",
    "direction": "Warm side/front",
    "highlights": "Soft specular on lips and eyes",
    "shadows": "Gentle, flattering"
  },
  "mood_and_expression": {
    "tone": "Intimate, elegant, confident",
    "atmosphere": "Warm, cinematic"
  },
  "style_and_realism": {
    "style": "Photoreal IG portrait",
    "imperfections": "Slight grain acceptable"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "noise": "Mild low-light grain"
  },
  "constraints": {
    "adult_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true
  },
  "negative_prompt": [
    "fake flames", "cgi",
    "plastic skin", "over-smoothing",
    "extra fingers", "warped hands",
    "readable text", "logos", "watermark"
  ]
}
```
