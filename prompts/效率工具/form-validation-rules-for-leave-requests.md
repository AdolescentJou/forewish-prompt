# Form Validation Rules for Leave Requests

## 说明

用途概述：{ "rules": [ { "leaveType": "Evlilik İzni", "validity": "Personelin evlenmesi halinde 3 iş günü şeklinde kullandırılır.
中文概述：提供土耳其语请假表单验证规则 JSON：婚假、产假、亲属丧假、自然灾害等类型及最大天数
关键词：表单验证、leave request、JSON、请假规则、土耳其

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：[@muhtesemozgur9](https://github.com/muhtesemozgur9)
- 类型：结构化(JSON/模版)（原始类型 STRUCTURED）
- 面向开发者：否

## Prompt 内容

```text
{
  "rules": [
    {
      "leaveType": "Evlilik İzni",
      "validity": "Personelin evlenmesi halinde 3 iş günü şeklinde kullandırılır.",
      "maxDays": 3
    },
    {
      "leaveType": "Doğum İzni (Eş)",
      "validity": "Personelin eşinin doğum yapması halinde 5 iş günü",
      "maxDays": 5
    },
    {
      "leaveType": "I.Derece Yakın Ölümü İçin İzin",
      "validity": "Personelin ana, baba, kardeş, eş ve çocuklarının ölümü halinde 3 iş günü",
      "maxDays": 3
    },
    {
      "leaveType": "Doğal Afet",
      "validity": "Doğal afet olması halinde 10 iş gününe kadar kullanılan izindir.",
      "maxDays": 10
    },
    {
      "leaveType": "Ücretli Doğum İzni",
      "validity": "Gebelik ve analık halinde Kanunu’na göre islem yapılır. Kadın personelin dogumdan önce 8 hafta ve dogumdan sonra 8 hafta olmak üzere çalıstırılmamaları esastır. Çogul gebelik halinde dogumdan önce çalıstırılmayacak 8 haftalık süreye iki hafta süre eklenir.",
      "preBirthWeeks": 8,
      "postBirthWeeks": 8,
      "extraWeeksForMultiplePregnancy": 2,
      "workUntilPreWeeks": 3
    },
    {
      "leaveType": "Ücretsiz Doğum İzni",
      "validity": "Ücretli doğum izninin bitmesi durumunda çalışanın talebi üzerine 6 aya kadar verilen izindir. Parçalar halinde kullanılamaz.",
      "maxMonths": 6
    },
    {
      "leaveType": "Hamile Çalışan Sağlık Kontrol İzni",
      "validity": "Hamile çalışanın hamileliğini belgelemesi durumunda aylık kontrollerinde kullanılabilen ve gün kısıtı bulunmayan izin türüdür.",
      "documentationRequired": true
    },
    {
      "leaveType": "Sosyal Mazeret İzni",
      "validity": "Çalışanın bir yılda kullanabilecegi mazeret izni toplam 3 iş günüdür. 3 günü aşan izinler yıllık izinden düşürülür.",
      "maxDaysPerYear": 3
    },
    {
      "leaveType": "Ücretsiz İzin",
      "validity": "Çalışanın yazılı talebi üzerine işverenin uygun görmesi durumunda kısıtı bulunmayan izin türüdür.",
      "documentationRequired": true
    }
  ],
  "generalRules": {
    "duplicateCheck": "Daha önce aynı tarihler içinde bir izin talebi varsa kullanıcının tekrar izin talep etmemeli.",
    "applicableFormId": 1
  }
}
```
