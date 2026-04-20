import sqlite3
import pandas as pd

database = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 13 (SQL using Python - II)\Lesson 3 (SQL Statements – Part 2)\Activity 1 (Play with Tables - Part 2)\database.sqlite"

try:
    conn = sqlite3.connect(database)
    print("Opened data successfully\n")

    tables = pd.read_sql("""
        SELECT * FROM sqlite_master 
        WHERE type='table';
    """, conn)
    print("--- Tables in Database ---")
    print(tables)
    print("\n" + "="*50 + "\n")

    matches = pd.read_sql("""
        SELECT * FROM Match;
    """, conn)
    print("--- Matches Table (First 5 Rows) ---")
    print(matches.head())
    print("\n" + "="*50 + "\n")

    result1 = pd.read_sql("""
        SELECT AVG(Win_Margin), Match_Winner 
        FROM Match 
        WHERE Season_Id == 9 
        GROUP BY Match_Winner 
        ORDER BY AVG(Win_Margin);
    """, conn)
    print("--- Average Win Margin by Team (Season 9) ---")
    print(result1)
    print("\n" + "="*50 + "\n")

    result2 = pd.read_sql("""
        SELECT COUNT(DISTINCT Venue_Id) AS Total_Venues
        FROM Match 
        WHERE Season_Id == 9;
    """, conn)
    print("--- Total Unique Venues (Season 9) ---")
    print(result2)
    print("\n" + "="*50 + "\n")

    result3 = pd.read_sql("""
        SELECT MIN(Win_Margin), MAX(Win_Margin), AVG(Win_Margin), COUNT(DISTINCT Man_of_the_Match) 
        FROM Match;
    """, conn)
    print("--- Min/Max/Avg Margin & Total Unique MOTM ---")
    print(result3)
    print("\n" + "="*50 + "\n")

    result4 = pd.read_sql("""
        SELECT SUM(Win_Margin) AS Sum_Win_Margin
        FROM Match 
        WHERE Season_Id == 9;
    """, conn)
    print("--- Sum of Win Margins (Season 9) ---")
    print(result4)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if 'conn' in locals():
        conn.close()
        print("\nDatabase connection closed.")