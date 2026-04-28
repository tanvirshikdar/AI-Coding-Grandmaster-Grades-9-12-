import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

file_path = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 20 (Deep Learning - I)\Lesson 6 (ANN Implementation using Keras – 2)\ACP (Legendary Pokemon Prediction using ANN)\dataset.csv"

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
else:
    df = pd.read_csv("dataset.csv")

le = LabelEncoder()
for col in df.select_dtypes(include=['object']).columns:
    df[col] = le.fit_transform(df[col])

if 'is_legendary' in df.columns:
    target = 'is_legendary'
elif 'legendary' in df.columns:
    target = 'legendary'
else:
    target = df.columns[-1]

y = df.pop(target)
X = df

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

model = Sequential()
model.add(Dense(units=12, kernel_initializer='he_uniform', activation='relu', input_dim=X_train.shape[1]))
model.add(Dense(units=8, kernel_initializer='he_uniform', activation='relu'))
model.add(Dense(units=1, kernel_initializer='glorot_uniform', activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(X_train, y_train, batch_size=10, epochs=100, verbose=1)

model.summary()

y_pred = model.predict(X_test)
y_pred = (y_pred > 0.5)

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print(f"Accuracy Score: {accuracy_score(y_test, y_pred)}")