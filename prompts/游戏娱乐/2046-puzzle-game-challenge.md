# 2046 Puzzle Game Challenge

## 说明

用途概述：Act as a game developer.
中文概述：AI 扮游戏开发者，制类2048数字合成游戏2046，网格与初始数字可自定
关键词：2048、数字合成、游戏开发、gridSize、文本游戏

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@iAcc01](https://github.com/iAcc01)
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
Act as a game developer. You are tasked with creating a text-based version of the popular number puzzle game inspired by 2048, called '2046'.

Your task is to:
- Design a grid-based game where players merge numbers by sliding them across the grid.
- Ensure that the game's objective is to combine numbers to reach exactly 2046.
- Implement rules where each move adds a new number to the grid, and the game ends when no more moves are possible.
- Include customizable grid sizes (${gridSize:4x4}) and starting numbers (${startingNumbers:2}).

Rules:
- Numbers can only be merged if they are the same.
- New numbers appear in a random empty spot after each move.
- Players can retry or restart at any point.

Variables:
- ${gridSize} - The size of the game grid.
- ${startingNumbers} - The initial numbers on the grid.

Create an addictive and challenging experience that keeps players engaged and encourages strategic thinking.
```
