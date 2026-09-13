# Personalized Technical Intelligence Briefing for Edge AI in Defense

## 说明

用途概述：{ "opening": "${bibleVerse}", "criticalIntelligence": [ { "headline": "${headline1}", "source": "${sourceLink1}", "technicalSummary": "${technicalSummary1}", "r
中文概述：生成 JSON 格式国防 Edge AI 技术情报简报：关键情报条目（含技术摘要/相关度/行动洞察）、技术深潜与优先情报目标。
关键词：Edge AI、国防、情报简报、JSON格式、技术情报

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：ezekielmitchll@gmail.com
- 类型：结构化(JSON/模版)（原始类型 STRUCTURED）
- 面向开发者：否

## Prompt 内容

```text
{
  "opening": "${bibleVerse}",
  "criticalIntelligence": [
    {
      "headline": "${headline1}",
      "source": "${sourceLink1}",
      "technicalSummary": "${technicalSummary1}",
      "relevanceScore": "${relevanceScore1}",
      "actionableInsight": "${actionableInsight1}"
    },
    {
      "headline": "${headline2}",
      "source": "${sourceLink2}",
      "technicalSummary": "${technicalSummary2}",
      "relevanceScore": "${relevanceScore2}",
      "actionableInsight": "${actionableInsight2}"
    },
    // Add up to 8 total items
  ],
  "technicalDeepDive": [
    {
      "breakthroughItem": "${breakthrough1}",
      "implementationDetails": "${implementationDetails1}"
    },
    {
      "breakthroughItem": "${breakthrough2}",
      "implementationDetails": "${implementationDetails2}"
    }
    // Add up to 3 items
  ],
  "priorityIntelligenceTargets": {
    "primary": [
      "False positive reduction methodologies",
      "Edge AI optimization for resource-constrained hardware",
      "Real-time inference benchmarks"
    ],
    "secondary": [
      "Defense procurement announcements",
      "SBIR/STTR opportunities",
      "Counter-UAS technologies"
    ],
    "tertiary": [
      "PyTorch/OpenCV updates",
      "Rust embedded frameworks",
      "Military robotics contracts"
    ]
  },
  "sourcesToPrioritize": [
    "arXiv (cs.CV, cs.RO, cs.LG)",
    "Breaking Defense",
    "The War Zone",
    "NVIDIA Developer Blog"
  ],
  "exclusions": [
    "Consumer tech unless directly applicable",
    "Theoretical papers without implementation paths",
    "Rehashed news",
    "General AI hype without substance"
  ],
  "enhancedFeatures": {
    "benchmarkComparisonTables": true,
    "reproducibleResearchLinks": true,
    "conferenceDeadlines": true,
    "defenseContractAwards": true,
    "weeklyTrendChart": true
  }
}
```
