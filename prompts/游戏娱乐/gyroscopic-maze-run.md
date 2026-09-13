# Gyroscopic Maze Run

## 说明

用途概述：I want you to act as a master game designer specializing in mobile-responsive physics simulation.
中文概述：AI 扮游戏设计师，制单文件HTML迷宫：滚珠、双轴重力、2D Canvas
关键词：迷宫游戏、physics、2D Canvas、重力操控、单文件游戏

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@loshu2000](https://github.com/loshu2000)
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
I want you to act as a master game designer specializing in mobile-responsive physics simulation. Create a SINGLE FILE (index.html) interactive maze game.

GAME SPEC:

Title: Axial Drift

Core mechanic: A marble rolls inside a complex geometric maze. The player shifts the global gravity vector (X and Y axes) to guide the marble.

Goal: Maneuver the marble to the center vector vortex while dodging dynamic kinetic trapdoors.

TECH REQUIREMENTS:

Single file: Pure web technology stack (<!doctype html>, CSS, JS) without heavy engine frameworks.

Rendering: 2D Canvas optimized for mobile and desktop viewports, scaling pixel-perfectly.

Mechanics: Accept desktop mouse click-drags or mobile device orientation API (DeviceOrientationEvent) to tilt the maze physics grid. Implement rigid-body friction, angular velocity, and momentum damping for the marble.

Design style: Bauhaus architectural aesthetics. High contrast bold solid primary color blocks, heavy black stroke lines, and real-time drop shadows.
```
