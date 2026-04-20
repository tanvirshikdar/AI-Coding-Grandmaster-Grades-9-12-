import sqlite3
import pandas as pd

database = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 13 (SQL using Python - II)\Lesson 4 (SQL Constraints)\Activity 1 (Let’s Create a Table0\database.sqlite"

try:
    conn = sqlite3.connect(database)
    print("Opened database successfully")

    conn.execute('''CREATE TABLE IF NOT EXISTS CLASS_10
             (SNO INT PRIMARY KEY NOT NULL,
             Roll_No INT NOT NULL,
             Name TEXT NOT NULL,
             AGE INT DEFAULT (15),
             GENDER TEXT NOT NULL,
             Email_ID TEXT NOT NULL,
             Contact_No REAL NOT NULL);''')

    print("Table created successfully")

    try:
        conn.execute("INSERT INTO CLASS_10 (SNO,Roll_No,NAME,AGE,Gender,Email_ID,Contact_No) \
              VALUES (1, 1, 'Allen', 14, 'Male', 'allen@gmail.com', 8080900 )")

        conn.execute("INSERT INTO CLASS_10 (SNO,Roll_No,NAME,AGE,Gender,Email_ID,Contact_No) \
              VALUES (2, 2, 'Aisha', 14, 'Female', 'aish@gmail.com', 9080900 )")

        conn.execute("INSERT INTO CLASS_10 (SNO,Roll_No,NAME,AGE,Gender,Email_ID,Contact_No) \
              VALUES (3, 3, 'Jeff', 15, 'Male', 'jeff@gmail.com', 9900900 )")
        
        conn.commit()
        print("Records created successfully")
    except sqlite3.IntegrityError:
        print("Records already exist, skipping insertion.")

    print("\n--- Current Data in CLASS_10 ---")
    df = pd.read_sql("SELECT * FROM CLASS_10;", conn)
    print(df)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if 'conn' in locals():
        conn.close()
        print("\nConnection closed.")