# Table in PDF to CSV conversion

## 说明

用途概述："Attached is an image of a table listing the model parameters for the ${insert_model_name} model (from [Insert Author/Paper Name]).
中文概述：把图片中的论文参数表格提取为可存 CSV 代码块：首行表头、合并单元格补值、含逗号字段加引号
关键词：PDF、CSV、表格提取、data-extraction、单元格合并

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@Bornduck](https://github.com/Bornduck)
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
"Attached is an image of a table listing the model parameters for the ${insert_model_name} model (from [Insert Author/Paper Name]).
Please extract the data and convert it into a CSV code block that I can copy and save directly.
Requirements:
Use the first row as the header.
If cells are merged, repeat the value for each row to ensure the CSV is flat and processable.
Do not include units in the numeric columns (e.g., remove 'ms' or '%'), or keep them consistent in a separate column.
If any text is unclear due to image quality, mark it as '${unclear}' rather than guessing.
Ensure all fields containing commas are properly quoted."
```
