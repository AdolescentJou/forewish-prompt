# Nightclub Booth Flash (half-body, party candids)

## 说明

用途概述：{ "category": "NIGHTCLUB_BOOTH_FLASH", "subject": { "demographics": "Adult woman, 21-29, Turkish-looking, nightlife vibe.
中文概述：AI 生成夜店卡座抓拍式照片描述：土耳其女性半身、灯光氛围
关键词：图像生成、夜店、party candid、写实人像、照片提示词

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：dorukkurtoglu@gmail.com
- 类型：结构化(JSON/模版)（原始类型 STRUCTURED）
- 面向开发者：否

## Prompt 内容

```text
{
  "category": "NIGHTCLUB_BOOTH_FLASH",
  "subject": {
    "demographics": "Adult woman, 21-29, Turkish-looking, nightlife vibe.",
    "hair": {
      "color": "Dark brown",
      "style": "Slightly messy, night-out texture",
      "texture": "Strands visible, slight shine",
      "movement": "Hair slightly displaced as if dancing"
    },
    "face": {
      "eyes": "Bright, playful",
      "skin_details": "Real texture, slight flash shine",
      "makeup": "Night-out natural glam"
    },
    "clothing": {
      "outfit": "Trendy black outfit, no logos",
      "fabric": "Realistic fabric sheen (not plastic)"
    },
    "accessories": {
      "jewelry": ["Silver hoops"],
      "props": ["Simple drink glass (no labels)"]
    }
  },
  "pose": {
    "type": "Half-body candid booth shot",
    "orientation": "Leaning slightly toward camera",
    "hands": "One hand holding glass, other brushing hair back",
    "gaze": "Direct eye contact",
    "expression": "Playful smirk"
  },
  "setting": {
    "environment": "Nightclub booth",
    "background_elements": [
      "Colored lights bokeh",
      "Soft atmospheric haze (not smoke)",
      "Crowd silhouettes blurred (no faces identifiable)"
    ],
    "depth": "Face sharp, background bokeh heavy"
  },
  "camera": {
    "shot_type": "Half-body nightlife portrait",
    "angle": "Eye-level, handheld",
    "focal_length_equivalent": "26mm phone night mode",
    "framing": "4:5",
    "focus": "Eyes sharp, background soft"
  },
  "lighting": {
    "source": "Phone flash + ambient club lights",
    "highlights": "Flash pop on face, realistic shine",
    "shadows": "Soft but contrasty nightlife look"
  },
  "mood_and_expression": {
    "tone": "Fun, confident, candid",
    "atmosphere": "Energetic nightlife"
  },
  "style_and_realism": {
    "style": "Photorealistic party UGC",
    "imperfections": "Grain, slight blur in background"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "noise": "Noticeable but realistic low-light noise",
    "motion_blur": "Minimal; allowed in background only"
  },
  "constraints": {
    "adult_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true
  },
  "negative_prompt": [
    "readable signage", "logos", "watermark",
    "plastic skin", "cgi",
    "extra limbs", "warped hands"
  ]
}
```
