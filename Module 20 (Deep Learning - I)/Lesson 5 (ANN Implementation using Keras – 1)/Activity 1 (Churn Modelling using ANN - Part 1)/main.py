import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

file_path = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 20 (Deep Learning - I)\Lesson 5 (ANN Implementation using Keras – 1)\Activity 1 (Churn Modelling using ANN - Part 1)\dataset.csv"

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
else:
    df = pd.read_csv('Churn_Modelling.csv')

print(df.head())
df.info()
print(df.describe())

lb = LabelEncoder()
df['Geography'] = lb.fit_transform(df['Geography'])
df['Gender'] = lb.fit_transform(df['Gender'])

df = df.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1)

y = df.pop('Exited')
X = df

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

print("Preprocessed X_train sample:")
print(X_train[:5])