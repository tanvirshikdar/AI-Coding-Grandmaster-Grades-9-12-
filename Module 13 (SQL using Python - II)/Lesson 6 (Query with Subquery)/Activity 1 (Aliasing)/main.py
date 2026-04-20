import pandas as pd
import sqlite3

database = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 13 (SQL using Python - II)\Lesson 6 (Query with Subquery)\Activity 1 (Aliasing)\database.sqlite"

try:
    conn = sqlite3.connect(database)
    print("Opened database successfully\n")

    print("--- Tables in Database ---")
    tables = pd.read_sql("""SELECT * FROM sqlite_master WHERE type='table';""", conn)
    print(tables)
    print("\n" + "="*50 + "\n")

    query = '''SELECT Season_Id, Match_Id,  
               v.Venue_Name, c.City_Name, t.Team_Name AS Winner 
               FROM Match
               INNER JOIN Venue AS v ON Match.Venue_Id == v.Venue_Id
               INNER JOIN City AS c ON v.City_Id == c.City_Id
               INNER JOIN Team AS t ON Match.Match_Winner == t.Team_Id;'''

    match_details = pd.read_sql(query, conn)
    
    print("--- Match Details with Aliasing ---")
    print(match_details.head())

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if 'conn' in locals():
        conn.close()
        print("\nDatabase connection closed.")