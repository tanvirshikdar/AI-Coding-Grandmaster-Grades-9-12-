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

(x_train, y_train), (x_test, y_test) = cifar10.load_data()

for i in range(9):
    plt.subplot(330 + 1 + i)
    plt.imshow(x_train[i])

plt.show()

num_classes = 10
y_train = to_categorical(y_train, num_classes)
y_test = to_categorical(y_test, num_classes)

x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255

print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

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

print(model.summary())

opt = SGD(learning_rate=0.01, momentum=0.9, decay=0.0002, nesterov=False)
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])

classifer = model.fit(x_train, y_train, batch_size=32, epochs=1, verbose=1, validation_data=(x_test, y_test))
print("The model has successfully trained")

model.save('classifier.h5')
print("Saving the model as classifier.h5")

score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

def load_image(filename):
    img = load_img(filename, target_size=(32, 32))
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0) 
    return img

def run_example():
    img = load_image('image.jpg')
    model = load_model('classifier.h5')
    result = model.predict(img)
    print(result)
    
    if result[0][0]==1: 
        print("Aeroplane") 
    elif result[0][1]==1: 
        print('Automobile') 
    elif result[0][2]==1: 
        print('Bird') 
    elif result[0][3]==1: 
        print('Cat') 
    elif result[0][4]==1: 
        print('Deer') 
    elif result[0][5]==1: 
        print('Dog') 
    elif result[0][6]==1: 
        print('Frog') 
    elif result[0][7]==1: 
        print('Horse') 
    elif result[0][8]==1: 
        print('Ship') 
    elif result[0][9]==1: 
        print('Truck') 
    else: 
        print('Error')

run_example()