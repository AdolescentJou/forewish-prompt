# Hyper-Realistic Marvel Comic Fusion Image Generation

## 说明

用途概述：{ "image_generation": { "requirements": { "face_preservation": { "preserve_original": true, "accuracy_level": "100% identical to reference", "details": [ "real
中文概述：AI 将参考照片融合为 hyper-realistic Marvel 漫画风儿童形象：100% 保留面部、姿态、光照与 Avenger 战衣。
关键词：Marvel、comic-style、face-preservation、儿童、图像融合

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@senoldak](https://github.com/senoldak)
- 类型：结构化(JSON/模版)（原始类型 STRUCTURED）
- 面向开发者：否

## Prompt 内容

```text
{
  "image_generation": {
    "requirements": {
      "face_preservation": {
        "preserve_original": true,
        "accuracy_level": "100% identical to reference",
        "details": [
          "real facial proportions",
          "exact skin texture",
          "true eye shape and color",
          "natural look without makeup"
        ]
      },
      "pose": {
        "match_reference_pose": true,
        "description": "Chest-up portrait, face forward with a gentle rightward tilt."
      },
      "lighting": {
        "match_reference_lighting": true,
        "type": "soft diffused indoor lighting",
        "direction": "front-left",
        "shadows": "gentle soft shadows",
        "background_tone": "neutral with slight bluish tint"
      }
    },

    "subject": {
      "gender": "male",
      "age": "child",
      "hairstyle": {
        "match_reference": true,
        "description": "same hairstyle as reference, adapted naturally for a young boy"
      },
      "expression": "neutral, slightly curious",
      "clothing": {
        "top": "Avengers-style suit top (child version), subtle tech-textured fabric",
        "accessory": "miniature Avengers emblem on the chest"
      }
    },

    "composition": {
      "frame": "chest-up portrait",
      "orientation": "frontal with slight rightward tilt",
      "style": "hyper-realistic with split real/comic effect"
    },

    "special_effects": {
      "split_effect": {
        "type": "irregular centered tear",
        "edges": "white angled torn-paper look",
        "description": "image looks ripped down the middle"
      },

      "realistic_side": {
        "background": "soft, neutral, bluish environment",
        "filters": [
          "soft analog grain",
          "light vintage texture",
          "reduced saturation",
          "subtle film imperfections"
        ],
        "overlays": [
          "small holographic HUD icons (Iron Man–style)",
          "mini Captain America shield doodle",
          "tiny Thor hammer sketch",
          "stylized blue tech sparks"
        ]
      },

      "illustrated_side": {
        "art_style": "bold comic-style illustration inspired by Marvel",
        "color_palette": "vibrant, high-contrast superhero palette",
        "hair": "same color as realistic half but stylized sharply",
        "eyes": "slightly exaggerated heroic emphasis",
        "background": "dynamic red-blue comic burst pattern",
        "decorations": {
          "elements": [
            "chibi Iron Man flying",
            "pixel-style Captain America",
            "small cartoon lightning bolts",
            "comic-style 'POW!' and 'WHOOSH!' text bubbles",
            "floating colorful Avengers symbols"
          ]
        }
      }
    },

    "aesthetic": {
      "overall_tone": "heroic, energetic, lightly vintage",
      "lighting_consistency": "perfectly matching the reference",
      "skin_texture_realism": "high",
      "blending_quality": "smooth transition with crisp tear edge"
    },

    "output": {
      "style": "hyper-realistic + Marvel comic fusion",
      "quality": "ultra-high-resolution",
      "filters": [
        "subtle analog film",
        "soft grain"
      ]
    }
  }
}
```
