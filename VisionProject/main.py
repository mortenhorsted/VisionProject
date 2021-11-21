from CircleCalculations import areaOfCircle
from CircleDetection import detectCircle, justDetectCircle
from isolateIndicatorAndGlass import isolateIndicatorAndGlass
from detectMeanRGB import calculateMeanRGB
from detectMeanRGB import closest_color
from plotRGBValues import plotRGBValues
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
import matplotlib.ticker as mtick

from proofOfConcept import showProofOfConcept
#showProofOfConcept()





# INITIALIZATION PROCEDURE
init_image = cv2.imread("Images/RPI_Images/Bubbles/ImageNumber0.png")
isolatedGlass, maskGlass, indicator_x1, indicator_y1, indicator_x2, indicator_y2 = isolateIndicatorAndGlass(init_image)
referenceGlass = isolatedGlass.copy()
referenceGlass_grayscale = cv2.cvtColor(referenceGlass, cv2.COLOR_BGR2GRAY)
maskGlass_grayscale = cv2.cvtColor(maskGlass, cv2.COLOR_BGR2GRAY)
bubblesMaxDifference = cv2.countNonZero(maskGlass_grayscale)
time.sleep(2)


imgCounter = 0                                                                  #TEST VALUE: for inputting next image number
startTime = time.time()


while (__name__ == '__main__') and (imgCounter < 8):
    currentImage = cv2.imread("Images/RPI_Images/Bubbles/ImageNumber" + str(imgCounter) + ".png")
    print("")
    print("")
    print("")
    print("-----------------------------------")
    print("----- IMAGE LOADED: ImageNumber" + str(imgCounter))
    print("-----------------------------------")


    # ISOLATE COLOR AND READ RGB VALUE
    rectangularIndicator = currentImage[indicator_y1:indicator_y2, indicator_x1:indicator_x2]
    cv2.imwrite("Images/RPI_Images/Bubbles/Indicators/IsolatedIndicator_ImageNumber" + str(imgCounter) + ".png", rectangularIndicator)
    meanR, meanG, meanB = calculateMeanRGB(rectangularIndicator)
    closestColor = closest_color(meanR, meanG, meanB)
    yellowColorPercentage = closestColor[1] / (closestColor[0] + closestColor[1])
    print("Yellow color percentage is: ", yellowColorPercentage)


    # EXTRACT GLASS SECTION AND COMPARE
    currentGlass = cv2.bitwise_and(currentImage, referenceGlass)
    currentGlass_grayscale = cv2.cvtColor(currentGlass, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("Images/RPI_Images/Bubbles/Glasses/IsolatedGlass_ImageNumber" + str(imgCounter) + ".png", currentGlass_grayscale)

    bubblePixelDifference = np.sum(referenceGlass_grayscale != currentGlass_grayscale)
    bubblePercentageDecimal = bubblePixelDifference/bubblesMaxDifference
    bubblePercentage = round(bubblePercentageDecimal*100)


    #print("Bubbles 30 pct - difference is: " + str(diffBubbles30pct))
    print("Bubbles - difference in percent is: " + str(bubblePercentage) + "%")

    #cv2.imshow("current Glass", currentGlass_grayscale)
    #cv2.imshow("ref Glass", referenceGlass_grayscale)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    imgCounter = imgCounter + 1
    #time.sleep(2.0 - ((time.time() - startTime) % 2.0))                         #Command for calling main function every 1s


