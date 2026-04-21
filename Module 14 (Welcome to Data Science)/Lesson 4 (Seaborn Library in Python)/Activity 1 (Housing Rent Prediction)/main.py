import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 14 (Welcome to Data Science)\Lesson 4 (Seaborn Library in Python)\Activity 1 (Housing Rent Prediction)\USA_Housing.csv"

try:
    df = pd.read_csv(file_path)
    print("File loaded successfully!")
    
    print("\n--- First 10 Rows ---")
    print(df.head(10))

    print("\n--- Data Info ---")
    df.info() 

    print("\n--- Summary Statistics ---")
    print(df.describe())

    print("\n--- Columns ---")
    print(df.columns)

    numeric_df = df.select_dtypes(include=[np.number])

    print("\nGenerating Pairplot... (This might take a minute)")
    sns.pairplot(numeric_df)
    plt.show()

    print("Generating Heatmap...")
    plt.figure(figsize=(10, 8))
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
    plt.title("Correlation Heatmap of USA Housing Data")
    plt.show()

except FileNotFoundError:
    print(f"Error: Could not find the file at: {file_path}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")