import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r'C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 16 (Statistics - I)\Lesson 4 (Statistics for Categorical Variables and Data Transformation – I)\Activity 1 (Titanic Survival Prediction)\dataset.csv')

print(data.head(5))

print(data.dtypes)

nominal_cat = ['Name','Ticket','Cabin']
ordinal_cat = ['Embarked','Gender']

print(data['Gender'].value_counts())

gender_categories = ['Female','Male']
data['Gender'] = pd.Categorical(data['Gender'], categories=gender_categories, ordered=True)

median_index_gender = np.median(data['Gender'].cat.codes.dropna())
median_gender = gender_categories[int(median_index_gender)]
print(median_gender)

print(data['Embarked'].value_counts())

embarked_categories = ['S','C','Q']
data['Embarked'] = pd.Categorical(data['Embarked'], categories=embarked_categories, ordered=True)

median_index_embarked = np.median(data['Embarked'].cat.codes.dropna())
median_embarked = embarked_categories[int(median_index_embarked)]
print(median_embarked)