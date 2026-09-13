# Shadows of the Cold War: The 1962 Exchange

## 说明

用途概述：{ "prompt": "You will perform an image edit using the people from the provided photos as the main subjects.
中文概述：把照片中的人物合成为 1962 冷战间谍在雾桥接头的超写实电影画面，保留本人样貌
关键词：图像编辑、合成、电影质感、冷战、写实

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@ersinkoc](https://github.com/ersinkoc)
- 类型：结构化(JSON/模版)（原始类型 STRUCTURED）
- 面向开发者：否

## Prompt 内容

```text
{
  "prompt": "You will perform an image edit using the people from the provided photos as the main subjects. Preserve their core likeness. Create an Ultra-Photorealistic, Movie-Quality scene depicting Subject 1 (male) and Subject 2 (female) as covert spies meeting on a foggy, iron bridge during the Cold War. The image must look like a frame from a high-budget blockbuster movie shot on Arri Alexa. Use cinematic lighting to create deep shadows and highlights. The scene is highly detailed with a shallow depth of field. Subject 1 is handing off a secret package to Subject 2. The composition adheres to a cinematic 1:1 aspect ratio.",
  "details": {
    "year": "1962",
    "genre": "Cinematic Photorealism",
    "location": "The Glienicke Bridge at midnight, obscured by thick river fog and illuminated by dim, yellow streetlamps.",
    "lighting": [
      "Volumetric fog lighting",
      "Noir style chiaroscuro",
      "Rim lighting on silhouettes",
      "Soft yellow tungsten glow"
    ],
    "camera_angle": "Eye-level medium closeup with a shallow depth of field to isolate the subjects from the misty background.",
    "emotion": [
      "Suspenseful",
      "Urgent",
      "Clandestine"
    ],
    "color_palette": [
      "Steel blue",
      "Fog gray",
      "Tungsten amber",
      "Deep black",
      "Vibrant crimson"
    ],
    "atmosphere": [
      "Cold",
      "Tense",
      "Cinematic",
      "Mysterious"
    ],
    "environmental_elements": "Swirling mist rising from the water below, damp iron railings, the distant blurred headlights of a vintage checkpoint vehicle.",
    "subject1": {
      "costume": "A textured charcoal wool peacoat with the collar turned up against the wind.",
      "subject_expression": "Anxious, with sweat glistening on his brow and eyes darting nervously.",
      "subject_action": "Subtly sliding a leather dossier across the railing towards Subject 2."
    },
    "negative_prompt": {
      "exclude_visuals": [
        "daylight",
        "sunshine",
        "modern cars",
        "cell phones",
        "neon signs"
      ],
      "exclude_styles": [
        "cartoon",
        "3D render",
        "sketch",
        "anime",
        "impressionist"
      ],
      "exclude_colors": [
        "neon green",
        "hot pink",
        "pastel colors"
      ],
      "exclude_objects": [
        "umbrellas",
        "crowds",
        "modern architecture"
      ]
    },
    "subject2": {
      "costume": "A classic beige trench coat belted at the waist and a red hat.",
      "subject_expression": "Stoic and composed, with a piercing, calculating gaze.",
      "subject_action": "Reaching out with a black leather-gloved hand to intercept the dossier while looking over her shoulder."
    }
  }
}
```
