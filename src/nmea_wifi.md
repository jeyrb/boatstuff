---
title: Options to Integrate NMEA and Wifi
toc: false
---

# NMEA to Wifi Integration


```js
const collection = FileAttachment("data/nmea_wifi.zip").zip();
```

```js
const options = collection.file("Sheet_1.db").sqlite();
```

```js
const products = options.sql`SELECT * FROM Table_1`;
await products;
```

## Products

```js
const search = view(Inputs.search(products, {placeholder: "Search products ..."}));
```
```js
Inputs.table(search,{})
```