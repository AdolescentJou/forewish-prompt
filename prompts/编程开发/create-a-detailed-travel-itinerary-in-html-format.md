# Create a detailed travel itinerary in HTML format

## 说明

用途概述：<!DOCTYPE html> <html> <head> <title>Travel Itinerary: Nanjing to Changchun</title> <style> body { font-family: Arial, sans-serif; } .
中文概述：让 AI 生成南京至长春旅行的详细 HTML 行程页面，含日期、航班、酒店与每日安排
关键词：旅行行程、HTML、南京、长春、网页生成

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@flyp1028](https://github.com/flyp1028)
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
<!DOCTYPE html>
<html>
<head>
    <title>Travel Itinerary: Nanjing to Changchun</title>
    <style>
        body { font-family: Arial, sans-serif; }
        .itinerary { margin: 20px; }
        .day { margin-bottom: 20px; }
        .header { font-size: 24px; font-weight: bold; }
        .sub-header { font-size: 18px; font-weight: bold; }
    </style>
</head>
<body>
    <div class="itinerary">
        <div class="header">Travel Itinerary: Nanjing to Changchun</div>
        <div class="sub-header">Dates: ${startDate} to ${endDate}</div>
        <div class="sub-header">Budget: ${budget} RMB</div>

        <div class="day">
            <div class="sub-header">Day 1: Arrival in Changchun</div>
            <p><strong>Flight:</strong> ${flightDetails}</p>
            <p><strong>Hotel:</strong> ${hotelName} - Located in city center, comfortable and affordable</p>
            <p><strong>Weather:</strong> ${weatherForecast}</p>
            <p><strong>Packing Tips:</strong> ${packingRecommendations}</p>
        </div>

        <div class="day">
            <div class="sub-header">Day 2: Exploring Changchun</div>
            <p><strong>Attractions:</strong> ${attraction1} (Ticket: ${ticketPrice1}, Open: ${openTime1})</p>
            <p><strong>Lunch:</strong> Try local cuisine at ${restaurant1}</p>
            <p><strong>Afternoon:</strong> Visit ${attraction2} (Ticket: ${ticketPrice2}, Open: ${openTime2})</p>
            <p><strong>Dinner:</strong> Enjoy a meal at ${restaurant2}</p>
            <p><strong>Transportation:</strong> ${transportDetails}</p>
        </div>

        <!-- Repeat similar blocks for Day 3, Day 4, etc. -->
        
        <div class="day">
            <div class="sub-header">Day 5: Departure</div>
            <p><strong>Return Flight:</strong> ${returnFlightDetails}</p>
        </div>

    </div>
</body>
</html>
```
