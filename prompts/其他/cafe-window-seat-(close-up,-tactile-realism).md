# Cafe Window Seat (close-up, tactile realism)

## 说明

用途概述：{ "category": "CAFE_WINDOW_SEAT_CLOSEUP", "subject": { "demographics": "Adult woman, 21-27, Turkish-looking.
中文概述：把参考人物生成咖啡馆窗边近景人像，细节触感写实、本人不变
关键词：图像生成、咖啡馆、近景人像、写实、肖像

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：dorukkurtoglu@gmail.com
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
{
  "category": "CAFE_WINDOW_SEAT_CLOSEUP",
  "subject": {
    "demographics": "Adult woman, 21-27, Turkish-looking.",
    "hair": {
      "color": "Dark brown",
      "style": "Loose waves tucked behind one ear",
      "texture": "Individual strands visible, slight frizz",
      "movement": "A few strands fall forward naturally"
    },
    "face": {
      "shape": "Soft oval",
      "eyes": "Expressive, warm, natural wetline detail",
      "makeup": "Natural 'clean' makeup, subtle liner, soft blush",
      "skin_details": "Pores visible, natural sheen, no airbrush",
      "micro_details": "Fine baby hairs near forehead"
    },
    "clothing": {
      "top": "Casual knit or fitted tee (no text)",
      "texture": "Visible knit weave, realistic folds"
    },
    "accessories": {
      "jewelry": ["Small silver hoops"]
    }
  },
  "pose": {
    "type": "Candid portrait at a table",
    "orientation": "Close-up/half-body",
    "head_position": "Slight tilt",
    "hands": "One hand near chin, fingers relaxed and anatomically correct",
    "gaze": "Near-direct eye contact, soft smile",
    "posture": "Relaxed shoulders leaning slightly forward"
  },
  "setting": {
    "environment": "Cozy cafe by a window",
    "background_elements": [
      "Ceramic cup on table",
      "Condensation on glass",
      "Tiny crumbs on plate (subtle realism)",
      "Background patrons blurred (no identifiable faces)"
    ],
    "depth": "Shallow DOF with warm bokeh"
  },
  "camera": {
    "shot_type": "Portrait",
    "angle": "Slightly above eye level (casual handheld feel)",
    "focal_length_equivalent": "26mm phone OR 50mm pro portrait",
    "framing": "4:5, face and shoulders dominate frame",
    "focus": "Eyes sharp, background softly blurred"
  },
  "lighting": {
    "source": "Diffused window daylight + warm interior ambient",
    "direction": "Soft side light shaping cheekbones",
    "highlights": "Natural highlights on nose bridge and lips",
    "shadows": "Gentle shadow under chin, realistic contrast",
    "quality": "Soft, flattering, cozy"
  },
  "mood_and_expression": {
    "tone": "Warm, approachable, intimate",
    "expression": "Soft smile, lively eyes",
    "atmosphere": "Tactile, everyday candid"
  },
  "style_and_realism": {
    "style": "Photorealistic IG lifestyle",
    "fidelity": "High detail (lashes, pores, hair strands)",
    "imperfections": "Natural noise, slight imperfect WB allowed"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "noise": "Mild phone-like grain in shadows",
    "motion_blur": "None on face; minimal allowed in background"
  },
  "constraints": {
    "adult_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true
  },
  "negative_prompt": [
    "over-smoothing", "plastic skin", "uncanny eyes",
    "bad hands", "extra fingers",
    "readable text", "logos", "watermark",
    "cgi", "cartoon", "anime"
  ]
}
```
