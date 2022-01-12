import cv2.cv2

from CircleCalculations import areaOfCircle
from CircleDetection import detectCircle
from isolateIndicatorAndGlass import isolateIndicatorAndGlass
from detectMeanRGB import calculateMeanRGB
from detectMeanRGB import closest_color
from plotting import plotRGBValues
from plotting import plotQuality
from bubbleDetection import returnMarkedBubbles
import numpy as np
import cv2
import os
import glob
import time
import datetime
import math
from math import sqrt
from matplotlib import image
from matplotlib import pyplot as plt
from matplotlib.pyplot import hsv
from PIL import Image, ImageEnhance
import matplotlib.ticker as mtick
from init_readColor import readColor


# SETUP FOR GPIO PIN FOR MOISTURE PERCENTAGE INDICATION
import RPi.GPIO as GPIO
LED_PIN = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)

image_yellow = cv2.imread("Images/Danfoss/Documentation_NewSystem_Numbered/Image (1).jpg") # load reference image with green indicator here
image_green = cv2.imread("Images/Danfoss/Documentation_NewSystem_Numbered/Image (1).jpg")  # load reference image with yellow indicator here
readColor(image_green)  # for verifying the green color is detected correctly
readColor(image_yellow) # for verifying the yellow color is detected correctly



# FOR TESTING THE ALGORITHM WITH A FOLDER OF NUMBERED IMAGES
time.sleep(2)
imgSearcher = 0
images = []
while imgSearcher < 365:
    img = cv2.imread("E:/DetectionSystem_Test3/Numbered/Image (" + str(imgSearcher) + ").jpg")
    if img is not None:
        images.append(img)
    imgSearcher = imgSearcher + 1
print(len(images)) # for verifying that the expected amount of images have been loaded

time.sleep(5)

# INITIALIZATION PROCEDURE
init_image = cv2.imread("Images/Danfoss/REF.jpg") # load a reference image without gas bubbles here
isolatedGlass, maskGlass, indicator_x1, indicator_y1, indicator_x2, indicator_y2 = isolateIndicatorAndGlass(init_image)
referenceGlass = isolatedGlass.copy()
referenceGlass_grayscale = cv2.cvtColor(referenceGlass, cv2.COLOR_BGR2GRAY)
maskGlass_grayscale = cv2.cvtColor(maskGlass, cv2.COLOR_BGR2GRAY)
bubblesMaxDifference = cv2.countNonZero(maskGlass_grayscale) # the total amount of pixels within the glass frame
previousGlass = init_image.copy() # for initializing the previousGlass image
time.sleep(2)

imgCounter = 0
startTime = time.time()

# INITIALIZING ARRAYS FOR APPENDING THE DETECTED VALUES FOR PLOTTING
bubblePercentages = np.array([])
meanRval = np.array([])
meanBval = np.array([])
meanGval = np.array([])
moistureLevel = np.array([])
computationTime = np.array([])

while (__name__ == '__main__') and (imgCounter < 240):
    currentImage = images[imgCounter]
    print("-----------------------------------")
    print("IMAGE LOADED: ImageNumber" + str(imgCounter))

    # ISOLATE COLOR AND CALCULATE MOISTURE LEVEL
    rectangularIndicator = currentImage[indicator_y1:indicator_y2, indicator_x1:indicator_x2]
    meanR, meanG, meanB = calculateMeanRGB(rectangularIndicator)
    print("Mean RGB: " + str(meanR) + ", " + str(meanG) + "," + str(meanB))
    closestColor = closest_color(meanR, meanG, meanB)
    print(closestColor)
    yellowColorPercentage = closestColor[1] / (closestColor[0] + closestColor[1])
    yellowColorPercentage = round(yellowColorPercentage*100, 2)
    print("Moisture percentage is: " + str(yellowColorPercentage) + "%")
    meanRval = np.append(meanRval,meanR)
    meanBval = np.append(meanBval, meanB)
    meanGval = np.append(meanGval, meanG)
    moistureLevel = np.append(moistureLevel, int(yellowColorPercentage))

    # EXTRACT GLASS SECTION AND CALCULATE BUBBLE PERCENTAGE
    currentGlass = cv2.bitwise_and(currentImage, maskGlass)
    markedBubbles1 = returnMarkedBubbles(referenceGlass, currentGlass, 10)   # For empty glass as reference
    markedBubbles2 = returnMarkedBubbles(previousGlass, currentGlass, 7)     # For previous glass as reference
    markedBubbles = cv2.bitwise_and(markedBubbles1, markedBubbles2)
    nonZeroPixels = cv2.countNonZero(markedBubbles)
    previousGlass = currentGlass
    print("Nonzeropixels:             " + str(nonZeroPixels))
    print("Maximum pixels:              " + str(bubblesMaxDifference))
    bubblesPct = round((nonZeroPixels/bubblesMaxDifference)*100, 2)
    print("Bubbles percentage:         " + str((bubblesPct)) + " %")
    #if imgCounter > 0:

    bubblePercentages = np.append(bubblePercentages, bubblesPct) # Adding the detected bubble percentage to array for plotting

    # NOTING THE PROCESSING TIME FOR EACH IMAGE
    currentComputationTime = time.time()
    computationTime = np.append(computationTime, currentComputationTime)

    imgCounter = imgCounter + 1
    time.sleep(1.0 - ((time.time() - startTime) % 1.0)) #Command for calling main function every 1s


# Printing the computation time for each of the first 10 images
print("Computation times:")
timeElapsed1 = computationTime[0] - startTime
timeElapsed2 = computationTime[1] - computationTime[0]
timeElapsed3 = computationTime[2] - computationTime[1]
timeElapsed4 = computationTime[3] - computationTime[2]
timeElapsed5 = computationTime[4] - computationTime[3]
timeElapsed6 = computationTime[5] - computationTime[4]
timeElapsed7 = computationTime[6] - computationTime[5]
timeElapsed8 = computationTime[7] - computationTime[6]
timeElapsed9 = computationTime[8] - computationTime[7]
timeElapsed10 = computationTime[9] - computationTime[8]
print(timeElapsed1)
print(timeElapsed2)
print(timeElapsed3)
print(timeElapsed4)
print(timeElapsed5)
print(timeElapsed6)
print(timeElapsed7)
print(timeElapsed8)
print(timeElapsed9)
print(timeElapsed10)

# Plotting the detected amount of bubbles
plotQuality(bubblePercentages, imgCounter, 1)

time.sleep(5)

# Averaging the amount of bubbles detected over every 10 samples
avgElements = 10
avgResult = np.average(bubblePercentages.reshape(-1, avgElements), axis=1)
print("Averaging over every ", avgElements, " elements of a numpy array:")
plotQuality(avgResult, 24, 2)

time.sleep(5)

# Averaging the amount of bubbles detected over every 3 samples
avgElements = 3
avgResult2 = np.average(bubblePercentages.reshape(-1, avgElements), axis=1)
print("Averaging over every ", avgElements, " elements of a numpy array:")
plotQuality(avgResult2, 80, 3)

# Print the detected amount of bubbles and export as .csv file for validation
bubblePercentages.tofile('BubbleData.csv', sep = ',')