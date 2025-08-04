/// marimo-embed
    height: 400px
    mode: run

```python(marimo)
@app.cell
def __():
    import pandas as pd
    import sqlite3
    
    # Read sqlite query results into a pandas DataFrame
    con = sqlite3.connect("data/systems/NMEA_Wifi_Options/Sheet_1.sqlite")
    df = pd.read_sql_query("SELECT * from Sheet_1", con)
    
    # Verify that result of SQL query is stored in the dataframe
    print(df.head())
    
    con.close()
    return
```
///