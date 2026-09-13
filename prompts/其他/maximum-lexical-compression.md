# Maximum Lexical Compression

## 说明

用途概述：Rewrite my text with maximal lexicalization (maximum lexical compression): For every phrase, sentence, or paragraph that has an established equivalent term, ter
中文概述：文本改写指令：对每段可用既有词或术语表达的内容做最大词汇压缩，全部替换为单词/术语并去掉冗长解释。
关键词：文本改写、词汇压缩、术语化、rewrite、简洁

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：omidzamani2@gmail.com
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
Rewrite my text with maximal lexicalization (maximum lexical compression):
For every phrase, sentence, or paragraph that has an established equivalent term,
term of art, or single word, remove it and replace it with just that word/term.
Do not keep any explanation in long form if it can be expressed with a single word.

INPUT:
${paste_your_text_here}
```
