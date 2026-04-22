import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 15 (Visualization with Data Science)\Lesson 5 (Visualization with Data Science V)\ACP (Visualization to Check Relation between Variables)\dataset.csv"

df = pd.read_csv(file_path)

plt.figure(figsize=(10, 6))
plt.scatter(df['Culmen Length (mm)'], df['Body Mass (g)'], color='blue', alpha=0.5)
plt.title('Scatter Plot: Culmen Length vs Body Mass')
plt.xlabel('Culmen Length (mm)')
plt.ylabel('Body Mass (g)')
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df['Culmen Depth (mm)'], df['Body Mass (g)'], color='green', alpha=0.5)
plt.title('Scatter Plot: Culmen Depth vs Body Mass')
plt.xlabel('Culmen Depth (mm)')
plt.ylabel('Body Mass (g)')
plt.show()

sns.pairplot(df.dropna())
plt.show()

df_sorted = df.sort_values('Culmen Length (mm)')
plt.figure(figsize=(10, 6))
plt.fill_between(df_sorted['Culmen Length (mm)'], df_sorted['Body Mass (g)'], color="skyblue", alpha=0.4)
plt.plot(df_sorted['Culmen Length (mm)'], df_sorted['Body Mass (g)'], color="Slateblue", alpha=0.6)
plt.title('Area Graph: Culmen Length vs Body Mass')
plt.xlabel('Culmen Length (mm)')
plt.ylabel('Body Mass (g)')
plt.show()