import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

file_path = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 18 (Machine Learning - I)\Lesson 3 (Classification and Regression)\ACP (Data Classification)\dataset.csv"
df = pd.read_csv(file_path, sep='\t') 

cols_to_drop = ['Name', 'Ticket', 'Cabin']
df = df.drop([col for col in cols_to_drop if col in df.columns], axis=1)

print(df.info())

plt.figure()
sb.heatmap(df.isnull())
plt.show()

if 'Age' in df.columns:
    df['Age'] = df['Age'].interpolate()

df = df.dropna()

print(df.head())

plt.figure()
sb.countplot(x="Survived", data=df)
plt.show()

if 'Sex' in df.columns:
    plt.figure()
    sb.countplot(x="Survived", hue="Sex", data=df, palette="winter")
    plt.show()

plt.figure()
sb.countplot(x="Survived", hue="Pclass", data=df, palette="PuBu")
plt.show()

if 'Age' in df.columns:
    plt.figure()
    df["Age"].plot.hist()
    plt.show()