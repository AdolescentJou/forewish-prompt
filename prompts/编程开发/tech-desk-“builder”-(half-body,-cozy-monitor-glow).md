# Tech Desk “Builder” (half-body, cozy monitor glow)

## 说明

用途概述：{ "category": "TECH_DESK_BUILDER_HALF_BODY", "subject": { "demographics": "Adult woman, 21-29, Turkish-looking, creator vibe.
中文概述：生成描述土耳其裔女性创作者半身坐于暖光科技桌旁的写实图像 JSON 提示
关键词：图像生成、人物描述、JSON、科技桌、暖光、半身像

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：dorukkurtoglu@gmail.com
- 类型：结构化(JSON/模版)（原始类型 STRUCTURED）
- 面向开发者：否

## Prompt 内容

```text
{
  "category": "TECH_DESK_BUILDER_HALF_BODY",
  "subject": {
    "demographics": "Adult woman, 21-29, Turkish-looking, creator vibe.",
    "hair": {
      "color": "Dark brown",
      "style": "Low ponytail or loose waves",
      "texture": "Strands visible, slight flyaways"
    },
    "face": {
      "eyes": "Focused but friendly",
      "skin_details": "Real texture, no smoothing",
      "makeup": "Minimal"
    },
    "clothing": {
      "outfit": "Casual black top + light cardigan, no logos",
      "fabric": "Real knit weave, subtle wrinkles"
    },
    "accessories": {
      "jewelry": ["Silver hoops"]
    }
  },
  "pose": {
    "type": "Half-body seated",
    "orientation": "Body slightly angled, shoulders relaxed",
    "hands": "One hand near trackpad, other tucking hair behind ear",
    "gaze": "Looking at camera with small smirk",
    "posture": "Relaxed confident"
  },
  "setting": {
    "environment": "Minimal desk setup",
    "background_elements": [
      "Laptop/monitor with generic blurred UI (NO readable text)",
      "Warm desk lamp + cool monitor glow mix",
      "Plant in corner, small clutter blurred"
    ],
    "depth": "Face sharp, background bokeh"
  },
  "camera": {
    "shot_type": "Half-body lifestyle portrait",
    "angle": "Slightly above eye level",
    "focal_length_equivalent": "26mm phone or 50mm pro",
    "framing": "4:5",
    "focus": "Eyes sharp"
  },
  "lighting": {
    "source": "Warm lamp + cool monitor glow",
    "direction": "Soft mixed lighting with gentle shadows",
    "highlights": "Natural facial speculars",
    "shadows": "Soft, realistic"
  },
  "mood_and_expression": {
    "tone": "Cozy creator, confident",
    "expression": "Micro-smirk",
    "atmosphere": "Late-night build session vibe"
  },
  "style_and_realism": {
    "style": "Photorealistic lifestyle",
    "imperfections": "Mild noise, slight imperfect WB"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "noise": "Mild",
    "resolution": "High"
  },
  "constraints": {
    "adult_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true,
    "no_readable_screens": true
  },
  "negative_prompt": [
    "readable UI text", "logos", "watermark",
    "plastic skin", "cgi",
    "extra fingers", "warped hands"
  ]
}
```
