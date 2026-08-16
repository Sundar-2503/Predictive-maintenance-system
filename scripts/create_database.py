import sqlite3
import pandas as pd
from pathlib import Path
BASE_DIR=Path(__file__).resolve().parent.parent
DB_PATH=BASE_DIR/"database"/"maintanence.db"
connection=sqlite3.connect(DB_PATH)
# df.to_sql(
#     "machine_data",
#     connection,
#     if_exists="replace",
#     index=False
# )
# connection.close
# print("DB created")