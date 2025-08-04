---
title: Options to Integrate NMEA and Wifi
toc: false
---

# NMEA to Wifi Integration

```js
import SQLite from "npm:@observablehq/sqlite";
```

```js
const collection = FileAttachment("data/nmea_wifi.zip").zip();
```

```js
const options = collection.file("Products.db").sqlite();
```

```js
const products = options.sql`SELECT * FROM Products`;
await products;
```

## Products

```js
const search = view(Inputs.search(products, {placeholder: "Search products ..."}));
```
```js
Inputs.table(search,{})
```