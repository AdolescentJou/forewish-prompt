# Closed Domain Question Answering with LLMs

## 说明

用途概述：The following prompt tests an LLM's capabilities to answer closed-domain questions which involves answering questions belonging a specific topic or domain. <Callout type="warning" emoji="⚠️"> Note that due to the challenging nature of the task, LLMs are likely to hallucinate when they have no knowledge regarding the question. </Callout>
中文概述：封闭领域问答测试：要求LLM仅依据给定患者信息改写为医学记录，检验其不越界虚构的能力。
关键词：封闭域问答、医学记录、hallucination、信息约束、LLM测试

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

Please rewrite the data above into a medical note, using exclusively the information above.
```

## 参考链接

- [Sparks of Artificial General Intelligence: Early experiments with GPT-4](https://arxiv.org/abs/2303.12712) (13 April 2023)
