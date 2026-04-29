import tensorflow as tf
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
import numpy as np

dataset_path = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 21 (Deep Learning - II)\Lesson 3 (Image classifier using CNN part – 1)\ACP (Classify whether Cat or Dog)\dataset"

datagen = ImageDataGenerator(rescale=1.0/255.0, validation_split=0.2)

print("Loading Training Data:")
train_generator = datagen.flow_from_directory(
    dataset_path,
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary',
    subset='training'
)

print("\nLoading Validation Data:")
validation_generator = datagen.flow_from_directory(
    dataset_path,
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary',
    subset='validation'
)

print("\nClass Mappings:", train_generator.class_indices)

model = Sequential([
    Input(shape=(150, 150, 3)),
    Conv2D(32, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    
    Flatten(),
    
    Dense(512, activation='relu'),
    Dropout(0.5),
    
    Dense(1, activation='sigmoid')
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

print("\nTraining the model...")
history = model.fit(
    train_generator,
    validation_data=validation_generator,
    epochs=1, 
    verbose=1
)

model.save('cat_dog_classifier.h5')
print("\nModel saved as cat_dog_classifier.h5")

print("\nEvaluating model performance...")
score = model.evaluate(validation_generator, verbose=0)
print('Validation loss:', score[0])
print('Validation accuracy:', score[1])

def load_image(filename):
    img = load_img(filename, target_size=(150, 150))
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0) 
    img = img / 255.0 
    return img

def run_example():
    try:
        # Absolute path to the test image
        img_path = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 21 (Deep Learning - II)\Lesson 4 (Image classifier using CNN part – 2)\ACP (Classify whether Cat or Dog)\image.jpg"
        
        img = load_image(img_path)
        loaded_model = load_model('cat_dog_classifier.h5')
        result = loaded_model.predict(img)
        
        print("\nPrediction Raw Value:", result[0][0])
        if result[0][0] > 0.5: 
            print("Final Prediction: Dog") 
        else: 
            print("Final Prediction: Cat") 
            
    except FileNotFoundError:
        print("\n[ERROR] Image not found. Please double-check the path provided in the run_example function.")

run_example()