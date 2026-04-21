import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

sns.set_theme(style="ticks")

file_path = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 14 (Welcome to Data Science)\Lesson 5 (Advance Visualizations in Python)\Activity 1 (Weather Data Visualization)\dataset.csv"

try:
    weather = pd.read_csv(file_path)
    print("File loaded successfully!")

    print(weather.head())
    weather.info()

    plt.figure(figsize=(10, 6))
    sns.barplot(x=weather['humidity'], y=weather['temperature'])
    plt.title("Humidity vs Temperature Barplot")
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.histplot(weather['humidity'], kde=True)
    plt.title("Humidity Distribution")
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.histplot(weather['humidity'], kde=False)
    sns.rugplot(weather['humidity'])
    plt.title("Humidity Histogram with Rug")
    plt.show()

    sns.jointplot(x='humidity', y='temperature', data=weather)
    plt.show()

    sns.jointplot(x='humidity', y='temperature', data=weather, kind="hex")
    plt.show()

    sns.jointplot(x='humidity', y='temperature', data=weather, kind="kde")
    plt.show()

    sns.pairplot(weather[['humidity', 'temperature', 'air_pollution_index']])
    plt.show()

    plt.figure(figsize=(12, 6))
    sns.stripplot(x='weather_type', y='temperature', data=weather)
    plt.xticks(rotation=45)
    plt.show()

    plt.figure(figsize=(12, 6))
    sns.stripplot(x='weather_type', y='temperature', data=weather, jitter=True)
    plt.xticks(rotation=45)
    plt.show()

    plt.figure(figsize=(12, 6))
    sns.swarmplot(x='weather_type', y='temperature', data=weather.head(100)) 
    plt.title("Swarmplot (Sample of first 100 rows)")
    plt.show()

    plt.figure(figsize=(12, 6))
    sns.countplot(x='weather_type', data=weather)
    plt.xticks(rotation=45)
    plt.show()

    plt.figure(figsize=(12, 6))
    sns.pointplot(x='humidity', y='temperature', hue='weather_type', data=weather.head(100))
    plt.title("Pointplot (Sample)")
    plt.show()

except FileNotFoundError:
    print(f"Error: Could not find the file at {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")