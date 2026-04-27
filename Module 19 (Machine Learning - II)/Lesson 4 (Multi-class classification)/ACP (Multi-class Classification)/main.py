import pandas as pd
import numpy as np
from sklearn import linear_model

path = r'C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 19 (Machine Learning - II)\Lesson 4 (Multi-class classification)\Activity 1 (Apply the multi-class regression algorithm to the given dataset)\ACP (Multi-class Classification)\dataset.csv'

df = pd.read_csv(path)

features = ['Por', 'Brittle', 'Perm', 'TOC']
target = 'Prod'

X = df[features].values.reshape(-1, len(features))
y = df[target].values

ols = linear_model.LinearRegression()
model = ols.fit(X, y)

print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print("R^2 Score:", model.score(X, y))

x_pred_1 = np.array([12, 81, 2.31, 2.8])
x_pred_1 = x_pred_1.reshape(-1, len(features))

print("Single Prediction:", model.predict(x_pred_1))

x_pred_2 = np.array([[12, 81, 2.31, 2.8], [15, 60, 2.5, 1]])
x_pred_2 = x_pred_2.reshape(-1, len(features))

print("Multiple Predictions:", model.predict(x_pred_2))