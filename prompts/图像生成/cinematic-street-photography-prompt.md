# Cinematic Street Photography Prompt

## 说明

用途概述：{ "colors": { "color_temperature": "warm", "contrast_level": "medium", "dominant_palette": [ "brown", "beige", "muted teal", "cream" ] }, "composition": { "came
中文概述：生成街头电影摄影提示：过肩视角拍人群中欢笑的年轻男女，前景相机形成 frame-within-a-frame 构图。
关键词：图像生成、street photography、bokeh、框架构图、cinematic

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@senoldak](https://github.com/senoldak)、halilibrahimnuroglu@gmail.com
- 类型：结构化(JSON/模版)（原始类型 STRUCTURED）
- 面向开发者：否

## Prompt 内容

```text
{
  "colors": {
    "color_temperature": "warm",
    "contrast_level": "medium",
    "dominant_palette": [
      "brown",
      "beige",
      "muted teal",
      "cream"
    ]
  },
  "composition": {
    "camera_angle": "eye-level",
    "depth_of_field": "shallow",
    "focus": "A young ${gender} laughing",
    "framing": "The main subject is framed by a blurred crowd in the background and a camera in the foreground. The camera's screen creates a frame-within-a-frame, emphasizing the act of photography."
  },
  "description_short": "An over-the-shoulder shot of a photographer taking a picture of a joyful young ${gender} laughing heartily in the middle of a blurred crowd.",
  "environment": {
    "location_type": "outdoor",
    "setting_details": "A busy, crowded public space, likely a city street or plaza. The background is filled with many people, all rendered as a soft blur, with some red bokeh lights visible.",
    "time_of_day": "afternoon",
    "weather": "cloudy"
  },
  "lighting": {
    "intensity": "moderate",
    "source_direction": "front",
    "type": "natural"
  },
  "mood": {
    "atmosphere": "A candid moment of pure joy",
    "emotional_tone": "joyful"
  },
  "narrative_elements": {
    "character_interactions": "A photographer is capturing a candid, happy moment of a ${gender}, suggesting a positive and comfortable rapport between them.",
    "environmental_storytelling": "The crowded, out-of-focus background highlights the ${gender} as a singular point of happiness and calm within a bustling environment, making the moment feel personal and intimate.",
    "implied_action": "A photoshoot is actively in progress, capturing a spontaneous reaction from the subject."
  },
  "objects": [
    "camera",
    "${gender}",
    "crowd"
  ],
  "people": {
    "ages": [
      "young adult"
    ],
    "clothing_style": "casual winter wear",
    "count": "unknown",
    "genders": [
      "female"
    ]
  },
  "prompt": "Cinematic street photography from an over-the-shoulder perspective. A photographer holds a digital camera, its screen displaying the shot. The subject is a beautiful young Asian ${gender} with wavy brown hair, who is bursting into a joyful, open-mouthed laugh. She wears a cozy cream-colored knit sweater. The background is a dense, anonymous crowd, completely blurred with soft bokeh lights. The image has a warm, vintage color grade, shallow depth of field, and captures a candid, heartwarming moment of pure happiness.",
  "style": {
    "art_style": "realistic",
    "influences": [
      "street photography",
      "candid portraiture",
      "cinematic"
    ],
    "medium": "photography"
  },
  "technical_tags": [
    "shallow depth of field",
    "bokeh",
    "over-the-shoulder shot",
    "candid photography",
    "portrait",
    "frame within a frame",
    "warm tones"
  ],
  "use_case": "Stock photography for themes of happiness, urban life, photography, and candid moments.",
  "uuid": "c0e1b01c-e07e-41b1-b035-f8802d8ec319"
}
```
