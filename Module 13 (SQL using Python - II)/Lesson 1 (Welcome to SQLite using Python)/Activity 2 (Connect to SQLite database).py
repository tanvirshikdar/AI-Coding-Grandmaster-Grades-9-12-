import sqlite3
import pandas as pd

database = 'database.sqlite'

try:
    conn = sqlite3.connect(database)
    print('Opened data successfully')

    query = "SELECT * FROM sqlite_master WHERE type='table';"
    tables = pd.read_sql(query, conn)
    
    print("\nTables found in database:")
    print(tables)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if 'conn' in locals():
        conn.close()