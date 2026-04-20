import sqlite3
import pandas as pd

database = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 13 (SQL using Python - II)\Lesson 6 (Query with Subquery)\ACP (Answer with Subquery)\basketball.sqlite"

try:
    conn = sqlite3.connect(database)
    print("Opened database successfully\n")

    print("--- Tables in Database ---")
    tables = pd.read_sql("SELECT * FROM sqlite_master WHERE type='table';", conn)
    print(tables)
    print("\n" + "="*50 + "\n")

    print("--- Team Table (Analysis) ---")
    team_df = pd.read_sql("SELECT * FROM Team LIMIT 5;", conn)
    print(team_df)
    print("\n" + "="*50 + "\n")

    print("--- Team_Attributes Table (Analysis) ---")
    attr_df = pd.read_sql("SELECT * FROM Team_Attributes LIMIT 5;", conn)
    print(attr_df)
    print("\n" + "="*50 + "\n")

    subquery_query = """
        SELECT * FROM Team_Attributes 
        WHERE ID IN (
            SELECT id 
            FROM Team 
            WHERE state = 'New York'
        );
    """
    
    ny_team_attributes = pd.read_sql(subquery_query, conn)
    print("--- Team Attributes for New York State Teams ---")
    print(ny_team_attributes)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if 'conn' in locals():
        conn.close()
        print("\nDatabase connection closed.")