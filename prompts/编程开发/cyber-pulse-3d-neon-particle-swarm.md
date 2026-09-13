# Cyber-Pulse: 3D Neon Particle Swarm

## 说明

用途概述：Game Concept: A fast-paced arcade "dodge-em-up" set in a digital void.
中文概述：让 AI 用 Three.js 构建 15000 粒子、带辉光与鼠标斥力交互的赛博霓虹粒子游戏场景
关键词：Three.js、粒子系统、3D、游戏开发、shader

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@loshu2000](https://github.com/loshu2000)
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：是

## Prompt 内容

```text
Game Concept: A fast-paced arcade "dodge-em-up" set in a digital void. The player controls a core energy spark, navigating through a fluid-like nebula of 10,000+ blue and purple particles that react to the player's presence.
Technical Prompt:
Create a Three.js scene featuring a Points system with 15,000 particles. Use a custom ShaderMaterial for a glow effect. Implement a repulsion logic where particles fly away from the mouse cursor.

JavaScript
// Core repulsion math
let dist = particlePos.distanceTo(mousePos);
if (dist < 5) {
  direction.subVectors(particlePos, mousePos).normalize();
  particlePos.addScaledVector(direction, 0.2);
}
Include a BloomPass for post-processing and ensure 60FPS performance via
```
