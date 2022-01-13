#Dependencies
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import os

#Array for moisture and bubble values
bubble = np.array([])
moisture = np.array([])

#Visualization of the detection
def plotDetectedValues(val, samples, yLabel):
    x = np.linspace(275,360,samples)
    plt.plot(x, val, color="black")
    plt.xlim([275, 360])
    plt.xlabel("Image number")
    plt.ylim([0, 1.5])
    plt.ylabel(yLabel)
    plt.savefig('Test_Result_Alt_ML.png')
    plt.show()



#Load models
model_indicator = tf.keras.models.load_model("trained_models/indicator/model_indicator_3.h5")
model_bubbles = tf.keras.models.load_model("trained_models/bubble/model_bubble_6.h5")

#Test directory
dir_path = 'testing'

#Running test on images
count = 0
for i in os.listdir(dir_path):
    img = image.load_img(dir_path + '//' + i, target_size=(200, 200), interpolation='lanczos')

    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])
    val1 = model_indicator.predict(images)
    val2 = model_bubbles.predict(images)

    #Moisture detection
    if val1 == 0:
        print(i + ': WET')
    else:
        print(i + ': DRY')
    moisture = np.append(moisture, not val1)

    #Bubble detection
    if val2 == 0:
        print(i + ': Bubbles')
    else:
        print(i + ': No bubbles')
    bubble = np.append(bubble, not val2)
    count = count+1
#Visualizarion of test result
plotDetectedValues(bubble, count, 'Bubble detected')
#plotDetectedValues(moisture, count, 'Moisture detected')