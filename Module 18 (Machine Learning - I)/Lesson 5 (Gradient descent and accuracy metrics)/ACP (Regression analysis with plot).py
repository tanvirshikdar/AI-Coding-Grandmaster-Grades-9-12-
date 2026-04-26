import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (12.0, 9.0)

file_path = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 18 (Machine Learning - I)\Lesson 4 (Study of Regression)\ACP (Regression analysis)\dataset.csv"
data = pd.read_csv(file_path)

X = data.iloc[:, 1].values
Y = data.iloc[:, 2].values

X_mean = np.mean(X)
Y_mean = np.mean(Y)

num = 0
den = 0
for i in range(len(X)):
    num += (X[i] - X_mean) * (Y[i] - Y_mean)
    den += (X[i] - X_mean)**2

m = num / den
c = Y_mean - m * X_mean

print(f"Slope (m): {m}")
print(f"Intercept (c): {c}")

Y_pred = m * X + c

mse_num = 0
for i in range(len(Y)):
    mse_num += (Y[i] - Y_pred[i])**2
mse = mse_num / len(Y)

ssr = 0 
sst = 0 
for i in range(len(Y)):
    ssr += (Y[i] - Y_pred[i])**2
    sst += (Y[i] - Y_mean)**2
r2 = 1 - (ssr / sst)

print(f"Mean Squared Error: {mse}")
print(f"R-Squared Value: {r2}")

plt.scatter(X, Y, color='blue', label='Actual Data') 
plt.plot([min(X), max(X)], [min(Y_pred), max(Y_pred)], color='red', label='Regression Line') 
plt.xlabel("X Variable")
plt.ylabel("Y Variable")
plt.legend()
plt.show()