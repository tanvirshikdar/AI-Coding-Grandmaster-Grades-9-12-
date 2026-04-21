import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 14 (Welcome to Data Science)\Lesson 6 (Capstone Project)\Activity 1 (Capstone Project)\dataset.csv"

try:
    df = pd.read_csv(file_path)
    print("File loaded successfully!")

    print("\n--- First 10 Rows ---")
    print(df.head(10))
    print("\n--- Shape ---")
    print(df.shape)
    print("\n--- Last 5 Rows ---")
    print(df.tail())
    print("\n--- Null Value Count ---")
    print(df.isnull().sum())
    print("\n--- Data Types ---")
    print(df.dtypes)
    print("\n--- Dataset Info ---")
    df.info()

    print("\n--- Basic Statistics ---")
    print(df.describe())
    print("\n--- All Statistics (including Categorical) ---")
    print(df.describe(include='all'))
    print("\n--- Correlation Matrix ---")
    numeric_df = df.select_dtypes(include=[np.number])
    print(numeric_df.corr())

    plt.figure(figsize=(10, 8))
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
    plt.title("Correlation Heatmap")
    plt.show()

    numeric_df.hist(figsize=(12, 8), bins=20)
    plt.suptitle("Numerical Distributions")
    plt.show()

    num_cols = len(numeric_df.columns)
    numeric_df.plot(kind='box', subplots=True, layout=(1, num_cols), 
                    sharex=False, sharey=False, figsize=(15, 5))
    plt.suptitle("Box Plots for Outlier Detection")
    plt.show()

    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        print(f"\nValue counts for {col}:")
        print(df[col].value_counts())
        
        plt.figure(figsize=(8, 5))
        sns.countplot(data=df, x=col)
        plt.title(f"Count Plot: {col}")
        plt.show()

    if len(categorical_cols) > 0:
        print("\nGenerating Pairplot... please wait.")
        sns.pairplot(data=df, hue=categorical_cols[0])
        plt.show()

except FileNotFoundError:
    print(f"Error: Could not find the file at {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")