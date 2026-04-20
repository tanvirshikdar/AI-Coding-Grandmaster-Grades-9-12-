import sqlite3
import pandas as pd

database = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 13 (SQL using Python - II)\Lesson 3 (SQL Statements – Part 2)\ACP (Answer the Query)\basketball.sqlite"

try:
    conn = sqlite3.connect(database)
    print("Opened database successfully\n")

    tables = pd.read_sql("""
        SELECT * FROM sqlite_master 
        WHERE type='table';
    """, conn)
    print("--- Tables in Database ---")
    print(tables)
    print("\n" + "="*50 + "\n")

    team_table = pd.read_sql("""
        SELECT * FROM Team;
    """, conn)
    print("--- Team Table (First 5 Rows) ---")
    print(team_table.head())
    print("\n" + "="*50 + "\n")

    top_drafts = pd.read_sql("""
        SELECT idTeam, COUNT(DISTINCT idPlayer) AS Total_Players_Drafted
        FROM Draft
        GROUP BY idTeam
        ORDER BY Total_Players_Drafted DESC
        LIMIT 10;
    """, conn)
    print("--- Top 10 Teams that Drafted the Most Players ---")
    print(top_drafts)

except Exception as e:
    print(f"An error occurred: {e}")
    print("\n*Tip: If it says a column like 'idTeam' or 'idPlayer' doesn't exist, check the exact column names of your Draft table and update the query!*")

finally:
    if 'conn' in locals():
        conn.close()
        print("\nDatabase connection closed.")