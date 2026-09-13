# Detailed Image Generation Prompt for Fashion and Portrait Photography

## 说明

用途概述：{ "image_generation_prompt": { "subject": { "demographics": "Young woman", "hair": { "color": "Strawberry blonde / Golden blonde", "style": "Long, voluminous, l
中文概述：输出时尚/人像摄影用详细 JSON 图像提示：人物发肤妆容、服饰材质、环境光线与构图全参数。
关键词：时尚摄影、人像提示词、JSON格式、服装细节、光线构图

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：cipeberre@gmail.com
- 类型：结构化(JSON/模版)（原始类型 STRUCTURED）
- 面向开发者：否

## Prompt 内容

```text
{
  "image_generation_prompt": {
    "subject": {
      "demographics": "Young woman",
      "hair": {
        "color": "Strawberry blonde / Golden blonde",
        "style": "Long, voluminous, layered, slightly messy waves",
        "parting": "Middle part"
      },
      "face": {
        "makeup": "Winged black eyeliner, mascara, defined eyebrows, highlighter on nose and cheeks, glossy pink lips",
        "expression": "Neutral to slight pout, focused on mirror reflection"
      },
      "physique": "Slender, fit, tan skin tone"
    },
    "apparel": {
      "outerwear": {
        "item": "Faux fur jacket",
        "color": "Crimson/red mixed tones",
        "texture": "Shaggy, plush, voluminous"
      },
      "top": {
        "item": "Corset top",
        "style": "Strapless, bustier-style, cropped",
        "material": "Crimson satin or slightly shiny fabric",
        "fit": "Tight, structured bodice"
      },
      "bottoms": {
        "item": "Jeans",
        "color": "Light blue wash",
        "fit": "Low-rise, tight fit",
        "details": "Visible stitching, front pockets"
      }
    },
    "accessories": {
      "jewelry": [
        "Thin gold chain necklace with small pendant",
        "Gold ring on right ring finger"
      ],
      "belt": {
        "material": "Black leather",
        "buckle": "Rectangular gold/metallic frame"
      },
      "tech": {
        "item": "Smartphone (iPhone style)",
        "case_color": "Black",
        "holding_style": "Held vertically in front of face with right hand"
      },
      "beauty_details": {
        "nails": "Short, painted bright red"
      }
    },
    "pose_and_framing": {
      "type": "Mirror selfie",
      "posture": "Standing, slight hip tilt (contrapposto), midriff exposed",
      "framing": "Thigh-up shot, portrait orientation"
    },
    "setting_and_lighting": {
      "location": "Indoors (likely a bedroom or hallway)",
      "background_elements": {
        "left": "Dark window with blinds, glimpse of bed/furniture with white clutter",
        "right": "White door frame/jamb, plain wall"
      },
      "lighting": {
        "quality": "Warm, directional artificial light",
        "source": "Coming from the right side",
        "shadows": "Casts shadows on the left side of the torso and background"
      }
    }
  }
}
```
