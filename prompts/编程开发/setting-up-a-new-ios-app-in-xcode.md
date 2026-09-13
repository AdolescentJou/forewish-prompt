# Setting Up a New iOS App in Xcode

## 说明

用途概述：You are setting up a new iOS app project in Xcode.
中文概述：让 AI 按严格默认在 Xcode 中新建仅支持竖屏 iPhone 的 iOS 应用项目
关键词：iOS、Xcode、iPhone、工程配置、Info.plist

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@ilkerulusoy](https://github.com/ilkerulusoy)
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
You are setting up a new iOS app project in Xcode.

Goal
Create a clean iPhone-only app with strict defaults.

Project settings
- Minimum iOS Deployment Target: 26.0
- Supported Platforms: iPhone only
- Mac support: Mac (Designed for iPhone) enabled
- iPad support: disabled

Orientation
- Default orientation: Portrait only
- Set “Supported interface orientations (iPhone)” to Portrait only
- Verify Build Settings or Info.plist includes only:
  - UISupportedInterfaceOrientations = UIInterfaceOrientationPortrait

Security and compliance
- Info.plist: App Uses Non-Exempt Encryption (ITSAppUsesNonExemptEncryption) = NO

Output
Confirm each item above and list where you set it in Xcode (Target, General, Build Settings, Info.plist).
```
