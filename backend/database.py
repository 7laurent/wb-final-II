import pandas as pd
import sqlite3

# Read CSV
df = pd.read_csv(
    "data/unemployment.csv/unemployment.csv",
    skiprows=4
)

# Connexion SQLite
conn = sqlite3.connect("data/unemployment.db")

# Save in SQLite
df.to_sql(
    "unemployment",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Database created successfully!")