import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 15 (Visualization with Data Science)\Lesson 6 (Capstone Project)\ACP (Capstone Project)\dataset.csv"

df = pd.read_csv(file_path)

print(df.isnull().sum())

plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title("Missing Values Heatmap")
plt.show()

num_cols = df.select_dtypes(include=[np.number]).columns
for col in num_cols:
    df[col] = df[col].fillna(df[col].median())

cat_cols = df.select_dtypes(include=['object']).columns
for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

print(df.isnull().sum())

sns.pairplot(df)
plt.show()

plt.figure(figsize=(12, 8))
numeric_only = df.select_dtypes(include=[np.number])
sns.heatmap(numeric_only.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

plt.figure(figsize=(12, 6))
df.boxplot(column=['Culmen Length (mm)', 'Culmen Depth (mm)', 'Flipper Length (mm)'])
plt.title("Boxplot of Dimensions")
plt.show()

plt.figure(figsize=(8, 5))
plt.boxplot(df['Body Mass (g)'])
plt.title("Boxplot of Body Mass")
plt.show()

target_gender_col = 'Gender' if 'Gender' in df.columns else 'Sex'
plt.figure(figsize=(8, 5))
sns.countplot(x=target_gender_col, data=df, palette='Set2')
plt.title(f"Count Plot for {target_gender_col}")
plt.show()