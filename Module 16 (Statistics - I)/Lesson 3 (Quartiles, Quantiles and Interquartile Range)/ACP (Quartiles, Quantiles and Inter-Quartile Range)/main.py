import pandas as pd
import numpy as np
import statistics as stats
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 16 (Statistics - I)\Lesson 3 (Quartiles, Quantiles and Interquartile Range)\ACP (Quartiles, Quantiles and Inter-Quartile Range)\dataset.csv')

print(data.head())
print(data.info())
print(data.isnull().any())

ten_percentile_price = np.quantile(data['Price'], 0.1)
print("Value that divides 10 Percent of Data :", ten_percentile_price)

Q1_price = np.quantile(data['Price'], 0.25)
Q2_price = np.quantile(data['Price'], 0.5)
Q3_price = np.quantile(data['Price'], 0.75)

print("Quartiles for Price -")
print("First Quartile :", Q1_price)
print("Second Quartile :", Q2_price)
print("Third Quartile :", Q3_price)

IQR_price = Q3_price - Q1_price
print("Inter-Quartile Range :", IQR_price)

Q1_rating = np.quantile(data['User Rating'], 0.25)
Q2_rating = np.quantile(data['User Rating'], 0.5)
Q3_rating = np.quantile(data['User Rating'], 0.75)

print("Quartiles for User Rating -")
print("First Quartile :", Q1_rating)
print("Second Quartile :", Q2_rating)
print("Third Quartile :", Q3_rating)

IQR_rating = Q3_rating - Q1_rating
print("Inter-Quartile Range :", IQR_rating)

plt.boxplot(data['Price'])
plt.ylabel('Price')
plt.title("Distribution of Price")
plt.show()

plt.boxplot(data['User Rating'])
plt.ylabel('User Rating')
plt.title("Distribution of User Rating")
plt.show()