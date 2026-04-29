import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.utils import to_categorical
from numpy import argmax
import os

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
input_shape = (28, 28, 1)

y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255

model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=input_shape))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dense(10, activation='softmax'))

opt = SGD(learning_rate=0.01)
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])

model.fit(x_train, y_train, batch_size=128, epochs=10, verbose=1, validation_data=(x_test, y_test))

model.save('mnist_model.keras')

def load_image(filename):
    img = keras.utils.load_img(filename, color_mode="grayscale", target_size=(28, 28))
    img = keras.utils.img_to_array(img)
    img = img.reshape(1, 28, 28, 1)
    img = img.astype('float32') / 255.0
    return img

def run_example():
    image_path = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 21 (Deep Learning - II)\Lesson 6 (Let’s build digit recognizer- 2)\image.jpg"
    
    if os.path.exists(image_path):
        img = load_image(image_path)
        trained_model = load_model('mnist_model.keras')
        predict_value = trained_model.predict(img)
        digit = argmax(predict_value)
        print(f"Predicted Digit: {digit}")
    else:
        print(f"Error: {image_path} not found.")

run_example()