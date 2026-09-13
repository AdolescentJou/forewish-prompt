# Omniroute bulk input key converter (cf)

## 说明

用途概述：Ask me for input data in next chat message.
中文概述：将 * 用户名 '编号' key '编号' 的多行格式转换为 用户名|编号|编号 管道分隔格式并在代码框输出
关键词：文本转换、格式转换、key converter、批量处理、管道分隔

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：sxlderek@gmail.com
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
Ask me for input data in next chat message.
I want you to format lines in this pattern

* derekstates70 ''1111111'' key ''2222222''
* jennyho666 ''3333333'' key ''4444444''

into this format

derekstates70|1111111|2222222
jennyho666|3333333|4444444

output the result in a code box
```
