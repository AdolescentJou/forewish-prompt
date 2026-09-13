# Whispers in Light Trails

## 说明

用途概述：{ "title": "Whispers in Light Trails", "description": "A cinematic long-exposure capture of a 1950s noir scene, contrasting the stillness of a detective with the kinetic energy of a jazz club.
中文概述：将照片中的两人改造成 1950s 长曝光 noir 画面：侦探静坐、爵士歌手化为光轨
关键词：图像编辑、长曝光、Noir、爵士、电影感

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@ersinkoc](https://github.com/ersinkoc)
- 类型：结构化(JSON/模版)（原始类型 STRUCTURED）
- 面向开发者：否

## Prompt 内容

```text
{
  "title": "Whispers in Light Trails",
  "description": "A cinematic long-exposure capture of a 1950s noir scene, contrasting the stillness of a detective with the kinetic energy of a jazz club.",
  "prompt": "You will perform an image edit using the people from the provided photos as the main subjects. Preserve their core likeness. Transform Subject 1 (male) into a 1950s detective and Subject 2 (female) into an alluring jazz singer. Utilize a Long Exposure artistic style where time seems to bleed. Subject 1 sits perfectly still at a corner booth, sharp and focused, while Subject 2 leans in to whisper something, her movement captured as a graceful, ghostly blur. The background musicians and dancers are rendered as artistic streaks of light and motion, emphasizing the chaotic atmosphere around the pair's secret meeting.",
  "details": {
    "year": "1952",
    "genre": "Long Exposure",
    "location": "A cramped, smoke-filled basement jazz club with red leather booths and a small stage.",
    "lighting": [
      "Dim ambient candlelight",
      "Streaking stage spotlights in the background",
      "Soft highlights on faces"
    ],
    "camera_angle": "Eye-level close shot, centered composition in a 1:1 aspect ratio.",
    "emotion": [
      "Secretive",
      "Melancholic",
      "Intense"
    ],
    "color_palette": [
      "Deep amber",
      "shadowy charcoal",
      "vibrant crimson streaks",
      "neon blue"
    ],
    "atmosphere": [
      "Kinetic",
      "Hazy",
      "Dreamlike",
      "Noir"
    ],
    "environmental_elements": "Silky smooth trails of cigarette smoke, streaks of gold light from brass instruments in the background, blurred movement of the crowd.",
    "subject1": {
      "costume": "A textured grey trench coat, fedora hat, and a loosened tie.",
      "subject_expression": "Stoic and intense, eyes locked forward.",
      "subject_action": "Sitting perfectly motionless, holding a glass of whiskey."
    },
    "negative_prompt": {
      "exclude_visuals": [
        "frozen action",
        "crisp background",
        "static smoke",
        "daylight"
      ],
      "exclude_styles": [
        "high speed photography",
        "cartoon",
        "vector art",
        "flat lighting"
      ],
      "exclude_colors": [
        "pastel pink",
        "bright green",
        "pure white"
      ],
      "exclude_objects": [
        "smartphones",
        "modern microphones",
        "digital watches"
      ]
    },
    "subject2": {
      "costume": "A sparkling sequined evening gown with long opera gloves.",
      "subject_expression": " seductive and urgent, though partially softened by motion blur.",
      "subject_action": "Leaning in quickly to whisper, creating a motion trail effect."
    }
  }
}
```
