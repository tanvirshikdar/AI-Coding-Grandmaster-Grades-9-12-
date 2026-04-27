import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import math

path = r'C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 19 (Machine Learning - II)\Lesson 3 (Two point classification)\Activity 1 (Apply the binary class algorithm to the given dataset)\dataset.csv'

df = pd.read_csv(path)
print(df.head())

plt.scatter(df.age, df.bought_insurance, marker='+', color='red')
plt.xlabel('Age')
plt.ylabel('Bought Insurance')
plt.show()

X_train, X_test, y_train, y_test = train_test_split(df[['age']], df.bought_insurance, train_size=0.8)

print("Test Features:\n", X_test)

model = LogisticRegression()
model.fit(X_train, y_train)

y_predicted = model.predict(X_test)
print("Predicted Probabilities:\n", model.predict_proba(X_test))
print("Model Accuracy Score:", model.score(X_test, y_test))

print("Predictions for X_test:", y_predicted)
print("Coefficient:", model.coef_)
print("Intercept:", model.intercept_)

def sigmoid(x):
  return 1 / (1 + math.exp(-x))

def prediction_function(age):
    z = model.coef_[0][0] * age + model.intercept_[0]
    y = sigmoid(z)
    return y

age_35 = 35
print(f"Prediction for age 35: {prediction_function(age_35)}")

age_43 = 43
print(f"Prediction for age 43: {prediction_function(age_43)}")