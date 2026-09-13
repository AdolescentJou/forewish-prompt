# 3D Kinetic Ball Simulation

## 说明

用途概述：I want you to act as an expert front-end game engineer specializing in single-file HTML5 games.
中文概述：用 p5.js 单文件 HTML5 实现倾斜控制弹球与粒子的 3D 动能弹跳竞技场
关键词：p5.js、HTML5游戏、3D物理、单文件、合成波风

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@loshu2000](https://github.com/loshu2000)
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
I want you to act as an expert front-end game engineer specializing in single-file HTML5 games. Your task is to produce a SINGLE FILE (index.html) implementation of a 3D Kinetic Bounce Arena.

GAME SPEC:

Title: Kinetic Bounce Arena

Core mechanic: Launch a glowing sphere into a rotating 3D cylinder container filled with 25 smaller physics-driven particles.

Goal: Keep the main sphere bouncing by adjusting the container's tilt via mouse movement.

TECH REQUIREMENTS:

Single file: <!doctype html> with inline <style> and <script> using p5.js (loaded via CDN).

Rendering: WebGL mode in p5.js, 600x600 canvas centered on page.

Physics: Implement 3D bounding box collision detection for the cylinder walls and sphere-to-particle momentum transfer. Particles must leave fading colorful motion trails.

Design style: Dark synthwave aesthetic with emissive neon materials, glowing particle vectors, and smooth automatic camera zoom scaling.
```
