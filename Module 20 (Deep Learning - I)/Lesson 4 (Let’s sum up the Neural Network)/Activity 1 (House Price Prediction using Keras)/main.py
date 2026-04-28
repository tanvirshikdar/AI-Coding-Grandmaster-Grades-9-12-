import pandas as pd
import numpy as np
import os
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

file_path = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 20 (Deep Learning - I)\Lesson 4 (Let’s sum up the Neural Network)\Activity 1 (House Price Prediction using Keras)\dataset.csv"

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    print("Dataset loaded successfully!")
else:
    print(f"Error: The file was not found at {file_path}")
    df = pd.read_csv("dataset.csv") 

print(df.head())

y = df.pop('AboveMedianPrice')
X = df

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

model = Sequential()
model.add(Dense(10, input_dim=X_train.shape[1], kernel_initializer='normal', activation='relu'))
model.add(Dense(6, kernel_initializer='normal', activation='relu'))
model.add(Dense(1, kernel_initializer='normal'))

model.compile(loss='mean_squared_error', optimizer='adam')

print("\nStarting training...")
model_history = model.fit(X_train, y_train, batch_size=10, epochs=100, verbose=1)

model.summary()

Y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, Y_pred)

print(f"\nMean Absolute Error: {mae}")
print(f"Estimated Accuracy: {1 - mae}")