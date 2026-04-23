import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r'C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 16 (Statistics - I)\Lesson 6 (Exploratory Data Analysis)\Activity 2 (Iris Data Survey)\dataset.csv')

print(data.head(5))

print(data.isnull().sum())

print(data.describe())

labels = ['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
for label in labels:
    print('Distribution of', label)
    sns.boxplot(x=data[label])
    plt.show()

numeric_data = data.select_dtypes(include=[np.number])
sns.heatmap(numeric_data.corr(), annot=True, cmap='RdYlGn')
plt.show()

for label in labels:
    print('Distribution of', label)
    sns.histplot(data[label], kde=True)
    plt.show()

for label in labels:
    print('skewness of ', label)
    print(data[label].skew())