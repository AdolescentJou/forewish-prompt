# The Gravedigger's Vigil

## 说明

用途概述：{ "title": "The Gravedigger's Vigil", "description": "A haunting portrait of a lone Victorian figure standing watch over a misty, decrepit cemetery at midnight.
中文概述：将男子照片编辑为 1888 年维多利亚掘墓人，哥特恐怖风中持提灯立于浓雾墓园，1:1 电影构图
关键词：图像编辑、gothic-horror、1888、墓园、电影构图

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@ersinkoc](https://github.com/ersinkoc)
- 类型：结构化(JSON/模版)（原始类型 STRUCTURED）
- 面向开发者：否

## Prompt 内容

```text
{
  "title": "The Gravedigger's Vigil",
  "description": "A haunting portrait of a lone Victorian figure standing watch over a misty, decrepit cemetery at midnight.",
  "prompt": "You will perform an image edit using the person from the provided photo as the main subject. Preserve his core likeness. Transform Subject 1 (male) into a solemn Victorian gravedigger standing amidst a sprawling, fog-choked necropolis. He holds a rusted lantern that casts long, uncanny shadows against the moss-covered mausoleums behind him. The composition adheres to a cinematic 1:1 aspect ratio, framing him tightly against the decaying iron gates.",
  "details": {
    "year": "1888",
    "genre": "Gothic Horror",
    "location": "An overgrown, crumbling cemetery gate with twisted iron bars and weeping angel statues.",
    "lighting": [
      "Pale, cold moonlight cutting through fog",
      "Flickering, warm amber candlelight from a lantern",
      "Deep, abyssal shadows"
    ],
    "camera_angle": "Eye-level medium shot, creating a direct and confronting connection with the viewer.",
    "emotion": [
      "Foreboding",
      "Solitary",
      "Melancholic"
    ],
    "color_palette": [
      "Obsidian black",
      "slate gray",
      "pale moonlight blue",
      "sepia tone",
      "muted moss green"
    ],
    "atmosphere": [
      "Eerie",
      "Cold",
      "Silent",
      "Supernatural",
      "Decaying"
    ],
    "environmental_elements": "Swirling ground mist that obscures the feet, twisted dead oak trees silhouetted against the moon, a lone crow perched on a headstone.",
    "subject1": {
      "costume": "A tattered, ankle-length black velvet frock coat, a weathered top hat, and worn leather gloves.",
      "subject_expression": "A somber, pale visage with a piercing, weary gaze staring into the darkness.",
      "subject_action": "Raising a lantern high with the right hand while gripping the handle of a spade with the left."
    },
    "negative_prompt": {
      "exclude_visuals": [
        "sunlight",
        "blooming flowers",
        "blue sky",
        "modern infrastructure",
        "smiling",
        "lens flare"
      ],
      "exclude_styles": [
        "cartoon",
        "cyberpunk",
        "high fantasy",
        "anime",
        "watercolor",
        "bright pop art"
      ],
      "exclude_colors": [
        "neon",
        "pastel pink",
        "vibrant orange",
        "saturated red"
      ],
      "exclude_objects": [
        "cars",
        "smartphones",
        "plastic",
        "streetlights"
      ]
    }
  }
}
```
