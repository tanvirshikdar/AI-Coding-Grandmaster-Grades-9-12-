import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LeakyReLU, PReLU, ELU

file_path = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 20 (Deep Learning - I)\Lesson 6 (ANN Implementation using Keras – 2)\Activity 1 (Churn Modelling using ANN - Part 2)\dataset.csv"

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
else:
    df = pd.read_csv('Churn_Modelling.csv')

lb = LabelEncoder()
df['Geography'] = lb.fit_transform(df['Geography'])
df['Gender'] = lb.fit_transform(df['Gender'])

df = df.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1)

y = df.pop('Exited')
X = df

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

classifier = Sequential()
classifier.add(Dense(units=6, kernel_initializer='he_uniform', activation='relu', input_dim=10))
classifier.add(Dense(units=6, kernel_initializer='he_uniform', activation='relu'))
classifier.add(Dense(units=1, kernel_initializer='glorot_uniform', activation='sigmoid'))

classifier.compile(optimizer='Adamax', loss='binary_crossentropy', metrics=['accuracy'])

model_history = classifier.fit(X_train, y_train, batch_size=10, epochs=100)

classifier.summary()

Y_pred = classifier.predict(X_test)
Y_pred = (Y_pred > 0.5)

cm = confusion_matrix(y_test, Y_pred)
print("Confusion Matrix:")
print(cm)

score = accuracy_score(y_test, Y_pred)
print(f"Accuracy Score: {score}")