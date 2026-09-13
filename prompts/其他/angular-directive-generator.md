# Angular Directive Generator

## 说明

用途概述：You are an expert Angular developer.
中文概述：让 AI 按描述生成 Angular 17+ 指令，含装饰器、绑定与用法示例
关键词：Angular、指令生成、TypeScript、前端开发、代码生成

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：satishbirhade16@gmail.com
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
You are an expert Angular developer. Generate a complete Angular directive based on the following description:

Directive Description: ${description}
Directive Type: [structural | attribute]
Selector Name: [e.g. appHighlight, *appIf]
Inputs needed: [list any @Input() properties]
Target element behavior: ${what_should_happen_to_the_host_element}

Generate:
1. The full directive TypeScript class with proper decorators
2. Any required imports
3. Host bindings or listeners if needed
4. A usage example in a template
5. A brief explanation of how it works

Use Angular 17+ standalone directive syntax. Follow Angular style guide conventions.
```
