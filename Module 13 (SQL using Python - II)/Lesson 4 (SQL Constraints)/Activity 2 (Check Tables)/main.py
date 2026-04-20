import pandas as pd
import sqlite3

database = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 13 (SQL using Python - II)\Lesson 4 (SQL Constraints)\Activity 2 (Check Tables)\database.sqlite"

try:
    conn = sqlite3.connect(database)
    print('Opened database successfully\n')

    print("--- Tables in Database ---")
    df_tables = pd.read_sql("""SELECT * FROM sqlite_master WHERE type='table';""", conn)
    print(df_tables)
    print("\n" + "="*50 + "\n")

    print("--- Player_Match Table (Head) ---")
    player_match = pd.read_sql("""SELECT * FROM Player_Match""", conn)
    print(player_match.head())
    print("\n" + "="*50 + "\n")

    print("--- Rows in Player_Match where Team_Id is NULL ---")
    null_player_match = pd.read_sql("""SELECT * FROM Player_Match WHERE Team_Id IS NULL""", conn)
    if null_player_match.empty:
        print("No NULL values found in Team_Id.")
    else:
        print(null_player_match)
    print("\n" + "="*50 + "\n")

    print("--- Match Table (Head) ---")
    match_data = pd.read_sql("""SELECT * FROM Match""", conn)
    print(match_data.head())
    print("\n" + "="*50 + "\n")

    print("--- Rows in Match where Match_Winner is NULL ---")
    null_match = pd.read_sql("""SELECT * FROM Match WHERE Match_Winner IS NULL""", conn)
    if null_match.empty:
        print("No NULL values found in Match_Winner.")
    else:
        print(null_match)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if 'conn' in locals():
        conn.close()
        print("\nDatabase connection closed.")