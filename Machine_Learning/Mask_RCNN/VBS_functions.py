#Dependencies
import cv2
import numpy as np
import matplotlib.pyplot as plt
from pixellib.instance import custom_segmentation
from math import sqrt
import tensorflow as tf

#Variables
rgb = np.zeros((3, 25))
meanR = np.array([])
meanG = np.array([])
meanB = np.array([])
moistureLevel = np.array([])

### COLORS FOR IDEAL COLOR CODES
COLORS = (
    (255, 221, 53),
    (151, 169, 38)
)

#Segmentation setup and loading model
SG_segmentation = custom_segmentation()
SG_segmentation.inferConfig(num_classes= 2, class_names= ["BG", "indicator", "glass"])
SG_segmentation.load_model("mask_rcnn_models/mask_rcnn_model.023-0.141302.h5")


#Ploting function for the R
def plotRGBValues(meanR, meanG, meanB, moistureLevel, samples):
    #x = np.linspace(0,100,samples)
    x = np.linspace(0,samples,samples)
    plt.plot(x, meanR, color="red")
    plt.plot(x, meanG, color="green")
    plt.plot(x, meanB, color="blue")
    plt.plot(x, moistureLevel, color="black")
    #plt.xlim([0, 100])
    plt.xlabel("Image number")
    plt.ylim([0, 270])
    plt.ylabel("RGB values")
    plt.savefig('MoistureLevel.png')
    plt.show()

def crop_RGB(image):
    img = image
    height, width, channels = img.shape

    #Finding coordinates
    rect_width = int(width/2.2)
    rect_height = int(height/2.2)
    x1 , y1 = int(rect_width) , int(rect_height)
    x2 , y2 = int(1.3*rect_width) , int(1.3*rect_height)

    #Cropped image
    crop_img = img[y1:y2, x1:x2]

    #The RGB value
    color = cv2.mean(crop_img)
    return color[2], color[1], color[0], crop_img

def closest_color(r, g, b):
    #r, g, b = rgb
    color_diffs = []
    for color in COLORS:
        cr, cg, cb = color
        color_diff = sqrt(abs(r - cr)**2 + abs(g - cg)**2 + abs(b - cb)**2)
        #print('Color difference: ' + str(color_diff))
        color_diffs.append((color_diff, color))
    return (color_diffs)[0][0], (color_diffs)[1][0]

def moisture_detect(indic_img):
    currentR, currentG, currentB, crop_png = crop_RGB(indic_img)
    closestColor = closest_color(currentR, currentG, currentB)
    yellowColorPercentage = closestColor[1] / (closestColor[0] + closestColor[1])
    yellowColorPercentage = round(yellowColorPercentage * 100, 2)
    print("Moisture percentage is: " + str(yellowColorPercentage) + "%")
    return yellowColorPercentage

def quality_detect(indic_img, indGlasBub_img,bubl_img):
    indic_img = cv2.cvtColor(indic_img, cv2.COLOR_BGR2GRAY)
    indGlasBub_img = cv2.cvtColor(indGlasBub_img, cv2.COLOR_BGR2GRAY)
    bubl_img = cv2.cvtColor(bubl_img, cv2.COLOR_BGR2GRAY)

    indic_pxl = cv2.countNonZero(indic_img)
    indGlasBub_pxl = cv2.countNonZero(indGlasBub_img)
    bubl_pxl = cv2.countNonZero(bubl_img)

    glass_pxl = indGlasBub_pxl - indic_pxl
    quality = round(((bubl_pxl / glass_pxl) * 100), 2)
    print("The refrigerant quality is " + str(quality) + "%")
    return quality





