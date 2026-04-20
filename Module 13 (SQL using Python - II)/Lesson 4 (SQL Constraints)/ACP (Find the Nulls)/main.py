import sqlite3
import pandas as pd

database = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 13 (SQL using Python - II)\Lesson 4 (SQL Constraints)\ACP (Find the Nulls)\basketball.sqlite"

try:
    conn = sqlite3.connect(database)
    print("Opened database successfully\n")

    tables = pd.read_sql("SELECT * FROM sqlite_master WHERE type='table';", conn)
    print("--- Tables in Database ---")
    print(tables)
    print("\n" + "="*50 + "\n")

    print("--- Rows with NULL nameOrganizationFrom in Draft table ---")
    null_orgs = pd.read_sql("SELECT * FROM Draft WHERE nameOrganizationFrom IS NULL;", conn)
    print(null_orgs)
    print("\n" + "="*50 + "\n")

    print("--- 5 Earliest Founded Teams ---")
    earliest_teams = pd.read_sql("SELECT * FROM Team ORDER BY year_founded ASC LIMIT 5;", conn)
    print(earliest_teams)
    print("\n" + "="*50 + "\n")

    print("--- 5 Latest Founded Teams ---")
    latest_teams = pd.read_sql("SELECT * FROM Team ORDER BY year_founded DESC LIMIT 5;", conn)
    print(latest_teams)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if 'conn' in locals():
        conn.close()
        print("\nDatabase connection closed.")