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
import time

def performAlgorithm(capturedImage, referenceImage, referenceMaxDifference):

    #------- INPUT IMAGE: ---------------
    #sightglassCaptured = cv2.imread("Images/TESTING/SG_Middle_50pctBubbly.png")
    #------------------------------------

    #referenceImageNoBubbles = cv2.imread("Images/TESTING/referenceImageForPOC.png")

    isolatedIndicator, isolatedGlass, rectangularIndicator, maxDifferenceMask = isolateIndicatorAndGlass(capturedImage)
    #cv2.imwrite("Images/TESTING/referenceImageForPOC.png", isolatedGlass)

    #cv2.imshow("Image captured from camera: ", capturedImage)
    cv2.imshow("The isolated indicator: ", isolatedIndicator)
#    cv2.imshow("The isolated glass frame as reference: ", isolatedGlass)
    #cv2.imshow("The rectangle used for color detection: ", rectangularIndicator)



#    input("Press Enter to continue...")
#    print("Performing indicator calculations..")

    meanR, meanG, meanB = calculateMeanRGB(rectangularIndicator)
    closestColor = closest_color(meanR, meanG, meanB)
    yellowColorPercentage = closestColor[1]/(closestColor[0]+closestColor[1])
#    print("Yellow color change percentage: " + str(yellowColorPercentage))
#    print("------------------------")
#    input("Press Enter to continue...")

#    cv2.imshow("The reference image of the glass: ", referenceImage)
#    cv2.imshow("Mask of all pixels inside the isolated glass: ", maxDifferenceMask)
    cv2.imshow("The isolated glass frame: ", isolatedGlass)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    maximumDifference = np.sum(referenceImage != referenceMaxDifference)
#    print("The maximum difference is: " + str(maximumDifference))

    diffBubbles = np.sum(referenceImage != isolatedGlass)
    differenceInPercent = diffBubbles/maximumDifference
#    print("The amount of pixels that are different from the reference: " + str(diffBubbles))
#    print("The difference in percent is: " + str(differenceInPercent) + "%")

#    input("Press Enter to continue...")

    return yellowColorPercentage, differenceInPercent


def showProofOfConcept():

    bubbleMeasurements = np.zeros(10)


    sleepyTime1 = 2
    sleepyTime2 = 2

    initialSG = cv2.imread("Images/TESTING/SG_Green.png")
    isolatedIndicator, isolatedGlass, rectangularIndicator, maxDifferenceMask = isolateIndicatorAndGlass(initialSG)
    referenceGlass = isolatedGlass.copy()
    referenceMaxDiff = maxDifferenceMask.copy()

    print("Reference image loaded.")

    print("-------------------------------------")
    print("-------------------------------------")

    time.sleep(sleepyTime1)
    print("Loading image of sight glass: Green, no bubbles")
    time.sleep(sleepyTime1)
    capturedImage = cv2.imread("Images/TESTING/SG_Green.png")
#    cv2.imshow("Loaded image: green, no bubbles", capturedImage)
    capturedImg_yellowColorPercentage, capturedImg_differenceInPercent = performAlgorithm(capturedImage, referenceGlass, referenceMaxDiff)
    print("The sight glass indicates a moisture level of: " + str(capturedImg_yellowColorPercentage))
    print("The sight glass indicates a bubble level of: " + str(capturedImg_differenceInPercent))
    bubbleMeasurements[0] = capturedImg_differenceInPercent
    time.sleep(sleepyTime2)

    print("-------------------------------------")
    print("-------------------------------------")

    print("Loading image of sight glass: 50% yellow/green, no bubbles")
    time.sleep(sleepyTime1)
    capturedImage = cv2.imread("Images/TESTING/SG_Middle.png")
#    cv2.imshow("Loaded image: both, no bubbles", capturedImage)
    capturedImg_yellowColorPercentage, capturedImg_differenceInPercent = performAlgorithm(capturedImage, referenceGlass, referenceMaxDiff)
    print("The sight glass indicates a moisture level of: " + str(capturedImg_yellowColorPercentage))
    print("The sight glass indicates a bubble level of: " + str(capturedImg_differenceInPercent))
    bubbleMeasurements[1] = capturedImg_differenceInPercent
    time.sleep(sleepyTime2)

    print("-------------------------------------")
    print("-------------------------------------")

    print("Loading image of sight glass: Yellow, no bubbles")
    time.sleep(sleepyTime1)
    capturedImage = cv2.imread("Images/TESTING/SG_Yellow.png")
