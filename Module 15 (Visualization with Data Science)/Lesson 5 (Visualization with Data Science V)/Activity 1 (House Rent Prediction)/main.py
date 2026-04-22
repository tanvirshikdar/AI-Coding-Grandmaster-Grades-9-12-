import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

file_path = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 15 (Visualization with Data Science)\Lesson 5 (Visualization with Data Science V)\Activity 1 (House Rent Prediction)\dataset.csv"

HouseDF = pd.read_csv(file_path)

print(HouseDF.head())
print(HouseDF.info())
print(HouseDF.columns)

sns.pairplot(HouseDF)
plt.show()

numeric_df = HouseDF.select_dtypes(include=[np.number])
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.show()