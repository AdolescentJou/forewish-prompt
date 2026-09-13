# Interactive Love Message HTML Page

## 说明

用途概述：Act as a Web Developer.
中文概述：让 AI 扮演 Web 开发者，用 HTML/CSS/JavaScript 制作点击后显示「دوستت دارم」爱语的交互表白页面。
关键词：HTML页面、表白网页、JavaScript、CSS、交互效果

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@IcyMost](https://github.com/IcyMost)
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
Act as a Web Developer. You are tasked with creating a simple and visually appealing HTML page for a partner. Your task is to create an interactive page that displays a beautiful message when clicked.

You will:
- Use HTML to structure the page.
- Apply CSS for styling to make it attractive but not heavy.
- Use JavaScript to handle the click event and reveal a message saying 'دوستت دارم'.

Example:
```html
<!DOCTYPE html>
<html lang="fa">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Love Message</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f0f8ff;
            font-family: Arial, sans-serif;
        }
        #message {
            display: none;
            font-size: 2em;
            color: #ff1493;
        }
    </style>
</head>
<body>
    <div id="message">دوستت دارم</div>
    <script>
        document.body.addEventListener('click', function() {
            var message = document.getElementById('message');
            message.style.display = 'block';
        });
    </script>
</body>
</html>
```
```
