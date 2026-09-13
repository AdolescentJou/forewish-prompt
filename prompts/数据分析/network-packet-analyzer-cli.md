# Network Packet Analyzer CLI

## 说明

用途概述：Create a command-line network packet analyzer in C using libpcap.
中文概述：用 C 与 libpcap 编写命令行网络抓包分析器：抓包过滤、TCP/UDP/DNS 协议解析、流量统计、PCAP/CSV 导出与可疑告警。
关键词：网络分析、libpcap、C语言、packet capture、协议解析、CLI

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@f](https://github.com/f)
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
Create a command-line network packet analyzer in C using libpcap. Implement packet capture from network interfaces with filtering options. Add protocol analysis for common protocols (TCP, UDP, HTTP, DNS, etc.). Include traffic statistics with bandwidth usage and connection counts. Implement packet decoding with detailed header information. Add export functionality in PCAP and CSV formats. Include alert system for suspicious traffic patterns. Implement connection tracking with state information. Add geolocation lookup for IP addresses. Include command-line arguments for all options with sensible defaults. Implement color-coded output for better readability.
```
