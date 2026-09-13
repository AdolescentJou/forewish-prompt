# Airport Corridor Walk (full-body)

## 说明

用途概述：{ "category": "AIRPORT_CORRIDOR_FULLBODY", "subject": { "demographics": "Adult woman, 21-27, Turkish-looking.
中文概述：生成女子机场通道行走全身镜头的视频提示词，含外貌、穿搭、动作与镜头细节
关键词：视频生成、全身镜头、机场场景、人物描写、提示词

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：dorukkurtoglu@gmail.com
- 类型：结构化(JSON/模版)（原始类型 STRUCTURED）
- 面向开发者：否

## Prompt 内容

```text
{
  "category": "AIRPORT_CORRIDOR_FULLBODY",
  "subject": {
    "demographics": "Adult woman, 21-27, Turkish-looking.",
    "hair": {
      "color": "Dark brown",
      "style": "Low ponytail, travel-day casual",
      "texture": "Natural strands, slight flyaways",
      "movement": "Subtle motion from walking"
    },
    "face": {
      "eyes": "Bright, awake",
      "skin_details": "Real texture, no filter",
      "makeup": "Minimal travel-friendly look"
    },
    "clothing": {
      "outfit": "Travel chic: coat + comfy pants + sneakers (no logos)",
      "fabric": "Realistic wrinkles at knees/elbows"
    },
    "accessories": {
      "items": ["Rolling suitcase (no branding)", "Small tote (no logos)"],
      "jewelry": ["Small silver hoops"]
    }
  },
  "pose": {
    "type": "Full-body walking candid",
    "orientation": "Mid-stride, slight lookback",
    "hands": "One hand on suitcase handle, other holding tote strap",
    "gaze": "Lookback toward camera, subtle smile",
    "posture": "Relaxed, confident traveler"
  },
  "setting": {
    "environment": "Airport corridor",
    "background_elements": [
      "Soft overhead lights",
      "Motion blur in distant travelers (no faces identifiable)",
      "Glossy floor reflections"
    ],
    "depth": "Subject sharp; background softened with motion"
  },
  "camera": {
    "shot_type": "Full-body travel photo",
    "angle": "Eye-level",
    "focal_length_equivalent": "26mm phone or 35mm editorial",
    "framing": "4:5",
    "focus": "Face readable, outfit sharp"
  },
  "lighting": {
    "source": "Overhead airport lighting",
    "highlights": "Natural reflections on floor",
    "shadows": "Soft, realistic"
  },
  "mood_and_expression": {
    "tone": "Travel-day stylish, candid",
    "expression": "Friendly micro-smile"
  },
  "style_and_realism": {
    "style": "Photorealistic UGC travel",
    "imperfections": "Slight tilt, mild noise"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "noise": "Mild",
    "motion_blur": "Background only"
  },
  "constraints": {
    "adult_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true
  },
  "negative_prompt": [
    "readable signage", "logos",
    "extra limbs", "warped suitcase",
    "plastic skin", "cgi"
  ]
}
```
