import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

file_path = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 15 (Visualization with Data Science)\Lesson 6 (Capstone Project)\Activity 1 (Iris Data Set Analysis)\dataset.csv"

df = pd.read_csv(file_path)

print(df.head())
print(df.shape)
print(df.columns)
print(df.describe())
print(df.isnull().sum())
print(df.info())

df.hist(figsize=(12,12), layout=(5,3))
plt.tight_layout()
plt.show()

df.plot(kind='box', subplots=True, layout=(5,3), figsize=(12,12))
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='sex', y='chol', hue='target', palette='spring')
plt.show()

print(df['sex'].value_counts())
print(df['target'].value_counts())
print(df['thal'].value_counts())

plt.figure(figsize=(20,10))
numeric_df = df.select_dtypes(include=[np.number])
sns.heatmap(numeric_df.corr(), annot=True, cmap='terrain')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x='sex', data=df, palette='husl', hue='target')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x="target", palette="BuGn", data=df)
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x="ca", hue="target", data=df)
plt.show()