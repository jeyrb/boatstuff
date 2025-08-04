---
title: Integrating NMEA with Wifi
---

# Integration Options for NMEA and Wifi

## Background

Table of options built in mid-2025 to upgrade a Bavaria Cruiser 36 with both an **NMEA 2000** and **NMEA 0183** network. Any prices and supplier info will be UK based.

## Options

```js
const workbook = FileAttachment("./data/NMEA_Wifi_Options.xlsx").xlsx();
```

```js 
const data = workbook.sheet("Sheet 1", {headers: true});
```


```js
Inputs.table(data)
```
