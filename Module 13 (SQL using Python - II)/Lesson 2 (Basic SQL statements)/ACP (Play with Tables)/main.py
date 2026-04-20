import sqlite3
import pandas as pd

database = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 13 (SQL using Python - II)\Lesson 2 (Basic SQL statements)\ACP (Play with Tables)\basketball.sqlite"

try:
    conn = sqlite3.connect(database)
    print("Opened database successfully\n")

    tables = pd.read_sql("""SELECT * FROM sqlite_master WHERE type='table';""", conn)
    print("--- Tables in Database ---")
    print(tables)
    print("\n" + "="*50 + "\n")

    teams_table = pd.read_sql("""SELECT * FROM Team;""", conn)
    print("--- Team Table (First 5 Rows) ---")
    print(teams_table.head())
    print("\n" + "="*50 + "\n")

    after_1990 = pd.read_sql("""
        SELECT full_name, nickname, city, year_founded 
        FROM Team 
        WHERE year_founded > 1990;
    """, conn)
    print("--- Teams Founded After 1990 ---")
    print(after_1990)
    print("\n" + "="*50 + "\n")

    tx_ny_teams = pd.read_sql("""
        SELECT * FROM Team 
        WHERE state IN ('Texas', 'New York');
    """, conn)
    print("--- Teams in Texas and New York ---")
    print(tx_ny_teams)
    print("\n" + "="*50 + "\n")

    los_teams = pd.read_sql("""
        SELECT * FROM Team 
        WHERE city LIKE 'Los%';
    """, conn)
    print("--- Teams Starting with 'Los' ---")
    print(los_teams)
    print("\n" + "="*50 + "\n")

    min_max_teams = pd.read_sql("""
        SELECT full_name, year_founded 
        FROM Team 
        WHERE year_founded = (SELECT MIN(year_founded) FROM Team)
           OR year_founded = (SELECT MAX(year_founded) FROM Team);
    """, conn)
    print("--- Earliest and Latest Founded Teams ---")
    print(min_max_teams)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if 'conn' in locals():
        conn.close()
        print("\nDatabase connection closed.")