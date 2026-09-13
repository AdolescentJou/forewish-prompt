# Kitchen Morning Window Light (candid, cozy)

## 说明

用途概述：{ "category": "KITCHEN_MORNING_WINDOWLIGHT", "identity_lock": { "enabled": true, "priority": "ABSOLUTE_MAX", "instruction": "Use the input reference image as the only identity source.
中文概述：人像图像生成带 identity_lock：以参考图为唯一身份源，生成厨房晨光窗边 21+ 女性的写实图片。
关键词：image generation、identity_lock、人像写真、photorealistic、晨光氛围

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：dorukkurtoglu@gmail.com
- 类型：结构化(JSON/模版)（原始类型 STRUCTURED）
- 面向开发者：否

## Prompt 内容

```text
{
  "category": "KITCHEN_MORNING_WINDOWLIGHT",
  "identity_lock": {
    "enabled": true,
    "priority": "ABSOLUTE_MAX",
    "instruction": "Use the input reference image as the only identity source. Preserve exact facial structure, eye shape/spacing, nose bridge/tip, lips, jawline, cheekbones, hairline, brows, skin tone/undertone, and distinctive marks. Do not beautify, do not change ethnicity/age perception. Adult (21+) only."
  },
  "subject": {
    "demographics": "Adult woman, 21-29, Turkish-looking / Mediterranean vibe (must match reference).",
    "hair": {
      "color": "Match reference exactly.",
      "style": "Loose, slightly messy morning hair; a few face-framing strands.",
      "texture": "Visible individual strands, subtle flyaways, realistic roots.",
      "movement": "Falls naturally; slight motion in ends is acceptable."
    },
    "face": {
      "shape": "Match reference exactly.",
      "eyes": "Exact reference eye shape; natural catchlights; no uncanny sharpening.",
      "lips": "Exact reference lip shape; natural texture lines visible.",
      "skin_details": "High-fidelity pores, subtle morning sheen; no airbrushing.",
      "micro_details": "Keep reference marks/freckles/moles precisely."
    },
    "clothing": {
      "top": "Soft oversized tee or casual tank (no logos, no text).",
      "fit": "Relaxed, slightly wrinkled, realistic drape.",
      "texture": "Cotton weave visible, faint pilling allowed."
    },
    "accessories": {
      "jewelry": ["Small silver hoops (optional, realistic reflections)"]
    }
  },
  "pose": {
    "type": "Candid lifestyle",
    "orientation": "Half-body leaning lightly on counter",
    "head_position": "Slight tilt; chin relaxed",
    "hands": "One hand holding a mug; other hand brushing hair behind ear (hands anatomically correct)",
    "gaze": "Near-direct eye contact (slight off-axis like a candid moment)",
    "expression": "Sleepy-soft smile, cozy morning vibe"
  },
  "setting": {
    "environment": "Home kitchen",
    "background_elements": [
      "Window with sheer curtain diffusing daylight",
      "Countertop with subtle crumbs/coffee spoon (no branding)",
      "Plants or fruit bowl (no readable labels)",
      "Soft clutter blur (tasteful, realistic)"
    ],
    "depth": "Subject sharp; background softly blurred with natural depth layering"
  },
  "camera": {
    "shot_type": "Half-body portrait",
    "angle": "Slightly above eye level, handheld",
    "focal_length_equivalent": "24-28mm smartphone wide (amateur) OR 35-50mm (pro)",
    "framing": "4:5 IG feed, asymmetrical composition",
    "focus": "Eyes/face sharp; fall-off on shoulders/background",
    "perspective": "Natural; no face distortion"
  },
  "lighting": {
    "source": "Soft window daylight + subtle indoor bounce",
    "direction": "Side/front soft light shaping cheekbones gently",
    "highlights": "Natural speculars on eyes, nose bridge, lips",
    "shadows": "Soft-edge shadows under chin and hairline",
    "quality": "Warm, comforting, realistic morning light"
  },
  "mood_and_expression": {
    "tone": "Cozy, intimate, relatable",
    "expression": "Soft smile with lively eyes",
    "atmosphere": "Unplanned, everyday candid"
  },
  "style_and_realism": {
    "style": "Photorealistic social media lifestyle",
    "fidelity": "High detail skin texture and hair strands; no smoothing",
    "imperfections": "Minor noise in shadows allowed"
  },
  "colors_and_tone": {
    "palette": "Warm neutrals + soft daylight tones",
    "white_balance": "Slightly warm indoor/daylight mix",
    "contrast": "Medium, realistic dynamic range",
    "saturation": "Natural"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "resolution": "High resolution",
    "noise": "Mild realistic sensor grain in shadows",
    "mode_variants": {
      "amateur": "iPhone-candid feel: slight tilt, imperfect framing, mild noise, subtle motion blur away from face",
      "pro": "Editorial lifestyle: cleaner exposure, controlled highlights, crisp micro-contrast, shallow DOF"
    }
  },
  "constraints": {
    "adult_only": true,
    "single_subject_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true,
    "no_readable_labels": true
  },
  "negative_prompt": [
    "identity drift", "face morphing", "beauty filter", "porcelain skin", "over-smoothing",
    "cgi", "cartoon", "anime",
    "extra fingers", "warped hands", "duplicate person",
    "readable text", "logos", "watermark"
  ]
}
```
