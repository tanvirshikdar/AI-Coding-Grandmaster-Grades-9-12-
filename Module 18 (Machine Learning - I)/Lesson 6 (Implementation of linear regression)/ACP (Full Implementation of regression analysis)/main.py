import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys

file_path = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 18 (Machine Learning - I)\Lesson 6 (Implementation of linear regression)\ACP (Full Implementation of regression analysis)\dataset.csv"

df = pd.read_csv(file_path, sep=None, engine='python', header=None)
df = df.dropna(axis=1, how='all')
df = df.apply(pd.to_numeric, errors='coerce')
df = df.dropna()

if len(df) < 5:
    print("ERROR: The dataset is still empty!")
    sys.exit()

X = df.iloc[:, 0].values 
Y = df.iloc[:, 1].values

m = 0  
c = 0 
L = 0.0001  
epochs = 1000 
n = float(len(X))

for i in range(epochs):
    Y_pred = m * X + c 
    D_m = (-2/n) * sum(X * (Y - Y_pred)) 
    D_c = (-2/n) * sum(Y - Y_pred)  
    m = m - L * D_m  
    c = c - L * D_c  

print(f"Final Slope (m): {m}")
print(f"Final Intercept (c): {c}")

Y_pred = m * X + c

plt.figure(figsize=(12, 8))
plt.scatter(X, Y, color='black', alpha=0.5, label='Actual Data')
plt.plot(X, Y_pred, color='red', linewidth=3, alpha=0.8, label='Gradient Descent Line')
plt.xlabel("X values")
plt.ylabel("Y values")
plt.legend()
plt.show()