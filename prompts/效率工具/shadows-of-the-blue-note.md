# Shadows of the Blue Note

## 说明

用途概述：{ "title": "Shadows of the Blue Note", "description": "A tense, high-stakes meeting between a weary detective and a glamorous informant in a smoky 1950s jazz lounge.
中文概述：AI 执行图像编辑，将照片中一男一女改造为 1950 年代 film noir 的私家侦探与 femme fatale，在烟雾爵士吧场景呈现电影级写实光影。
关键词：图像编辑、film noir、photorealistic、爵士俱乐部、人像替换

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@ersinkoc](https://github.com/ersinkoc)
- 类型：结构化(JSON/模版)（原始类型 STRUCTURED）
- 面向开发者：否

## Prompt 内容

```text
{
  "title": "Shadows of the Blue Note",
  "description": "A tense, high-stakes meeting between a weary detective and a glamorous informant in a smoky 1950s jazz lounge.",
  "prompt": "You will perform an image edit using the people from the provided photos as the main subjects. Preserve their core likeness. Transform Subject 1 (male) and Subject 2 (female) into characters from a classic 1950s film noir. Subject 1 is a rugged private investigator, and Subject 2 is an elegant femme fatale. They are seated at a secluded booth in a dimly lit, smoke-filled jazz club. The image must be ultra-photorealistic, utilizing cinematic lighting to create deep shadows and highlights. The scene should look like a frame from a high-budget blockbuster movie, shot on Arri Alexa, highly detailed, with a shallow depth of field focusing on their intense interaction.",
  "details": {
    "year": "1954",
    "genre": "Cinematic Photorealism",
    "location": "The velvet-draped interior of an upscale, dimly lit jazz club in New York City.",
    "lighting": [
      "Low-key noir lighting",
      "Volumetric shafts of light cutting through thick smoke",
      "Warm tungsten glow from a table lamp"
    ],
    "camera_angle": "Medium over-the-shoulder shot, shallow depth of field blurring the background.",
    "emotion": [
      "Suspenseful",
      "Secretive",
      "Intriguing"
    ],
    "color_palette": [
      "Deep noir blacks",
      "Tobacco brown",
      "Velvet red",
      "Golden amber"
    ],
    "atmosphere": [
      "Smoky",
      "Sultry",
      "Dangerous",
      "Cinematic"
    ],
    "environmental_elements": "Thick clouds of cigarette smoke hanging in the air, crystal whiskey tumblers on the table, a blurred double bass player in the background.",
    "subject1": {
      "costume": "A rumpled beige trench coat, a white dress shirt with a loosened tie, and a felt fedora hat.",
      "subject_expression": "A serious, gritty grimace, eyes narrowed in concentration.",
      "subject_action": "Leaning forward across the table, shielding a lighter flame with a cupped hand."
    },
    "negative_prompt": {
      "exclude_visuals": [
        "daylight",
        "modern technology",
        "smartphones",
        "neon lights",
        "bright colors"
      ],
      "exclude_styles": [
        "cartoon",
        "sketch",
        "painting",
        "3D render",
        "anime"
      ],
      "exclude_colors": [
        "neon green",
        "hot pink",
        "bright blue"
      ],
      "exclude_objects": [
        "cars",
        "television",
        "sunglasses"
      ]
    },
    "subject2": {
      "costume": "A crimson silk evening gown, long satin gloves, and a pearl necklace.",
      "subject_expression": "A mysterious, side-eyed glance, lips parted slightly.",
      "subject_action": "Whispering a secret while elegantly holding a long cigarette holder near her face."
    }
  }
}
```
