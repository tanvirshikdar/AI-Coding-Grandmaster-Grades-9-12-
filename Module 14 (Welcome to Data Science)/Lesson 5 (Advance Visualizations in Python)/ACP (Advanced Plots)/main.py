import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 14 (Welcome to Data Science)\Lesson 5 (Advance Visualizations in Python)\ACP (Advanced Plots)\dataset.csv"

try:
    df = pd.read_csv(file_path)
    print("File loaded successfully!")
    print(df.head())

    sns.set_theme(style="whitegrid")

    plt.figure(figsize=(8, 6))
    sns.barplot(x='Species', y='SepalLengthCm', data=df)
    plt.title('Sepal Length by Species')
    plt.show()

    plt.figure(figsize=(8, 6))
    sns.countplot(x='Species', data=df)
    plt.title('Count of Each Species')
    plt.show()

    plt.figure(figsize=(8, 6))
    sns.boxplot(x='Species', y='SepalWidthCm', data=df)
    plt.title('Sepal Width Distribution by Species (Boxplot)')
    plt.show()

    plt.figure(figsize=(8, 6))
    sns.swarmplot(x='Species', y='SepalWidthCm', data=df)
    plt.title('Sepal Width Distribution by Species (Swarmplot)')
    plt.show()

    plt.figure(figsize=(8, 6))
    sns.histplot(df['SepalWidthCm'], kde=True, color='purple')
    plt.title('Distribution of Sepal Width')
    plt.show()

    sns.jointplot(x='SepalLengthCm', y='SepalWidthCm', data=df, kind='scatter')
    plt.show()

    print("Generating Pair Plot... please wait.")
    sns.pairplot(df, hue='Species', markers=["o", "s", "D"])
    plt.show()

except FileNotFoundError:
    print(f"Error: The file was not found at {file_path}. Please check the folder path.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")