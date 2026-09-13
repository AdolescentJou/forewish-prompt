# Gravity Shift: Low-Poly Physics Platformer

## 说明

用途概述：Game Concept: A puzzle-platformer named "Gravity Shift" where players rotate the entire world to navigate a 3D low-poly labyrinth.
中文概述：技术构建提示：用 Three.js+Cannon.js 做 3D 低多边形物理平台跳跃游戏，按 R 旋转重力向量并以 Lerp 平滑相机
关键词：Three.js、Cannon.js、平台跳跃、游戏物理、重力旋转

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@loshu2000](https://github.com/loshu2000)
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：是

## Prompt 内容

```text
Game Concept: A puzzle-platformer named "Gravity Shift" where players rotate the entire world to navigate a 3D low-poly labyrinth. The environment is minimalist, using pastel gradients and sharp geometric shapes.
Technical Prompt:
Build a 3D platformer using Three.js and Cannon.js. The world is a cube-shaped maze. When the user presses 'R', rotate the world.gravity vector by 90 degrees.

JavaScript
// Gravity rotation logic
world.gravity.set(0, -9.82, 0); // Default
function rotateGravity() {
  let newG = new CANNON.Vec3(-world.gravity.y, world.gravity.x, 0);
  world.gravity.copy(newG);
}
Include smooth camera interpolation using Lerp to follow the player's rigid body during shifts.
```
