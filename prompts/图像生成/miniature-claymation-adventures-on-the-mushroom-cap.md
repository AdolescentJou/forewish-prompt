# Miniature Claymation Adventures on the Mushroom Cap

## 说明

用途概述：{ "prompt": "You will perform an image edit using the people from the provided photos as the main subjects.
中文概述：将照片中男女两人转为粘土质感微型冒险者,置于大红蘑菇顶的 stop-motion 定格场景
关键词：图像生成、Claymation、stop-motion、粘土、图像编辑

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@ersinkoc](https://github.com/ersinkoc)
- 类型：结构化(JSON/模版)（原始类型 STRUCTURED）
- 面向开发者：否

## Prompt 内容

```text
{
  "prompt": "You will perform an image edit using the people from the provided photos as the main subjects. Preserve their core likeness but render them as charming, handcrafted clay models. Transform Subject 1 (male) and Subject 2 (female) into miniature adventurers resting on the cap of a giant red mushroom. The scene should look like a freeze-frame from a high-budget stop-motion film, complete with visible thumbprints on the clay surfaces and uneven, sculpted textures.",
  "details": {
    "year": "Timeless Whimsy",
    "genre": "Claymation",
    "location": "A macro-scale forest floor, centered on top of a large, red Fly Agaric mushroom with white spots.",
    "lighting": [
      "Soft studio lighting",
      "Warm key light",
      "Simulated rim lighting to highlight clay edges"
    ],
    "camera_angle": "Slight high-angle macro shot with a shallow depth of field to simulate a miniature set.",
    "emotion": [
      "Joyful",
      "Cozy",
      "Wonder"
    ],
    "color_palette": [
      "Vibrant red",
      "moss green",
      "canary yellow",
      "earthy brown",
      "sky blue"
    ],
    "atmosphere": [
      "Playful",
      "Handcrafted",
      "Tactile",
      "Charming"
    ],
    "environmental_elements": "Oversized blades of grass made of flattened green clay, a snail with a spiral shell made of rolled play-dough, and cotton-ball clouds in the background.",
    "subject1": {
      "costume": "A textured hiker's vest made of matte clay, a plaid shirt with painted lines, and chunky brown boots.",
      "subject_expression": "A wide, friendly grin with slightly exaggerated, rounded features.",
      "subject_action": "Sitting on the edge of the mushroom, dangling his legs and pointing at a clay butterfly."
    },
    "negative_prompt": {
      "exclude_visuals": [
        "photorealistic skin",
        "human proportions",
        "hair strands",
        "digital gloss"
      ],
      "exclude_styles": [
        "CGI",
        "2D cartoon",
        "sketch",
        "anime",
        "watercolor"
      ],
      "exclude_colors": [
        "neon",
        "grayscale",
        "dark moody tones"
      ],
      "exclude_objects": [
        "modern technology",
        "cars",
        "buildings"
      ]
    },
    "subject2": {
      "costume": "A yellow raincoat with a smooth, glossy finish and oversized red rain boots.",
      "subject_expression": "A cheerful look with sculpted laugh lines and bright eyes.",
      "subject_action": "Kneeling on the mushroom cap, holding a giant, sculpted blueberry with both hands."
    }
  }
}
```
