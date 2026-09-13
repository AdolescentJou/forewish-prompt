# Cyber Security Character Workflow

## 说明

用途概述：{ "name": "Cyber Security Character", "steps": [ { "step_1": "Facial Identity Mapping", "description": "Maintain 100% facial consistency based on the provided reference photos.
中文概述：让 AI 按步骤生成赛博朋克网络安全角色图，保持面部一致并叠加战术装束与金色义体细节
关键词：图像生成、赛博朋克、角色设计、面部一致性、品牌元素

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@TRojen610](https://github.com/TRojen610)
- 类型：结构化(JSON/模版)（原始类型 STRUCTURED）
- 面向开发者：否

## Prompt 内容

```text
{
  "name": "Cyber Security Character",
  "steps": [
    {
      "step_1": "Facial Identity Mapping",
      "description": "Maintain 100% facial consistency based on the provided reference photos. Features: medium-length wavy red hair and a composed, visionary tech-innovator expression."
    },
    {
      "step_2": "Tactical Gear & Branding",
      "description": "Outfit the subject in a sleek red tactical jacket with intricate gold circuitry textures. Correctly integrate the '${Brand}' name and the specific '${Brand First Letter}' logo emblem onto the chest piece."
    },
    {
      "step_3": "Cybernetic Enhancement",
      "description": "Apply subtle, minimalist gold-accented cybernetic interface patterns onto the skin of the face, ensuring they blend naturally with the {Style:Cyberpunk} aesthetic."
    },
    {
      "step_4": "Environmental Integration",
      "description": "Design a background featuring the ${Country} flag merged with glowing golden digital circuits. Include a distant cinematic futuristic skyline of a ${Country} metropolis (${Style:Cyberpunk} ${City})."
    },
    {
      "step_5": "Lighting & Cinematic Render",
      "description": "Utilize warm, dramatic side lighting from the right to cast a soft silhouette onto the background. Render in 4K ultra-realistic quality with hyper-detailed textures."
    }
  ]
}
```
