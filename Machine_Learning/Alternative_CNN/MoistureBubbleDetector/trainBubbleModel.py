from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from tensorflow.keras.optimizers import RMSprop
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import os

train = ImageDataGenerator(rescale=1 / 255)
validation = ImageDataGenerator(rescale=1 / 255)

train_dataset_bubble = train.flow_from_directory('bubbles/dataBase/training/',
                                          target_size=(200, 200),
                                          batch_size=3,
                                          class_mode='binary')

validation_dataset_bubble = train.flow_from_directory('bubbles/dataBase/validation/',
                                               target_size=(200, 200),
                                               batch_size=3,
                                               class_mode='binary')

train_dataset_bubble.class_indices
{'No bubbles': 0, 'Bubbles': 1}

model_bubbles = tf.keras.models.Sequential([tf.keras.layers.Conv2D(16, (3, 3), activation='relu', input_shape=(200, 200, 3)),
                                    tf.keras.layers.MaxPool2D(2, 2),
                                    #
                                    tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
                                    tf.keras.layers.MaxPool2D(2, 2),
                                    #
                                    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
                                    tf.keras.layers.MaxPool2D(2, 2),
                                    ##
                                    tf.keras.layers.Flatten(),
                                    tf.keras.layers.Dense(512, activation='relu'),
                                    tf.keras.layers.Dense(1, activation='sigmoid')
                                    ]
                                   )
model_bubbles.compile(loss='binary_crossentropy',
              optimizer=RMSprop(learning_rate=0.001),
              metrics=['accuracy'])


model_fit = model_bubbles.fit(train_dataset_bubble,
                      steps_per_epoch=14,
                      epochs=70,
                      validation_data=validation_dataset_bubble)

model_bubbles.save('trained_models/bubble/model_bubble_6.h5')

model_bubbles = tf.keras.models.load_model("trained_models/bubble/model_bubble_6.h5")
#dir_path = 'Final_test/testing'
dir_path = 'bubbles/dataBase/testing'
for i in os.listdir(dir_path):
    img = image.load_img(dir_path + '//' + i, target_size=(200, 200))
    plt.imshow(img)
    plt.show()

    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])
    val = model_bubbles.predict(images)

    if val == 0:
        print(i + ': Bubbles')
    else:
        print(i + ': No bubbles')