import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

file_path = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 15 (Visualization with Data Science)\Lesson 1 (Visualization with Data Science I)\Activity 1 (Data Cleaning)\dataset.csv"

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    print("File loaded successfully!")
else:
    print(f"Error: The file at {file_path} was not found. Please check the path.")

print("\n--- First 10 Rows ---")
print(df.head(10))

print("\n--- Missing Values Check ---")
print(df.isnull().sum())

subset = df.iloc[:5200, :] 
plt.figure(figsize=(12, 8))
sns.heatmap(subset.isnull(), cbar=False, cmap="viridis")
plt.title("Heatmap of Missing Values")
plt.show()

df = df.dropna(how="all")
df = df.bfill()
df = df.interpolate()

df_cleaned = df.dropna()

print("\n--- Cleaned Data Shape ---")
print(f"Original shape: {df.shape}")
print(f"Cleaned shape: {df_cleaned.shape}")

print(df_cleaned.head())