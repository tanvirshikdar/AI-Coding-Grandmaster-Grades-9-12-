import sqlite3
import pandas as pd

database = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 13 (SQL using Python - II)\Lesson 1 (Welcome to SQLite using Python)\ACP (Connect to SQLite database)\basketball.sqlite"

try:
    conn = sqlite3.connect(database)
    print("Opened database successfully")

    query = """
            SELECT * FROM sqlite_master 
            WHERE type='table';
            """

    tables_df = pd.read_sql(query, conn)

    print("\nTables present in the database:")
    if tables_df.empty:
        print("The database is currently empty (no tables found).")
    else:
        print(tables_df)

except Exception as e:
    print(f"An error occurred while connecting: {e}")

finally:
    if 'conn' in locals():
        conn.close()
        print("\nDatabase connection closed.")