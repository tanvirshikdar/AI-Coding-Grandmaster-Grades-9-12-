import sqlite3
import pandas as pd

database = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 13 (SQL using Python - II)\Lesson 2 (Basic SQL statements)\Activity 1 (Let’s Analyze Tables)\database.sqlite"

try:
    conn = sqlite3.connect(database)
    print('Opened data successfully\n')

    tables_query = """SELECT * FROM sqlite_master
                      WHERE type='table';"""
                      
    tables = pd.read_sql(tables_query, conn)
    
    print("--- Tables in Database ---")
    print(tables)
    print("\n")

    match_query = """SELECT *
                     FROM Match;"""
                     
    matches = pd.read_sql(match_query, conn)

    print("--- Match Table Info ---")
    matches.info()

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if 'conn' in locals():
        conn.close()
        print("\nConnection closed.")