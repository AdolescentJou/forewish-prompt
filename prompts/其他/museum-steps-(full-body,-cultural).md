# Museum Steps (full-body, cultural)

## 说明

用途概述：{ "category": "MUSEUM_STEPS_FULLBODY", "subject": { "demographics": "Adult woman, 21-27, Turkish-looking, artsy vibe.
中文概述：生成土耳其裔女性坐在博物馆台阶上的全身文化写真，自然光与石质环境细节
关键词：全身写真、博物馆、人物摄影、自然光、图像生成

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：dorukkurtoglu@gmail.com
- 类型：结构化(JSON/模版)（原始类型 STRUCTURED）
- 面向开发者：否

## Prompt 内容

```text
{
  "category": "MUSEUM_STEPS_FULLBODY",
  "subject": {
    "demographics": "Adult woman, 21-27, Turkish-looking, artsy vibe.",
    "hair": {
      "color": "Dark brown",
      "style": "Loose waves, tucked behind one ear",
      "texture": "Natural strands, slight flyaways"
    },
    "face": {
      "eyes": "Thoughtful, warm",
      "skin_details": "Natural texture, no smoothing"
    },
    "clothing": {
      "outfit": "Minimal chic black outfit + light coat (no logos)",
      "fabric": "Textile weave visible"
    },
    "accessories": {
      "jewelry": ["Silver hoops"]
    }
  },
  "pose": {
    "type": "Seated full-body",
    "orientation": "Sitting on steps, ankles crossed",
    "hands": "One hand resting on knee, other near chin",
    "gaze": "Soft eye contact, calm",
    "posture": "Relaxed, composed"
  },
  "setting": {
    "environment": "Museum exterior steps",
    "background_elements": [
      "Stone texture with realistic pores and wear",
      "Soft daylight",
      "No readable plaques/signage"
    ],
    "depth": "Subject sharp, background softly blurred"
  },
  "camera": {
    "shot_type": "Full-body portrait",
    "angle": "Slightly low angle for elegance",
    "focal_length_equivalent": "35-50mm editorial",
    "framing": "4:5",
    "focus": "Face + hands sharp, background soft"
  },
  "lighting": {
    "source": "Natural daylight",
    "direction": "Soft front-side",
    "shadows": "Gentle, realistic"
  },
  "mood_and_expression": {
    "tone": "Artsy, calm, confident",
    "expression": "Subtle smile, thoughtful eyes"
  },
  "style_and_realism": {
    "style": "Photoreal editorial lifestyle",
    "imperfections": "Natural hair flyaways preserved"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "noise": "Very mild",
    "sharpness": "Crisp facial detail"
  },
  "constraints": {
    "adult_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true
  },
  "negative_prompt": [
    "readable text", "logos", "watermark",
    "extra fingers", "warped steps",
    "plastic skin", "cgi"
  ]
}
```
