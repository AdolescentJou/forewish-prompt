# Draw a Person Using Alphabet Letters

## 说明

用途概述：The following prompt tests an LLM's capabilities to handle visual concepts, despite being trained only on text. This is a challenging task for the LLM so it involves several iterations. In the example below the user first requests for a desired visual and then provides feedback along with corrections and additions. The follow up instructions will depend on the progress the LLM makes on the task. Note that this task is asking to generate TikZ code which will then need to manually compiled by the user.
中文概述：教学示例：让 LLM 用 TikZ 绘制字母拼成的人物并多轮迭代修正
关键词：TikZ、字母拼图、教学示例、多轮迭代

## 元信息（仓库提供）

- 来源仓库：[dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)
- 贡献者：DAIR.AI
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

Prompt Iteration 1:
```markdown
Produce TikZ code that draws a person composed from letters in the alphabet. The arms and torso can be the letter Y, the face can be the letter O (add some facial features) and the legs can be the legs of the letter H. Feel free to add other features.
```  

Prompt Iteration 2:
```markdown
The torso is a bit too long, the arms are too short and it looks like the right arm is carrying the face instead of the face being right above the torso. Could you correct this please?
```

Prompt Iteration 3:
```markdown
Please add a shirt and pants.
```

## 参考链接

- [Sparks of Artificial General Intelligence: Early experiments with GPT-4](https://arxiv.org/abs/2303.12712) (13 April 2023)
