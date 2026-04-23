import pandas as pd
import numpy as np
import statistics as stats

data = pd.read_csv(r'C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 16 (Statistics - I)\Lesson 1 (Statistics – Part 1)\ACP (Mean, Median, and Mode)\dataset.csv')

print("--- Dataset Information ---")
print(data.info())

print("\n--- Null Value Check ---")
print(data.isnull().sum())

data['User Rating'] = data['User Rating'].fillna(data['User Rating'].median())
data['Reviews'] = data['Reviews'].fillna(data['Reviews'].median())
data['Price'] = data['Price'].fillna(data['Price'].median())

def get_stats(column_name):
    print(f"\n--- Statistics for {column_name} ---")
    print("Mean:", np.mean(data[column_name]))
    print("Median:", np.median(data[column_name]))
    print("Mode:", stats.mode(data[column_name]))

get_stats('User Rating')
get_stats('Price')
get_stats('Reviews')