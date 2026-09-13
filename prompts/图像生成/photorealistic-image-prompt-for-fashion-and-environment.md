# Photorealistic Image Prompt for Fashion and Environment

## 说明

用途概述：{ "image_prompt": { "subject": { "type": "Adult woman (21+) matching the reference image identity", "appearance": "Fair skin, long dark messy hair with subtle r
中文概述：按参考人像生成写真 prompt:成年女性穿土耳其国家队球衣、举手撩发直视镜头的中景
关键词：图像生成、写真、球衣、环境人像、参考图

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：dorukkurtoglu@gmail.com
- 类型：结构化(JSON/模版)（原始类型 STRUCTURED）
- 面向开发者：否

## Prompt 内容

```text
{
  "image_prompt": {
    "subject": {
      "type": "Adult woman (21+) matching the reference image identity",
      "appearance": "Fair skin, long dark messy hair with subtle red highlights, nose piercing",
      "expression": "Relaxed, looking directly at the camera, mouth slightly open",
      "pose": "Medium shot; both arms raised; hands running through hair; elbows pointing outward; confident, casual posture"
    },
    "outfit": {
      "clothing": "Türkiye (Turkish) national football team jersey",
      "details": "Official-style Türkiye national team jersey (home kit look): deep red base with subtle tonal fabric patterning, clean white accents, crew neck collar. Include a white Nike swoosh on the right chest and the Türkiye crest (TFF badge with crescent and star) on the left chest. No club crest, no club sponsor logos, no 'Standard Chartered', no 'Expedia'. Fabric looks like modern performance polyester, slightly textured, natural wrinkles from movement.",
      "accessories": "Black hair tie on wrist"
    },
    "environment": {
      "location": "Inside a boat or yacht, positioned near a window frame",
      "background": "Bright blue ocean under sunny sky; distant rocky coastline and cliffs visible through the window; the window frame is visible and helps ground the scene as shot from inside the boat"
    },
    "lighting": {
      "type": "Natural sunlight, bright daylight",
      "shadows": "Hard, realistic sun shadows; crisp highlights on skin and jersey; realistic specular sheen on hair; no studio light reflections"
    },
    "camera": {
      "capture_device": "Smartphone or consumer camera",
      "framing": "Medium shot (torso and head clearly visible), centered composition",
      "angle": "Eye-level",
      "focus": "Sharp focus on face and jersey details; background slightly softer but recognizable",
      "look": "Mild natural softness, not over-sharpened; realistic handheld feel without motion blur"
    },
    "style": {
      "aesthetic": "Candid Instagram influencer style, photorealistic, ultra-detailed, high resolution, 8K look",
      "skin_rendering": "Natural skin texture and pores visible, no plastic smoothing, no heavy retouching",
      "color": "True-to-life daylight color, no cinematic teal-orange grading, no artificial filters",
      "quality": "Clean, crisp, natural photography, realistic fabric behavior and stitching"
    },
    "negative_prompt": "club logos, Liverpool crest, Nike club kit sponsor logos, Standard Chartered text, Expedia text, fashion campaign studio lighting, ring light catchlights, over-posed model stance, plastic skin, overly smoothed face, anime, illustration, CGI, artificial background, text watermark, misspelled logos, distorted crest, extra limbs, warped hands, unrealistic anatomy, extreme HDR, cinematic color grading"
  }
}
```
