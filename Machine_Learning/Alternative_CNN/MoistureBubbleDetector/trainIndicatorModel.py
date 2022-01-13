from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from tensorflow.keras.optimizers import RMSprop
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import os

train = ImageDataGenerator(rescale=1 / 255)
validation = ImageDataGenerator(rescale=1 / 255)

train_dataset = train.flow_from_directory('indicator/dataBase/training/',
                                          target_size=(200, 200),
                                          batch_size=3,
                                          class_mode='binary')
validation_dataset = train.flow_from_directory('indicator/dataBase/validation/',
                                               target_size=(200, 200),
                                               batch_size=3,
                                               class_mode='binary')
train_dataset.class_indices
{'DRY': 0, 'WET': 1}

model_indicator = tf.keras.models.Sequential([tf.keras.layers.Conv2D(16, (3, 3), activation='relu', input_shape=(200, 200, 3)),
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
model_indicator.compile(loss='binary_crossentropy',
              optimizer=RMSprop(lr=0.001),
              metrics=['accuracy'])
model_fit = model_indicator.fit(train_dataset,
                      steps_per_epoch=5,
                      epochs=30,
                      validation_data=validation_dataset)

model_indicator.save('trained_models/indicator/model_indicator_3.h5')

dir_path = 'indicator/dataBase/testing'
for i in os.listdir(dir_path):
    img = image.load_img(dir_path + '//' + i, target_size=(200, 200))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])
    val = model_indicator.predict(images)

    #print(val)
    if val == 0:
        print(i + ': WET')
    else:
        print(i + ': DRY')


