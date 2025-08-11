---
title: Checklists
toc: false
---

# Checklists

```js
import SQLite from "npm:@observablehq/sqlite";
```

```js
const collection = FileAttachment("data/checklists.zip").zip();
```

```js
const options = collection.file("Laying_Up.db").sqlite();
```

```js
const layingup = options.sql`SELECT * FROM Laying_Up_Checklist`;
await layingup;
```

## Laying Up

```js
Inputs.table(layingup,{rows:20})
```
