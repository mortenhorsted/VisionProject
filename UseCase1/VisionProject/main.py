import cv2.cv2

from CircleCalculations import areaOfCircle
from CircleDetection import detectCircle, justDetectCircle
from isolateIndicatorAndGlass import isolateIndicatorAndGlass
from detectMeanRGB import calculateMeanRGB
from detectMeanRGB import closest_color
from plotting import plotRGBValues
from bubbleDetection import returnMarkedBubbles
import numpy as np
import cv2
import os
import glob
import time
import math
from math import sqrt
from matplotlib import image
from matplotlib import pyplot as plt
from matplotlib.pyplot import hsv
from PIL import Image, ImageEnhance
import matplotlib.ticker as mtick
from init_readColor import readColor

# SETUP GPIO PIN
#import RPi.GPIO as GPIO
LED_PIN = 26
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)


image_yellow = cv2.imread("Images/RealImages/v5/ImageNumber0.jpg")
image_green = cv2.imread("Images/RealImages/v5/ImageNumber0.jpg")
#readColor(image_green)
#readColor(image_yellow)


#time.sleep(5)


# INITIALIZATION PROCEDURE

#init_image = cv2.imread("Images/RPI_Images/Colorchanging/ImageNumber0.jpg")
#init_image = cv2.imread("Images/RealImages/ExtractedImages/ImageNumber0.png")
def detectCircle2(image, minRadius, maxRadius):
    minDist = 100
    param1 = 30  ##30## 500
    param2 = 50  ##50## 200 #smaller value-> more false circles"
    #WORKING FOR TEST IMAGES:
            #    param1 = 35  ##30## 500
            #    param2 = 65  ##50## 200 #smaller value-> more false circles"
    # minRadius = 5
    # maxRadius = 170 #10

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blurred = cv2.medianBlur(gray, 25)  # cv2.bilateralFilter(gray,10,50,50)


    # docstring of HoughCircles: HoughCircles(image, method, dp, minDist[, circles[, param1[, param2[, minRadius[, maxRadius]]]]]) -> circles
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, minDist, param1=param1, param2=param2,
                               minRadius=minRadius, maxRadius=maxRadius)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            cv2.circle(image, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # print('Radius of outer circle is: ', i[2])
            return i[0],i[1],i[2]

#init_image = cv2.imread("Images/Danfoss/ImageNumber00001.png")
init_image = cv2.imread("Images/SelfBubbles/ImageNumber0.jpg")
cv2.imshow("INITIMAGE1", init_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
detectCircle2(init_image,100,200)
cv2.imshow("INITIMAGE", init_image)




isolatedGlass, maskGlass, indicator_x1, indicator_y1, indicator_x2, indicator_y2 = isolateIndicatorAndGlass(init_image)
referenceGlass = isolatedGlass.copy()
referenceGlass_grayscale = cv2.cvtColor(referenceGlass, cv2.COLOR_BGR2GRAY)
maskGlass_grayscale = cv2.cvtColor(maskGlass, cv2.COLOR_BGR2GRAY)
bubblesMaxDifference = cv2.countNonZero(maskGlass_grayscale)
time.sleep(2)


imgCounter = 1                                                               #TEST VALUE: for inputting next image number
startTime = time.time()

bubblePercentages = np.array([])
meanRval = np.array([])
meanBval = np.array([])
meanGval = np.array([])
while (__name__ == '__main__') and (imgCounter < 40):
    currentImage = cv2.imread("Images/Danfoss/ImageNumber0000" + str(imgCounter) + ".png")
    currentImage = cv2.imread("Images/SelfBubbles/ImageNumber" + str(imgCounter) + ".png")
    #currentImage = cv2.imread("Images/RPI_Images/RPI_BubbleManipulation/Image" + str(imgCounter) + ".png")
    #currentImage = cv2.imread("Images/RPI_Images/Colorchanging/ImageNumber" + str(imgCounter) + ".jpg")
    #cv2.imshow("current image", currentImage)

    print("")
    print("-----------------------------------")
    print("----- IMAGE LOADED: ImageNumber" + str(imgCounter))
    print("-----------------------------------")


    # ISOLATE COLOR AND READ RGB VALUE
    #isolatedIndicator = cv2.bitwise_and(currentImage, halvedMaskIndicator)
    rectangularIndicator = currentImage[indicator_y1:indicator_y2, indicator_x1:indicator_x2]
    #cv2.imwrite("Images/RPI_Images/RPI_BubbleManipulation/IsoIndicators/Image" + str(imgCounter) + ".png", isolatedIndicator)
    meanR, meanG, meanB = calculateMeanRGB(rectangularIndicator)
    closestColor = closest_color(meanR, meanG, meanB)
    #print("RGB value for the indicator is: ", meanR, meanG, meanB)
    yellowColorPercentage = closestColor[1] / (closestColor[0] + closestColor[1])
    #cv2.imshow("Isolated indicator", isolatedIndicator)
    yellowColorPercentage = round(yellowColorPercentage*100)
    print("Yellow color percentage is: " + str(yellowColorPercentage) + "%")


    meanRval = np.append(meanRval,meanR)
    meanBval = np.append(meanBval, meanB)
    meanGval = np.append(meanGval, meanG)

    # EXTRACT GLASS SECTION AND COMPARE
    currentGlass = cv2.bitwise_and(currentImage, maskGlass)
    markedBubbles = returnMarkedBubbles(referenceGlass, currentGlass)
    nonZeroPixels = cv2.countNonZero(markedBubbles)



    print("Nonzeropixels:             " + str(nonZeroPixels))

    print("Maximum pixels:              " + str(bubblesMaxDifference))
    #markedBubbles = cv2.cvtColor(markedBubbles, cv2.COLOR_BGR2GRAY)



    bubblesPct = round((nonZeroPixels/bubblesMaxDifference)*100, 2)
    print("Bubbles percentage:         " + str((bubblesPct)) + " %")
    bubblePercentages = np.append(bubblePercentages, bubblesPct)






    cv2.imshow("Marked bubbles", markedBubbles)
    cv2.imshow("Isolated glass", currentGlass)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    imgCounter = imgCounter + 1
    #time.sleep(1.0 - ((time.time() - startTime) % 1.0))                         #Command for calling main function every 1s


#plotRGBValues(meanR, meanG, meanB, imgCounter