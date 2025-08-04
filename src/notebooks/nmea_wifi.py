import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    import sqlite3

    # Read sqlite query results into a pandas DataFrame
    con = sqlite3.connect("data/systems/NMEA_Wifi_Options/Sheet_1.sqlite")
    df = pd.read_sql_query("SELECT * from Sheet_1", con)

    # Verify that result of SQL query is stored in the dataframe
    print(df.head())

    con.close()
    return


if __name__ == "__main__":
    app.run()
