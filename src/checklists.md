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

```

## Arriving at Boat
```js
const arriving_sheet = collection.file("Arriving.db ").sqlite();
const arriving = arriving_sheet.sql`SELECT * FROM Arriving_on_Boat_Checklist`;
await arriving;
```

```js
Inputs.table(arriving,{rows:20})
```

## Preparing to Sail
```js
const prep_sheet = collection.file("Preparing_to_Sail.db").sqlite();
const prep = prep_sheet.sql`SELECT * FROM Preparing_to_Sail_Checklist`;
await prep;
```

```js
Inputs.table(prep,{rows:20})
```

## After Sailing
```js
const after_sheet = collection.file("After_Sailing.db").sqlite();
const after = after_sheet.sql`SELECT * FROM After_Sailing_Checklist`;
await after;
```

```js
Inputs.table(after,{rows:20})
```

## Leaving Boat
```js
const leaving_sheet = collection.file("Leaving_Boat.db").sqlite();
await leaving_sheet;
const leaving = leaving_sheet.sql`SELECT * FROM Leaving_Boat_Checklist`;
await leaving;
```

```js
Inputs.table(leaving,{rows:20})
```

## Laying Up

```js
const layingup_sheet = collection.file("Laying_Up.db").sqlite();
const layingup = layingup_sheet.sql`SELECT * FROM Laying_Up_Checklist`;
await layingup;
```

```js
Inputs.table(layingup,{rows:20})
```

## Storm Prep

```js
const storm_sheet = collection.file("Storm.db").sqlite();
await storm_sheet;
const storm = storm_sheet.sql`SELECT * FROM Storm_Checklist___in_addition_to_Leaving_Boat_Checklist__`;
await storm;
```

```js
Inputs.table(storm,{rows:20})
```
