import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 15 (Visualization with Data Science)\Lesson 4 (Visualization with Data Science IV)\ACP (Visualization Using Histogram)\dataset.csv"

df = pd.read_csv(file_path)

plt.figure(figsize=(10, 6))
plt.hist(df['Culmen Length (mm)'].dropna(), bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Culmen Length (mm)')
plt.xlabel('Length (mm)')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(df['Culmen Depth (mm)'].dropna(), bins=15, color='salmon', edgecolor='black')
plt.title('Distribution of Culmen Depth (mm)')
plt.xlabel('Depth (mm)')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(df['Flipper Length (mm)'].dropna(), bins=25, color='lightgreen', edgecolor='black')
plt.title('Distribution of Flipper Length (mm)')
plt.xlabel('Length (mm)')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(df['Body Mass (g)'].dropna(), bins=30, color='plum', edgecolor='black')
plt.title('Distribution of Body Mass (g)')
plt.xlabel('Mass (g)')
plt.ylabel('Frequency')
plt.show()