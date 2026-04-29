import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Input, Dense, Flatten, Dropout, Conv2D, MaxPooling2D
from tensorflow.keras.constraints import MaxNorm
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.optimizers import SGD
import matplotlib.pyplot as plt
import numpy as np

# 1. Import Dataset
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# Plot first few images
for i in range(9):
    plt.subplot(330 + 1 + i)
    plt.imshow(x_train[i])
plt.show()

# 2. Preprocess dataset
num_classes = 10
y_train = to_categorical(y_train, num_classes)
y_test = to_categorical(y_test, num_classes)

x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255

# 3. Model Building
model = Sequential()
model.add(Input(shape=(32, 32, 3)))
model.add(Conv2D(32, (3, 3), activation='relu', padding='same')) 
model.add(Dropout(0.2)) 
model.add(Conv2D(32, (3, 3), activation='relu', padding='same')) 
model.add(MaxPooling2D(pool_size=(2, 2))) 
model.add(Conv2D(64, (3, 3), activation='relu', padding='same')) 
model.add(Dropout(0.2)) 
model.add(Conv2D(64, (3, 3), activation='relu', padding='same')) 
model.add(MaxPooling2D(pool_size=(2, 2))) 
model.add(Conv2D(128, (3, 3), activation='relu', padding='same')) 
model.add(Dropout(0.2)) 
model.add(Conv2D(128, (3, 3), activation='relu', padding='same')) 
model.add(MaxPooling2D(pool_size=(2, 2))) 
model.add(Flatten()) 
model.add(Dropout(0.2)) 
model.add(Dense(1024, activation='relu', kernel_constraint=MaxNorm(3))) 
model.add(Dropout(0.2)) 
model.add(Dense(512, activation='relu', kernel_constraint=MaxNorm(3))) 
model.add(Dropout(0.2)) 
model.add(Dense(num_classes, activation='softmax'))

# 4. Model Compilation
opt = SGD(learning_rate=0.01, momentum=0.9, nesterov=False)
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])

# 5. Model Training (Set to 1 epoch for testing)
model.fit(x_train, y_train, batch_size=32, epochs=1, verbose=1, validation_data=(x_test, y_test))
print("The model has successfully trained")

model.save('classifier.h5')
print("Saving the model as classifier.h5")

# 6. Prediction Logic
def load_image(filename):
    img = load_img(filename, target_size=(32, 32))
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0) 
    return img

def run_example():
    try:
        # ABSOLUTE PATH FIX HERE:
        img_path = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 21 (Deep Learning - II)\Lesson 4 (Image classifier using CNN part – 2)\Activity 1 (Image Classification using CNN - Part 2)\image.jpg"
        
        img = load_image(img_path)
        model = load_model('classifier.h5')
        result = model.predict(img)
        
        # In multi-class, we look for the index with the highest probability
        prediction = np.argmax(result)
        classes = ["Aeroplane", "Automobile", "Bird", "Cat", "Deer", "Dog", "Frog", "Horse", "Ship", "Truck"]
        
        print(f"\nPrediction Result: {classes[prediction]}")
        print(f"Probabilities: {result}")
        
    except FileNotFoundError:
        print("\n[ERROR] Could not find the image. Please verify the absolute path.")

run_example()