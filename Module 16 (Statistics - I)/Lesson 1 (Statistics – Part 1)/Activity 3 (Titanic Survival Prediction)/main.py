import pandas as pd
import numpy as np
import statistics as stats
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r'C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 16 (Statistics - I)\Lesson 1 (Statistics – Part 1)\Activity 3 (Titanic Survival Prediction)\dataset.csv')

print(data.head())

median_age = np.median(data['Age'].dropna())
print("Median value of Age -", median_age)

median_fare = np.median(data['Fare'])
print("Median value of Fare -", median_fare)

mode_age = stats.mode(data['Age'].dropna())
print("Mode value of Age -", mode_age)

mode_class = stats.mode(data['Pclass'])
print("Mode value of PClass -", mode_class)

mode_gender = data['Gender'].value_counts().index[0]
print("Mode of Feature Gender -", mode_gender)