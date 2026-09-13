# A Wrinkle in Time

## 说明

用途概述：{ "prompt": "You will perform an image edit using the person from the provided photo as the main subject.
中文概述：把照片中人物改写成穿越到史前丛林的维多利亚时代旅人，写实电影质感
关键词：图像编辑、人像变换、科幻穿越、电影感、照片处理

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@ersinkoc](https://github.com/ersinkoc)
- 类型：结构化(JSON/模版)（原始类型 STRUCTURED）
- 面向开发者：否

## Prompt 内容

```text
{
  "prompt": "You will perform an image edit using the person from the provided photo as the main subject. Preserve his core likeness. Transform Subject 1 (male) into a Victorian time traveler who has just materialized in a dense, prehistoric jungle. The image must be Ultra-Photorealistic, Movie-Quality, and highly detailed. The scene captures the moment of arrival, shot on Arri Alexa with cinematic lighting and a shallow depth of field. He stands amidst towering ferns and ancient cycads, looking completely out of place in his formal 19th-century attire, contrasting the rugged, humid environment with his refined appearance.",
  "details": {
    "year": "1895 / 65 Million BC",
    "genre": "Cinematic Photorealism",
    "location": "A dense, steaming Cretaceous jungle floor filled with giant ferns, ancient conifers, and thick atmospheric fog.",
    "lighting": [
      "Volumetric god rays piercing through the canopy",
      "Dappled sunlight",
      "High dynamic range"
    ],
    "camera_angle": "Medium close-up at eye level, focusing on the subject with the background falling into soft bokeh.",
    "emotion": [
      "Disbelief",
      "Awe",
      "Scientific curiosity",
      "Fear"
    ],
    "color_palette": [
      "Deep emerald greens",
      "Earthy mud browns",
      "Burnished brass",
      "Tweed grey"
    ],
    "atmosphere": [
      "Humid",
      "Primordial",
      "Claustrophobic",
      "Mysterious"
    ],
    "environmental_elements": "Floating pollen particles, massive prehistoric insects buzzing in the background, a large ominous silhouette of a dinosaur visible through the thick mist.",
    "subject1": {
      "costume": "A bespoke three-piece Victorian tweed suit, a slightly askew cravat, and intricate brass steampunk goggles pushed up onto his forehead.",
      "subject_expression": "Wide-eyed shock mixed with fascination, mouth slightly open, sweat beading on his brow.",
      "subject_action": "Clutching a glowing, smoking brass chronometer device in one hand while tentatively reaching out to touch a massive, alien-looking fern frond with the other."
    },
    "negative_prompt": {
      "exclude_visuals": [
        "modern buildings",
        "paved roads",
        "cars",
        "cell phones",
        "contemporary fashion",
        "cleanliness"
      ],
      "exclude_styles": [
        "cartoon",
        "3D render",
        "illustration",
        "painting",
        "low resolution",
        "blur",
        "sketch"
      ],
      "exclude_colors": [
        "neon",
        "pastel pinks",
        "artificial brights"
      ],
      "exclude_objects": [
        "spaceships",
        "aliens",
        "modern weapons"
      ]
    }
  }
}
```
