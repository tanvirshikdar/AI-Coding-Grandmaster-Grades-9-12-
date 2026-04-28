import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

file_path = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 20 (Deep Learning - I)\Lesson 5 (ANN Implementation using Keras – 1)\ACP (Legendary Pokemon Prediction using ANN)\dataset.csv"

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
else:
    df = pd.read_csv("dataset.csv")

categorical_cols = df.select_dtypes(include=['object']).columns
le = LabelEncoder()
for col in categorical_cols:
    df[col] = le.fit_transform(df[col])

if 'is_legendary' in df.columns:
    y = df.pop('is_legendary')
elif 'legendary' in df.columns:
    y = df.pop('legendary')
else:
    y = df.iloc[:, -1]
    df = df.iloc[:, :-1]

X = df

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

print("Preprocessing Complete.")
print("Feature Shape:", X_train.shape)
print("Target Distribution:\n", y.value_counts())