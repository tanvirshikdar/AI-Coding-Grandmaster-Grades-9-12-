import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r'C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 16 (Statistics - I)\Lesson 6 (Exploratory Data Analysis)\ACP (Exploratory Data Analysis)\dataset.csv')

print(data.head())
print(data.info())
print(data.isnull().sum())
print(data.describe())

sns.countplot(x='gender', data=data, palette='winter', hue='gender', legend=False)
plt.show()

sns.countplot(x='race/ethnicity', data=data, palette='winter', hue='race/ethnicity', legend=False)
plt.show()

sns.countplot(x='lunch', data=data, palette='winter', hue='lunch', legend=False)
plt.show()

sns.countplot(x='parental level of education', data=data, palette='winter', hue='parental level of education', legend=False)
plt.xticks(rotation=45)
plt.show()

data.groupby('race/ethnicity').size().plot(kind='pie', autopct='%.2f')
plt.ylabel('')
plt.show()

data.groupby('parental level of education').size().plot(kind='pie', autopct='%.2f')
plt.ylabel('')
plt.show()

sns.countplot(data=data, x='gender', hue='race/ethnicity', palette='winter')
plt.show()

sns.countplot(data=data, x='lunch', hue='gender', palette='winter')
plt.show()

sns.histplot(data['math score'], kde=True)
plt.show()
print("Skewness Math Score:", data['math score'].skew())

sns.histplot(data['reading score'], kde=True)
plt.show()
print("Skewness Reading Score:", data['reading score'].skew())

sns.histplot(data['writing score'], kde=True)
plt.show()
print("Skewness Writing Score:", data['writing score'].skew())

sns.boxplot(x='gender', y='math score', data=data, hue='gender', legend=False)
plt.show()

numeric_data = data.select_dtypes(include=[np.number])
sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm')
plt.show()