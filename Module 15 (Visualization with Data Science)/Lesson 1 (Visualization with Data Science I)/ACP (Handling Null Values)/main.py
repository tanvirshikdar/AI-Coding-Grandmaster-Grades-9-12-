import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import os

file_path = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 15 (Visualization with Data Science)\Lesson 1 (Visualization with Data Science I)\ACP (Handling Null Values)\dataset.csv"

data = pd.read_csv(file_path)

print(data.isnull().sum())

sns.heatmap(data.isnull())
plt.show()

data['Culmen Depth (mm)'] = data['Culmen Depth (mm)'].fillna(data['Culmen Depth (mm)'].mean())
data['Culmen Length (mm)'] = data['Culmen Length (mm)'].fillna(data['Culmen Length (mm)'].mean())
data['Flipper Length (mm)'] = data['Flipper Length (mm)'].fillna(data['Flipper Length (mm)'].mean())
data['Body Mass (g)'] = data['Body Mass (g)'].fillna(data['Body Mass (g)'].mean())
data['Delta 13 C (o/oo)'] = data['Delta 13 C (o/oo)'].fillna(data['Delta 13 C (o/oo)'].mean())
data['Delta 15 N (o/oo)'] = data['Delta 15 N (o/oo)'].fillna(data['Delta 15 N (o/oo)'].mean())

data['Gender'] = data['Gender'].fillna(data['Gender'].value_counts().index[0])

if 'Comments' in data.columns:
    data = data.drop('Comments', axis=1)

print("\n--- After Cleaning ---")
print(data.isnull().sum())