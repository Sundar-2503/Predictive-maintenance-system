import sqlite3
import pandas as pd
df=pd.read_csv("E:/New folder/predictive-maintenance-system/data/ai4i2020.csv")
connection=sqlite3.connect("database/maintanence.db")
df.to_sql(
    "machine_data",
    connection,
    if_exists="replace",
    index=False
)
connection.close
print("DB created")