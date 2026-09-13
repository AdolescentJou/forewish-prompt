# “Blue Hour Bridge” (full-body, cinematic but still IG)

## 说明

用途概述：{ "category": "BLUE_HOUR_BRIDGE_FULLBODY", "subject": { "demographics": "Adult woman, 21-29, Turkish-looking, calm confident vibe.
中文概述：以JSON描述蓝调时刻桥上全身照：土耳其风成年女性靠栏回头直视镜头，城市灯光虚化背景
关键词：blue hour、全身照、人像、桥、电影感、JSON

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：dorukkurtoglu@gmail.com
- 类型：结构化(JSON/模版)（原始类型 STRUCTURED）
- 面向开发者：否

## Prompt 内容

```text
{
  "category": "BLUE_HOUR_BRIDGE_FULLBODY",
  "subject": {
    "demographics": "Adult woman, 21-29, Turkish-looking, calm confident vibe.",
    "hair": {
      "color": "Dark brown",
      "style": "Loose waves, slightly wind-touched",
      "texture": "Individual strands visible",
      "movement": "Small motion in hair tips"
    },
    "face": {
      "eyes": "Calm direct gaze",
      "skin_details": "Natural texture, no smoothing"
    },
    "clothing": {
      "outfit": "Minimal black coat + fitted top, no logos",
      "fabric": "Coat texture visible, slight wrinkles"
    },
    "accessories": {
      "jewelry": ["Silver hoops"]
    }
  },
  "pose": {
    "type": "Full-body leaning on railing",
    "orientation": "Body angled, head turned to camera",
    "hands": "Hands resting on railing, fingers correct",
    "gaze": "Direct eye contact",
    "expression": "Neutral calm confidence"
  },
  "setting": {
    "environment": "Bridge at blue hour",
    "background_elements": [
      "City lights bokeh",
      "Cool dusk ambience",
      "Railing texture visible"
    ],
    "depth": "Subject sharp, background bokeh"
  },
  "camera": {
    "shot_type": "Full-body portrait",
    "angle": "Eye-level",
    "focal_length_equivalent": "35mm editorial",
    "framing": "4:5, subject off-center",
    "focus": "Face sharp, background creamy"
  },
  "lighting": {
    "source": "Ambient dusk + city light bounce",
    "direction": "Soft front fill from environment",
    "highlights": "Controlled, subtle"
  },
  "mood_and_expression": {
    "tone": "Cinematic, calm, premium",
    "atmosphere": "Blue hour dreamy realism"
  },
  "style_and_realism": {
    "style": "Photoreal social/editorial",
    "imperfections": "Slight low-light noise allowed"
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
    "fake skyline", "cgi",
    "plastic skin", "over-smoothing",
    "extra fingers", "warped railing",
    "readable text", "logos", "watermark"
  ]
}
```
