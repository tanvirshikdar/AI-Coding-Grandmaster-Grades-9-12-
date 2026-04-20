import sqlite3
import pandas as pd

database = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 13 (SQL using Python - II)\Lesson 2 (Basic SQL statements)\Activity 2 (Play with Tables)\database.sqlite"

try:
    conn = sqlite3.connect(database)
    print("Opened data successfully\n")

    tables = pd.read_sql("""SELECT * FROM sqlite_master WHERE type='table';""", conn)
    print("--- Tables in Database ---")
    print(tables)
    print("\n" + "="*50 + "\n")

    teams = pd.read_sql("""SELECT * FROM Team;""", conn)
    print("--- All Teams ---")
    print(teams)
    print("\n" + "="*50 + "\n")

    matches = pd.read_sql("""SELECT * FROM Match;""", conn)
    print("--- Matches Table (First 5 Rows) ---")
    print(matches.head()) 
    print("\n" + "="*50 + "\n")

    MI_wins = pd.read_sql("""SELECT * FROM Match WHERE Match_Winner == 7;""", conn)
    print("--- Mumbai Indians Wins ---")
    print(MI_wins)
    print("\n" + "="*50 + "\n")

    MI_S8_S9 = pd.read_sql("""SELECT * FROM Match WHERE Match_Winner == 7 AND Season_Id IN (8,9);""", conn)
    print("--- MI Wins (Seasons 8 & 9) ---")
    print(MI_S8_S9)
    print("\n" + "="*50 + "\n")

    new_teams = pd.read_sql("""SELECT * FROM Team WHERE Team_Name LIKE 'De%';""", conn)
    print("--- Teams starting with 'De' ---")
    print(new_teams)
    print("\n" + "="*50 + "\n")

    min_max_margin = pd.read_sql("""SELECT MIN(Win_Margin), MAX(Win_Margin) FROM Match;""", conn)
    print("--- Min and Max Win Margin ---")
    print(min_max_margin)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if 'conn' in locals():
        conn.close()
        print("\nDatabase connection closed.")