import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

file_path = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 14 (Welcome to Data Science)\Lesson 6 (Capstone Project)\ACP (Capstone Project)\dataset.csv"

try:
    df = pd.read_csv(file_path)
    print("File loaded successfully!")

    print("\n--- First Three Rows ---")
    print(df.head(3))
    print("\n--- Last Three Rows ---")
    print(df.tail(3))

    print("\n--- Dataset Info ---")
    df.info()

    print("\n--- Null Values Count ---")
    print(df.isnull().sum())

    subset = df.iloc[41:76]
    print("\n--- Subset (Rows 41 to 75) ---")
    print(subset)

    highest_votes = df.loc[df['No_of_Votes'].idxmax()]
    print("\n--- Movie with Highest Votes ---")
    print(highest_votes)

    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    sns.boxplot(y=df['IMDB_Rating'], color='skyblue')
    plt.title('Boxplot of IMDB Rating')

    plt.subplot(1, 2, 2)
    if df['Runtime'].dtype == 'object':
        df['Runtime'] = df['Runtime'].str.extract('(\d+)').astype(float)
    
    sns.boxplot(y=df['Runtime'], color='salmon')
    plt.title('Boxplot of Runtime (in mins)')
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.scatter(df['Runtime'], df['IMDB_Rating'], alpha=0.5, color='teal')
    plt.xlabel('Runtime (minutes)')
    plt.ylabel('IMDB Rating')
    plt.title('Relationship: Runtime vs IMDB Rating')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    sns.histplot(df['IMDB_Rating'], kde=True, color='green')
    plt.title('Distribution of IMDB Rating')

    plt.subplot(1, 2, 2)
    sns.histplot(df['Runtime'], kde=True, color='orange')
    plt.title('Distribution of Runtime')
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(12, 6))
    cert_col = 'Certificate' if 'Certificate' in df.columns else 'Rating'
    sns.countplot(data=df, x=cert_col, palette='viridis', order=df[cert_col].value_counts().index)
    plt.title(f'Number of Movies per {cert_col}')
    plt.xticks(rotation=45)
    plt.show()

except FileNotFoundError:
    print(f"Error: Could not find the file at {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")