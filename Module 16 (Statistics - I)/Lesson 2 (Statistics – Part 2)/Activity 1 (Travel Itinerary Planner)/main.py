import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r'C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 16 (Statistics - I)\Lesson 2 (Statistics – Part 2)\Activity 1 (Travel Itinerary Planner)\dataset.csv')

print(data.head(5))
print(data.info())
print(data.isnull().sum())

mean_temp = np.mean(data['Temperature (C)'])
print("Mean Temperature is :", mean_temp)

var_temp = np.var(data['Temperature (C)'])
print("Variation of Temperature is :", var_temp)

standard_deviation_temp = np.std(data['Temperature (C)'])
print("Standard Deviation of Temperature is :", standard_deviation_temp)

for i in range(1, 13):
    month = data.loc[data["month"] == i]["Temperature (C)"]
    print("For month "+str(i))
    print("Mean temperature is "+ str(np.mean(month)))
    print("Standard deviation is "+ str(np.std(month))+"\n")