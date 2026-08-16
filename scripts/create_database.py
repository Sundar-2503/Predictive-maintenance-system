import sqlite3
import pandas as pd
from pathlib import Path
BASE_DIR=Path(__file__).resolve().parent.parent
df=pd.read_csv(BASE_DIR/"data"/"ai4i2020.csv")
connection=sqlite3.connect("database/maintanence.db")
df.to_sql(
    "machine_data",
    connection,
    if_exists="replace",
    index=False
)
connection.close
print("DB created")