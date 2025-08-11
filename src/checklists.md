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
```

```js
const master_list = collection.file("Master_List.db").sqlite();
await master_list;
```

## Arriving at Boat


```js
const arriving = master_list.sql`SELECT Area, Task, "Check" FROM Checklist WHERE Arriving_On_Boat = 'Y' ORDER BY Area, Task`;
await arriving;
```

```js
Inputs.table(arriving,{rows:24})
```

## Preparing to Sail

```js
const prep = master_list.sql`SELECT Area, Task, "Check" FROM Checklist WHERE Preparing_to_Sail = 'Y' ORDER BY Area, Task`;
await prep;
```

```js
Inputs.table(prep,{rows:24})
```

## After Sailing

```js
const after =  master_list.sql`SELECT Area, Task, "Check" FROM Checklist WHERE After_Sailing = 'Y' ORDER BY Area, Task`;
await after;
```

```js
Inputs.table(after,{rows:24})
```

## Leaving Boat


```js
const leaving = master_list.sql`SELECT Area, Task, "Check" FROM Checklist WHERE Leaving_Boat = 'Y' ORDER BY Area, Task`;
await leaving;
```

```js
Inputs.table(leaving,{rows:24})
```

## Laying Up


```js
const layingup = master_list.sql`SELECT Area, Task, "Check" FROM Checklist WHERE Laying_Up = 'Y' ORDER BY Area, Task`;
await layingup;
```

```js
Inputs.table(layingup,{rows:24})
```

## Storm Prep

```js
const storm = master_list.sql`SELECT Area, Task, "Check" FROM Checklist WHERE Storm_Prep___Marina = 'Y' ORDER BY Area, Task`;
await storm;
```

```js
Inputs.table(storm,{rows:24})
```