#    cv2.imshow("Loaded image: yellow, no bubbles", capturedImage)
    capturedImg_yellowColorPercentage, capturedImg_differenceInPercent = performAlgorithm(capturedImage, referenceGlass, referenceMaxDiff)
    print("The sight glass indicates a moisture level of: " + str(capturedImg_yellowColorPercentage))
    print("The sight glass indicates a bubble level of: " + str(int(capturedImg_differenceInPercent)))
    bubbleMeasurements[2] = capturedImg_differenceInPercent
    time.sleep(sleepyTime2)

    print("-------------------------------------")
    print("-------------------------------------")

    print("Loading image of sight glass: Both, some bubbles")
    time.sleep(sleepyTime1)
    capturedImage = cv2.imread("Images/TESTING/SG_Bubbles0.png")
#    cv2.imshow("Loaded image: both, some bubbles", capturedImage)
    capturedImg_yellowColorPercentage, capturedImg_differenceInPercent = performAlgorithm(capturedImage, referenceGlass, referenceMaxDiff)
    print("The sight glass indicates a moisture level of: " + str(capturedImg_yellowColorPercentage))
    print("The sight glass indicates a bubble percentage of: " + str(capturedImg_differenceInPercent))
    bubbleMeasurements[3] = capturedImg_differenceInPercent
    time.sleep(sleepyTime2)

    print("-------------------------------------")
    print("-------------------------------------")

    print("Loading image of sight glass: Both, more bubbles")
    time.sleep(sleepyTime1)
    capturedImage = cv2.imread("Images/TESTING/SG_Bubbles1.png")
#    cv2.imshow("Loaded image: Both, more bubbles", capturedImage)
    capturedImg_yellowColorPercentage, capturedImg_differenceInPercent = performAlgorithm(capturedImage, referenceGlass, referenceMaxDiff)
    print("The sight glass indicates a moisture level of: " + str(capturedImg_yellowColorPercentage))
    print("The sight glass indicates a bubble level of: " + str(capturedImg_differenceInPercent))
    bubbleMeasurements[4] = capturedImg_differenceInPercent
    time.sleep(sleepyTime2)

    print("-------------------------------------")
    print("-------------------------------------")

    print("Loading image of sight glass: Both, more more bubbles")
    time.sleep(sleepyTime1)
    capturedImage = cv2.imread("Images/TESTING/SG_Bubbles2.png")
#    cv2.imshow("Loaded image: Both, more more bubbles", capturedImage)
    capturedImg_yellowColorPercentage, capturedImg_differenceInPercent = performAlgorithm(capturedImage, referenceGlass, referenceMaxDiff)
    print("The sight glass indicates a moisture level of: " + str(capturedImg_yellowColorPercentage))
    print("The sight glass indicates a bubble level of: " + str(capturedImg_differenceInPercent))
    bubbleMeasurements[5] = capturedImg_differenceInPercent
    time.sleep(sleepyTime2)

    print("-------------------------------------")
    print("-------------------------------------")

    print("Loading image of sight glass: Both, more more more bubbles")
    time.sleep(sleepyTime1)
    capturedImage = cv2.imread("Images/TESTING/SG_Bubbles3.png")
#    cv2.imshow("Loaded image: Both, more more more bubbles", capturedImage)
    capturedImg_yellowColorPercentage, capturedImg_differenceInPercent = performAlgorithm(capturedImage, referenceGlass, referenceMaxDiff)
    print("The sight glass indicates a moisture level of: " + str(capturedImg_yellowColorPercentage))
    print("The sight glass indicates a bubble level of: " + str(capturedImg_differenceInPercent))
    bubbleMeasurements[6] = capturedImg_differenceInPercent
    time.sleep(sleepyTime2)
    time.sleep(3)

    print("-------------------------------------")
    print("-------------------------------------")
    print("-------------------------------------")
    print("Finished. Adjustments are needed, but proof of concept has been shown :)")
    print("-------------------------------------")
    #print(bubbleMeasurements)



