# flaneur

## 说明

用途概述：Act as an expert travel planner.
中文概述：让 AI 按预算、交通与兴趣规划详细行程：概览、逐日安排、住宿与必做清单
关键词：旅行规划、行程安排、预算、自由行、itinerary

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：kennynah85@gmail.com
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
Act as an expert travel planner. Help me plan a detailed trip with the following criteria. 



**Trip Basics**

- **Destination**: 

- **Dates**: 

- **Travelers**: 2 seniors, 1 adult

- **Trip style**: ${family}



**Budget & Logistics**

- **Total budget**: $${amount} for everything, or $${amount}/day per person. Include flights.

- **Currency to use**: [SGD/USD/etc]

- **Accommodation preference**: [Hotel, Airbnb, Hostel, Resort, 4-star+]. Area to stay in if any: [___]

- **Transport**: [Public transport only, Rent a car, Mix, Rideshare/Grab, Walking]



**Interests & Constraints**

- **Must-dos**: ${please_recommend}

- **Interests**: [Food, Museums, Nature, Shopping, History]

- **Avoid**: ${hiking}

- **Pace**: ${flexible}



**Output Format I Want:**

1. **Overview**: Best time to go, weather for my dates, any local events/holidays to know.

2. **Day-by-day itinerary**: Morning / Afternoon / Evening, with travel time between spots. Include 1 backup indoor option per day.

3. **Food**: 2-3 local dishes to try + 5 restaurant/cafe recs at different price points.

4. **Budget breakdown**: Flights, lodging, food, transport, activities, total + buffer.

5. **Logistics**: Visa requirements for ${passport_nationality}, SIM/eSIM, airport to city transport, tipping norms, safety tips.

6. **Packing list**: Tailored to weather + activities.

7. **Booking timeline**: What to book now vs later.



Make it realistic for travel from ${singapore}. Keep transit times honest and don’t pack days too tightly.
```
