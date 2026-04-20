import pandas as pd
import sqlite3

database = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 13 (SQL using Python - II)\Lesson 6 (Query with Subquery)\Activity 2 (Query Inside Query)\database.sqlite"

try:
    conn = sqlite3.connect(database)
    print("Opened database successfully\n")

    print("--- Tables in Database ---")
    tables = pd.read_sql("SELECT * FROM sqlite_master WHERE type='table';", conn)
    print(tables)
    print("\n" + "="*50 + "\n")

    team = pd.read_sql("SELECT * FROM Team", conn)
    print("--- Team Table ---")
    print(team.head())
    print("\n" + "="*50 + "\n")

    csk_matches_2015 = pd.read_sql("""SELECT Match_Id, Team_2 as Away_Team, Toss_Winner, Match_Winner
                                    FROM Match 
                                    WHERE Team_1 = 
                                    (SELECT Team_1
                                    FROM Match
                                    WHERE Team_1 == 3 AND Season_Id == 8 LIMIT 1)""", conn)
    print("Matches Played By Chennai Super Kings (Home) in Year 2015:")
    print(csk_matches_2015.head())
    print("\n" + "="*50 + "\n")

    match_runs = pd.read_sql("""SELECT Match_Id, Runs_Scored as Total_Runs, Innings_No
                                FROM Batsman_Scored
                                WHERE Runs_Scored > 5 AND Match_Id IN  
                                (SELECT Match_Id
                                FROM Match
                                WHERE Season_Id == 8)""", conn)
    print("Matches with Scored Runs Greater Than 5 in Year 2015:")
    print(match_runs.head())
    print("\n" + "="*50 + "\n")

    avg_runs = pd.read_sql("""SELECT Match_Id, Runs_Scored as Total_Runs, Innings_No
                                FROM Batsman_Scored
                                WHERE Innings_No == 1 AND Runs_Scored > 
                                (SELECT AVG(Runs_Scored)
                                FROM Batsman_Scored)""", conn)
    print("Matches with Scored Runs Greater Than Average Scored Runs:")
    print(avg_runs.head())

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if 'conn' in locals():
        conn.close()
        print("\nDatabase connection closed.")