import sqlite3
import pandas as pd

database = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 13 (SQL using Python - II)\Lesson 5 (Joins in SQL)\ACP (Let’s Join the Tables)\basketball.sqlite"

try:
    conn = sqlite3.connect(database)
    print("Opened database successfully\n")

    tables = pd.read_sql("SELECT * FROM sqlite_master WHERE type='table';", conn)
    print("--- Tables in Database ---")
    print(tables)
    print("\n" + "="*50 + "\n")

    player_table = pd.read_sql("SELECT * FROM Player LIMIT 5;", conn)
    print("--- Player Table (First 5 Rows) ---")
    print(player_table)
    print("\n" + "="*50 + "\n")

    salary_table = pd.read_sql("SELECT * FROM Player_Salary LIMIT 5;", conn)
    print("--- Player_Salary Table (First 5 Rows) ---")
    print(salary_table)
    print("\n" + "="*50 + "\n")

    join_query = """
        SELECT DISTINCT s.nameTeam, s.namePlayer, s.value, p.is_active
        FROM Player_Salary s
        INNER JOIN Player p ON s.namePlayer = p.full_name
    """
    
    joined_data = pd.read_sql(join_query, conn)
    print("--- Joined Player and Salary Data (Distinct Teams) ---")
    print(joined_data.head(10))

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if 'conn' in locals():
        conn.close()
        print("\nDatabase connection closed.")