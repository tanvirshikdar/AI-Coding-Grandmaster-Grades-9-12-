import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r'C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 16 (Statistics - I)\Lesson 1 (Statistics – Part 1)\Activity 1 (Titanic Survival Prediction)\dataset.csv')
print(data.head(5))

print(data.dtypes)

print(data.isnull().sum())