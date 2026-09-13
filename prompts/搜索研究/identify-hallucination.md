# Identify Hallucination in LLM Responses

## 说明

用途概述：The following prompt tests an LLM's capabilities to identify hallucination in the context of [closed-domain question answering](/question-answering/closed-domain). Bubeck et al. (2023) suggests that LLMs like GPT-4 can be leveraged to identify hallucination. <Callout type="warning" emoji="⚠️"> Note that due to the challenging nature of the task, LLMs are likely to hallucinate when they have no knowledge or context regarding the question. </Callout> The prompt has been slightly modified to include indicators that show which sections of the prompt corresponds to what information.
中文概述：AI 在闭域问答场景判断模型回复中是否出现超出给定信息的幻觉，如病历改写示例。
关键词：幻觉识别、hallucination、闭域问答、事实性、LLM评估

## 元信息（仓库提供）

- 来源仓库：[dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)
- 贡献者：DAIR.AI
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```markdown
Patient’s facts:
- 20 year old female
- with a history of anerxia nervosa and depression
- blood pressure 100/50, pulse 50, height 5’5’’
- referred by her nutrionist but is in denial of her illness
- reports eating fine but is severely underweight

Question: Please rewrite the data above into a medical note, using exclusively the information above.

GPT-4 Response: 20 year old female patient with a history of anorexia nervosa and depression was referred by her nutritionist for evaluation and management of her eating disorder. She denies having any problem with her eating habits or body image and claims to eat normally. However, she is severely underweight for her height (BMI 16.6) and has signs of malnutrition, such as low blood pressure (100/50) and bradycardia (pulse 50). She also reports feeling depressed and hopeless. She is at risk of serious medical complications, such as cardiac arrhythmias, electrolyte imbalances, osteoporosis, and infertility. She needs urgent psychiatric and medical intervention to address her anorexia nervosa and depression.

Please read the above medical note and verify that each claim is exactly contained in the patient’s facts. Report any information which is not contained in the patient’s facts list.
```

## 参考链接

- [Sparks of Artificial General Intelligence: Early experiments with GPT-4](https://arxiv.org/abs/2303.12712) (13 April 2023)
