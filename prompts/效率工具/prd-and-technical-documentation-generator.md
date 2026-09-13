# prd-and-technical-documentation-generator

## 说明

用途概述：--- name: prd-and-technical-documentation-generator description: A skill for generating comprehensive Product Requirements Documents (PRDs) and technical documentation for projects.
中文概述：扮演文档生成 skill，为产品/功能撰写完整 PRD 与配套技术文档：定义产品、收集需求、含问题陈述、目标与范围
关键词：PRD、技术文档、需求文档、产品文档、skill

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@tcyjg](https://github.com/tcyjg)
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
---
name: prd-and-technical-documentation-generator
description: A skill for generating comprehensive Product Requirements Documents (PRDs) and technical documentation for projects.
---

# PRD and Technical Documentation Generator

This skill is designed to assist in the creation of detailed Product Requirements Documents (PRDs) and accompanying technical documentation.

## Instructions

1. **Define the Product or Feature**: Clearly specify the product or feature for which the documentation is being created.
2. **Gather Requirements**: Identify and list all necessary requirements, including functional and non-functional aspects.
3. **Structure the PRD**:
   - **Introduction**: Provide a brief overview of the product or feature.
   - **Problem Statement**: Describe the problem the product or feature aims to solve.
   - **Objectives**: Outline the main goals and objectives.
   - **Scope**: Define the scope, including what is included and excluded.
   - **Requirements**: Detail functional and non-functional requirements.
   - **User Stories**: Include user stories to illustrate usage scenarios.
4. **Technical Documentation**:
   - **Architecture Overview**: Provide an architectural diagram and description.
   - **Technical Specifications**: Detail the technical requirements and specifications.
   - **APIs and Interfaces**: List APIs and interfaces, including usage and examples.
   - **Security and Compliance**: Outline security measures and compliance requirements.

## Examples

- **Example Input**: "Create a PRD for a new e-commerce platform feature"
- **Example Output**: A structured document with all sections populated with relevant information.

## Variables

- ${productFeature} - The specific product feature or initiative.
- ${documentType:PRD} - Type of document to generate (PRD or Technical).

Utilize this skill to efficiently produce comprehensive documentation that supports project objectives and stakeholder needs.
```
