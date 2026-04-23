import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r'C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 16 (Statistics - I)\Lesson 4 (Statistics for Categorical Variables and Data Transformation – I)\Activity 2 (Titanic Survival Prediction)\dataset.csv')

print(data.head(5))

sns.set_style('whitegrid')

sns.countplot(x='Survived', data=data)
plt.show()

sns.countplot(x='Gender', hue='Survived', data=data)
plt.show()

sns.countplot(x='Survived', data=data, palette='winter', hue='Survived', legend=False)
plt.show()

sns.countplot(x='Gender', hue='Survived', data=data, palette='winter')
plt.show()

sns.countplot(x='Embarked', data=data)
plt.show()

sns.countplot(x='Embarked', data=data)
plt.xticks(rotation=30, fontsize=20)
plt.show()