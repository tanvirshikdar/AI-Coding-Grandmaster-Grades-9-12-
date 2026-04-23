import pandas as pd
import numpy as np
import statistics as stats
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 16 (Statistics - I)\Lesson 2 (Statistics – Part 2)\ACP (Data Distribution Measures)\dataset.csv')

print(data.head())
print(data.info())
print(data.isnull().any())

data = data.dropna() 

rating_std = np.std(data['User Rating'])
print("User Rating Standard Deviation:", rating_std)

rating_var = np.var(data['User Rating'])
print("User Rating Variance:", rating_var)

price_std = np.std(data['Price'])
print("Price Standard Deviation:", price_std)

price_var = np.var(data['Price'])
print("Price Variance:", price_var)

plt.hist(data['User Rating'])
plt.xlabel('User Rating')
plt.ylabel('Number of Books')
plt.show()

bins_rating = np.arange(3, 5.1, 0.1) # Adjusted to 5.1 to include 5.0
plt.hist(data['User Rating'], edgecolor='black', color='teal', bins=bins_rating)
plt.xlabel('User Rating')
plt.ylabel('Number of Books')
plt.show()

plt.hist(data['Price'])
plt.xlabel('Price')
plt.ylabel('Number of Books')
plt.show()

bins_price = np.arange(0, 110, 5)
plt.hist(data['Price'], edgecolor='black', color='darkred', bins=bins_price)
plt.xlabel('Price')
plt.ylabel('Number of Books')
plt.show()