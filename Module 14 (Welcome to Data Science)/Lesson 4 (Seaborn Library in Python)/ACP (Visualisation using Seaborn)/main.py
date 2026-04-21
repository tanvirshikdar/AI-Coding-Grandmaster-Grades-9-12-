import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 14 (Welcome to Data Science)\Lesson 4 (Seaborn Library in Python)\ACP (Visualisation using Seaborn)\dataset.csv"

try:
    df = pd.read_csv(file_path)
    print("File loaded successfully!")
    print(df.head(10))

    plt.figure(figsize=(8, 4))
    sns.histplot(df["size"], kde=True)
    plt.title("Distribution of Size")
    plt.show()

    plt.figure(figsize=(8, 4))
    sns.histplot(df["tip"], kde=True)
    plt.title("Distribution of Tip")
    plt.show()

    plt.figure(figsize=(8, 4))
    sns.histplot(df["total_bill"], kde=True)
    plt.title("Distribution of Total Bill")
    plt.show()

    plt.figure(figsize=(8, 4))
    sns.histplot(df["total_bill"], kde=False)
    plt.title("Total Bill Histogram (No KDE)")
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x="total_bill", y="tip", hue="time", style="time")
    plt.title("Total Bill vs Tip (by Time)")
    plt.show()

    print("Generating Pair Plot... please wait.")
    sns.pairplot(df, hue='sex')
    plt.show()

except FileNotFoundError:
    print(f"Error: Could not find the file at {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")