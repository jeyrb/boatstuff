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
await collection;
const master_list = collection.file("Master_List.db");
await master_list;
```

## Arriving at Boat


```js
const arriving = master_list.sql`SELECT * FROM Checklist WHERE Arriving_On_Boat = 'Y'`;
await arriving;
```

```js
Inputs.table(arriving,{rows:20})
```

## Preparing to Sail

```js
const prep = master_list.sql`SELECT * FROM Checklist WHERE Preparing_to_Sail = 'Y'`;
await prep;
```

```js
Inputs.table(prep,{rows:20})
```

## After Sailing

```js
const after =  master_list.sql`SELECT * FROM Checklist WHERE After_Sailing = 'Y'`;
await after;
```

```js
Inputs.table(after,{rows:20})
```

## Leaving Boat


```js
const leaving = master_list.sql`SELECT * FROM Checklist WHERE Leaving_Boat = 'Y'`;
await leaving;
```

```js
Inputs.table(leaving,{rows:20})
```

## Laying Up


```js
const layingup = master_list.sql`SELECT * FROM Checklist WHERE Laying_Up = 'Y'`;
await layingup;
```

```js
Inputs.table(layingup,{rows:20})
```

## Storm Prep

```js
const storm = master_list.sql`SELECT * FROM Checklist WHERE Storm_Prep___Marina = 'Y'`;
await storm;
```

```js
Inputs.table(storm,{rows:20})
```
