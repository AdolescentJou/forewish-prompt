# Pitchside Tunnel Moment with Your Favorite Footballer

## 说明

用途概述：Inputs Reference 1: User’s uploaded photo Reference 2: ${Footballer Name} Jersey Number: ${Jersey Number} Jersey Team Name: ${Jersey Team Name} (team of the jer
中文概述：生成用户照片与球星在主场场边合影的写实图像提示，含球衣道具与主场氛围设定
关键词：图像生成、足球、写实照片、球迷、人像

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@semihkislar](https://github.com/semihkislar)、[@f](https://github.com/f)
- 类型：图像生成（原始类型 IMAGE）
- 面向开发者：否

## Prompt 内容

```text
Inputs

Reference 1: User’s uploaded photo

Reference 2: ${Footballer Name}

Jersey Number: ${Jersey Number}
Jersey Team Name: ${Jersey Team Name} (team of the jersey being held)
User Outfit: ${User Outfit Description}
Mood: ${Mood}

Prompt
Create a photorealistic image of the person from the user’s uploaded photo standing next to ${Footballer Name} pitchside in front of the stadium stands, posing for a photo.

Location: Pitchside/touchline in a large stadium. Natural grass and advertising boards look realistic.

Stands: The background stands must feel 100% like ${Footballer Name}’s team home crowd (single-team atmosphere). Dominant team colors, scarves, flags, and banners. No rival-team colors or mixed sections visible.

Composition: Both subjects centered, shoulder to shoulder. ${Footballer Name} can place one arm around the user.

Prop: They are holding a jersey together toward the camera. The back of the jersey must clearly show ${Footballer Name} and the number ${Jersey Number}. Print alignment is clean, sharp, and realistic.

Critical rule (lock the held jersey to a specific team)

The jersey they are holding must be an official kit design of ${Jersey Team Name}.

Keep the jersey colors, patterns, and overall design consistent with ${Jersey Team Name}.

If the kit normally includes a crest and sponsor, place them naturally and realistically (no distorted logos or random text).

Prevent color drift: the jersey’s primary and secondary colors must stay true to ${Jersey Team Name}’s known colors.

Note: ${Jersey Team Name} must not be the club ${Footballer Name} currently plays for.

Clothing:

${Footballer Name}: Wearing his current team’s match kit (shirt, shorts, socks), looks natural and accurate.

User: ${User Outfit Description}

Camera: Eye level, 35mm, slight wide angle, natural depth of field. Focus on the two people, background slightly blurred.

Lighting: Stadium lighting + daylight (or evening match lights), realistic shadows, natural skin tones.

Faces: Keep the user’s face and identity faithful to the uploaded reference. ${Footballer Name} is clearly recognizable. Expression: ${Mood}

Quality: Ultra realistic, natural skin texture and fabric texture, high resolution.

Negative prompts
Wrong team colors on the held jersey, random or broken logos/text, unreadable name/number, extra limbs/fingers, facial distortion, watermark, heavy blur, duplicated crowd faces, oversharpening.

Output
Single image, 3:2 landscape or 1:1 square, high resolution.
```
