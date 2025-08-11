---
title: Checklists
toc: true
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

## Arriving at Boat
```js
const arriving = options.sql`SELECT * FROM Arriving_on_Boat_Checklist`;
await arriving;
Inputs.table(arriving,{rows:20})
```

## Preparing to Sail
```js
const prep = options.sql`SELECT * FROM Preparing_to_Sail_Checklist`;
await prep;
Inputs.table(prep,{rows:20})
```

## After Sailing
```js
const after = options.sql`SELECT * FROM After_Sailing_Checklist`;
await after;
Inputs.table(after,{rows:20})
```

## Leaving Boat
```js
const leaving = options.sql`SELECT * FROM Leaving_Boat_Checklist`;
await leaving;
Inputs.table(leaving,{rows:20})
```

## Laying Up

```js
const layingup = options.sql`SELECT * FROM Laying_Up_Checklist`;
await layingup;
Inputs.table(layingup,{rows:20})
```

## Storm Prep

```js
const storm = options.sql`SELECT * FROM Storm_Checklist___in_addition_to_Leaving_Boat_Checklist__`;
await storm;
Inputs.table(layingup,{rows:20})
```
