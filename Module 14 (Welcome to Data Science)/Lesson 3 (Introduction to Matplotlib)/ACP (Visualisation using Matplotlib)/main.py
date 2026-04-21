import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_path = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 14 (Welcome to Data Science)\Lesson 3 (Introduction to Matplotlib)\ACP (Visualisation using Matplotlib)\company_sales_data.csv"

try:
    train = pd.read_csv(file_path)
    print("File loaded successfully!")
except FileNotFoundError:
    print(f"Error: Could not find the file at {file_path}")
    exit()

profitList = train['total_profit'].tolist()
monthList = train['month_number'].tolist()

plt.figure(figsize=(10, 6))
plt.plot(monthList, profitList, label='Month-wise Profit data of last year')
plt.xlabel('Month number')
plt.ylabel('Profit in dollar')
plt.xticks(monthList)
plt.title('Company profit per month')
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(monthList, profitList, label='Profit data of last year', 
         color='r', marker='o', markerfacecolor='k', 
         linestyle='--', linewidth=3)
      
plt.xlabel('Month Number')
plt.ylabel('Sold units number') 
plt.legend(loc='lower right')
plt.title('Company Sales data of last year')
plt.xticks(monthList)
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.show()

faceCremSalesData = train['facecream'].tolist()
faceWashSalesData = train['facewash'].tolist()
toothPasteSalesData = train['toothpaste'].tolist()
bathingsoapSalesData = train['bathingsoap'].tolist()
shampooSalesData = train['shampoo'].tolist()
moisturizerSalesData = train['moisturizer'].tolist()

plt.figure(figsize=(10, 6))
plt.plot(monthList, faceCremSalesData, label='Face cream Sales Data', marker='o', linewidth=3)
plt.plot(monthList, faceWashSalesData, label='Face Wash Sales Data', marker='o', linewidth=3)
plt.plot(monthList, toothPasteSalesData, label='ToothPaste Sales Data', marker='o', linewidth=3)
plt.plot(monthList, bathingsoapSalesData, label='Bathing Soap Sales Data', marker='o', linewidth=3)
plt.plot(monthList, shampooSalesData, label='Shampoo Sales Data', marker='o', linewidth=3)
plt.plot(monthList, moisturizerSalesData, label='Moisturizer Sales Data', marker='o', linewidth=3)

plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.legend(loc='upper left')
plt.xticks(monthList)
plt.yticks([1000, 2000, 4000, 6000, 8000, 10000, 12000, 15000, 18000])
plt.title('Sales data')
plt.show()

plt.figure(figsize=(10, 6))
plt.bar([a-0.25 for a in monthList], faceCremSalesData, width=0.25, label='Face Cream sales data', align='edge')
plt.bar([a+0.25 for a in monthList], faceWashSalesData, width=-0.25, label='Face Wash sales data', align='edge')

plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.legend(loc='upper left')
plt.xticks(monthList)
plt.grid(True, linewidth=1, linestyle="--")
plt.title('Facewash and facecream sales data')
plt.show()