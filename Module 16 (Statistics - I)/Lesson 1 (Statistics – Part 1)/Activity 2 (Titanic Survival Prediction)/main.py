import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r'C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 16 (Statistics - I)\Lesson 1 (Statistics – Part 1)\Activity 2 (Titanic Survival Prediction)\dataset.csv')

print(data.head())

mean_age = np.mean(data['Age'])
print("Mean Age of Passengers is - ", mean_age)

mean_fare = np.mean(data['Fare'])
print("Mean Fare is - ", mean_fare)