import pandas as pd
import sqlite3

database = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 13 (SQL using Python - II)\Lesson 5 (Joins in SQL)\Activity 1 (Let’s Join the Tables)\database.sqlite"

try:
    conn = sqlite3.connect(database)
    print("Opened database successfully\n")

    print("--- Tables in Database ---")
    tables = pd.read_sql("SELECT * FROM sqlite_master WHERE type='table'", conn)
    print(tables)
    print("\n" + "="*50 + "\n")

    print("--- Inner Join (Country & City) ---")
    joined_city = pd.read_sql("""SELECT c.Country_Id, c.Country_Name, ci.City_Name
                                FROM country c
                                INNER JOIN city ci
                                ON c.Country_Id == ci.Country_id""", conn)
    print(joined_city.head())
    print("\n" + "="*50 + "\n")

    print("--- Left Join (Player & Season) ---")
    joined_left = pd.read_sql("""SELECT *
                                FROM player
                                LEFT JOIN season
                                ON player.Player_Id == season.Man_of_the_Series""", conn)
    print(joined_left.head())
    print("\n" + "="*50 + "\n")

    print("--- Cross Join (Country & City) ---")
    joined_cross = pd.read_sql("""SELECT c.Country_Id, c.Country_Name, ci.City_Name
                                FROM country c
                                CROSS JOIN city ci""", conn)
    print(joined_cross.head())
    print("\n" + "="*50 + "\n")

    print("--- Union Clause (Players & Teams) ---")
    union = pd.read_sql("""SELECT Player_Name 
                          FROM player
                          UNION
                          SELECT Team_Name
                          FROM team""", conn)
    print(union.head())

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if 'conn' in locals():
        conn.close()
        print("\nDatabase connection closed.")