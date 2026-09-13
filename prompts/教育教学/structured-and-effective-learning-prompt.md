# Structured and Effective Learning Prompt

## 说明

用途概述：${subject}= ${current_level}= ${time_available}= ${learning_style}= ${goal}= Step 1: Knowledge Assessment 1.
中文概述：分四步产出学习方案：知识评估与技能树、路径与时间表、资源清单、练习框架。
关键词：skill tree、学习路径、resource curation、学习规划、时间安排

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@kenicodes](https://github.com/kenicodes)
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
${subject}=
${current_level}=
${time_available}=
${learning_style}=
${goal}=

Step 1: Knowledge Assessment
1. Break down ${subject} into core components
2. Evaluate complexity levels of each component
3. Map prerequisites and dependencies
4. Identify foundational concepts
Output detailed skill tree and learning hierarchy

~ Step 2: Learning Path Design
1. Create progression milestones based on ${current_level}
2. Structure topics in optimal learning sequence
3. Estimate time requirements per topic
4. Align with ${time_available} constraints
Output structured learning roadmap with timeframes

~ Step 3: Resource Curation
1. Identify learning materials matching ${learning_style}:
   - Video courses
   - Books/articles
   - Interactive exercises
   - Practice projects
2. Rank resources by effectiveness
3. Create resource playlist
Output comprehensive resource list with priority order

~ Step 4: Practice Framework
1. Design exercises for each topic
2. Create real-world application scenarios
3. Develop progress checkpoints
4. Structure review intervals
Output practice plan with spaced repetition schedule

~ Step 5: Progress Tracking System
1. Define measurable progress indicators
2. Create assessment criteria
3. Design feedback loops
4. Establish milestone completion metrics
Output progress tracking template and benchmarks

~ Step 6: Study Schedule Generation
1. Break down learning into daily/weekly tasks
2. Incorporate rest and review periods
3. Add checkpoint assessments
4. Balance theory and practice
Output detailed study schedule aligned with ${time_available}
```
