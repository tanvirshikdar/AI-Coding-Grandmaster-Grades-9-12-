import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r'C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 16 (Statistics - I)\Lesson 6 (Exploratory Data Analysis)\Activity 1 (Titanic Survival Prediction)\dataset.csv')

print(data.head(5))

sns.countplot(x='Gender', hue='Survived', data=data)
plt.show()

sns.countplot(x='Pclass', hue='Survived', data=data)
plt.show()

sns.histplot(data['Age'].dropna(), kde=False, bins=40)
plt.show()

sns.countplot(x='Gender', data=data)
plt.show()

sns.countplot(x='Survived', hue='SibSp', data=data, palette="mako")
plt.show()

sns.countplot(x='Survived', hue='Parch', data=data, palette="mako")
plt.show()

sns.histplot(data['Fare'], kde=True)
plt.show()

sns.boxplot(x='Pclass', y='Age', data=data, palette='winter', hue='Pclass', legend=False)
plt.show()

numeric_data = data.select_dtypes(include=[np.number])
sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm')
plt.show()