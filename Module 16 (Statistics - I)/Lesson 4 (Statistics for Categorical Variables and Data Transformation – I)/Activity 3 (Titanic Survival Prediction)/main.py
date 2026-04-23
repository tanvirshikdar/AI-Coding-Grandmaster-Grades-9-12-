import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

data = pd.read_csv(r'C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 16 (Statistics - I)\Lesson 4 (Statistics for Categorical Variables and Data Transformation – I)\Activity 3 (Titanic Survival Prediction)\dataset.csv')

print(data.head(5))

num_data = data.drop(['Name', 'Ticket', 'Cabin', 'Embarked', 'Gender'], axis=1)

labels = ['PassengerId','Survived','Pclass','Age','SibSp','Parch','Fare']

for label in labels:
    plt.boxplot(num_data[label].dropna())
    print('Distribution of', label)
    plt.show()

scaler = StandardScaler()
num_data_scaled = scaler.fit_transform(num_data.dropna())