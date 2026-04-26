import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

file_path = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 18 (Machine Learning - I)\Lesson 2 (Understanding more about data)\Activity 1 (Data preprocessing)\dataset.csv"
Titanic = pd.read_csv(file_path)

print("--- Initial Data ---")
print(Titanic.head())
print(f"Shape: {Titanic.shape}")
print("\n--- Null Values ---")
print(Titanic.isnull().sum())

sns.heatmap(Titanic.isnull(), cmap="spring")
plt.title("Null Values Heatmap (Before)")
plt.show() 

if 'deck' in Titanic.columns:
    Titanic.drop("deck", axis=1, inplace=True)
    print("\n'deck' column dropped.")

Titanic.dropna(inplace=True)

sns.heatmap(Titanic.isnull(), cbar=False)
plt.title("Null Values Heatmap (After)")
plt.show()

print("\n--- Cleaned Null Count ---")
print(Titanic.isnull().sum())

sex = pd.get_dummies(Titanic["sex"], drop_first=True)
arked = pd.get_dummies(Titanic["embarked"], drop_first=True)
pclass = pd.get_dummies(Titanic["pclass"], drop_first=True)

Titanic = pd.concat([Titanic, sex, pclass], axis=1)

print("\n--- Final Updated Dataset ---")
print(Titanic.head())