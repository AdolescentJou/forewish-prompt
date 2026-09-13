# Camp Planner

## 说明

用途概述：{ "research_config": { "topic": "Logistics-Oriented and Car-Free Camping Planning Analysis", "target_persona": { "age_group": "${age_group:30-35}", "group_size"
中文概述：AI 输出无车露营规划分析，涵盖公共交通接驳、选址与精简装备清单。
关键词：露营规划、公共交通、无车出行、营地选址、planning

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：yigitdemiralp06@gmail.com
- 类型：结构化(JSON/模版)（原始类型 STRUCTURED）
- 面向开发者：否

## Prompt 内容

```text
{
  "research_config": {
    "topic": "Logistics-Oriented and Car-Free Camping Planning Analysis",
    "target_persona": {
      "age_group": "${age_group:30-35}",
      "group_size": "${group_size:4}",
      "travel_mode": "Intermodal Transportation (Public Transit + Hiking/Walking Only)"
    },
    "output_lang": "${lang:English}"
  },
  "context": {
    "origin": "${origin:Ankara Yenimahalle}",
    "destination_region": "${destination:Nallihan}",
    "specific_date": "${date:March 14, 2026}",
    "priorities": [
      "Logistical feasibility",
      "Safety",
      "Nature immersion",
      "Minimalism/Ultralight approach"
    ]
  },
  "knowledge_base_requirements": {
    "transport_analysis": [
      "Main artery bus/train lines and specific stop locations",
      "First/Last Mile connectivity (Local shuttles, taxi availability, or trekking distance from the final stop)",
      "Weekend frequency and ticketing/payment methods (e.g., local transit cards vs. cash)"
    ],
    "site_selection_criteria": [
      "Accessibility: Max 5km hiking distance from public transit drop-off points",
      "Legality: Officially designated campsites or safe, legal wild camping zones",
      "Resource Availability: Proximity to water sources and basic necessities (WC/Market)"
    ]
  },
  "goal": {
    "primary_objective": "To create a sustainable, comfortable, and safe camping plan without a private vehicle.",
    "specific_research_tasks": [
      "Identify 3 distinct campsite typologies (e.g., lakeside, forest, high altitude) in the region.",
      "Curate a gear and meal list considering a strict backpack weight limit (max 15-18kg).",
      "Calculate distances to the nearest settlement and medical facilities for emergency protocols.",
      "Construct a precise timeline for a Saturday morning departure and Sunday evening return."
    ]
  },
  "output_structure": {
    "format": "Strategic Research Report",
    "sections": [
      "1. Transportation & Logistics Matrix",
      "2. Campsite Options (with Pros/Cons Analysis)",
      "3. Gear & Meal Planning (Ultralight & Practical)",
      "4. Step-by-Step Weekend Timeline (Chronological)",
      "5. Safety Protocols & Local Insider Tips"
    ],
    "tone": "Analytical, instructional, safe and encouraging"
  }
}
```
