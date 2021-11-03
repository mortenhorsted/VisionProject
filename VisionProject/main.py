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





######### PLOTTING SEQUENCE

#meanR = np.zeros(21)
#meanG = np.zeros(21)
#meanB = np.zeros(21)

#imgNumber = 1
#while imgNumber < 22:
#    imageSightGlass = cv2.imread("Images/NumberedImages/" + str(imgNumber) + ".png")
#    isolatedIndicator, isolatedGlass, rectangularIndicator = isolateIndicatorAndGlass(imageSightGlass)
#    cv2.imwrite('Images/NumberedImages/Masks/MaskedIndicator' + str(imgNumber) + '.png', rectangularIndicator)
#    meanR[imgNumber-1], meanG[imgNumber-1], meanB[imgNumber-1] = calculateMeanRGB(rectangularIndicator)
#    print("Image number: " + str(imgNumber))
#    closestColor = closest_color(meanR[imgNumber-1], meanG[imgNumber-1], meanB[imgNumber-1])
#    yellowColorPercentage = closestColor[1]/(closestColor[0]+closestColor[1])
#    print("Yellow color change percentage: " + str(yellowColorPercentage))
#    imgNumber = imgNumber + 1

#plotRGBValues(meanR, meanG, meanB, 21)

###########################


isolatedGlassReference = cv2.imread("Images/TESTING/CurrentTestImage.png")

isolatedIndicator, isolatedGlass, rectangularIndicator, maxDifferenceMask = isolateIndicatorAndGlass(isolatedGlassReference)
referenceImageNoBubbles = isolatedGlass.copy()
#cv2.imwrite("Images/Bubbles/IsolatedGlassNoBubbles.png", isolatedGlass)
Bubbles1 = cv2.imread("Images/Bubbles/1Bubble.png")
Bubbles2 = cv2.imread("Images/Bubbles/2Bubble.png")
Bubbles3 = cv2.imread("Images/Bubbles/3Bubble.png")
Bubbles4 = cv2.imread("Images/Bubbles/4Bubble.png")
Bubbles5 = cv2.imread("Images/Bubbles/5Bubble.png")
Bubbles6 = cv2.imread("Images/Bubbles/5BubbleX.png")
Bubbles7 = cv2.imread("Images/Bubbles/6Bubble.png")
Bubbles8 = cv2.imread("Images/Bubbles/6BubbleX.png")
Bubbles30pct = cv2.imread("Images/Bubbles/BubblySG.png")

cv2.imshow("Reference image, no bubbles", referenceImageNoBubbles)
cv2.imshow("Maximum difference mask", maxDifferenceMask)
cv2.imshow("5 bubbles", Bubbles5)
cv2.imshow("30 pct bubbles", Bubbles30pct)


maximumDifference = np.sum(referenceImageNoBubbles != maxDifferenceMask)
print("Maximum difference is: " + str(maximumDifference))

#cv2.imshow("MaxDiff Mask", maxDifferenceMask)
#cv2.imshow("ReferenceImg No bubbles", referenceImageNoBubbles)


diffBubbles1 = np.sum(referenceImageNoBubbles != Bubbles1)
print("Bubbles1 - difference is: " + str(diffBubbles1))
print("Bubbles1 - difference in percent is: " + str(diffBubbles1/maximumDifference) + "%")

diffBubbles2 = np.sum(referenceImageNoBubbles != Bubbles2)
print("Bubbles2 - difference is: " + str(diffBubbles2))
print("Bubbles2 - difference in percent is: " + str(diffBubbles2/maximumDifference) + "%")

diffBubbles3 = np.sum(referenceImageNoBubbles != Bubbles3)
print("Bubbles3 - difference is: " + str(diffBubbles3))
print("Bubbles3 - difference in percent is: " + str(diffBubbles3/maximumDifference) + "%")

diffBubbles4 = np.sum(referenceImageNoBubbles != Bubbles4)
print("Bubbles4 - difference is: " + str(diffBubbles4))
print("Bubbles4 - difference in percent is: " + str(diffBubbles4/maximumDifference) + "%")

diffBubbles5 = np.sum(referenceImageNoBubbles != Bubbles5)
print("Bubbles5 - difference is: " + str(diffBubbles5))
print("Bubbles5 - difference in percent is: " + str(diffBubbles5/maximumDifference) + "%")


diffBubbles6 = np.sum(referenceImageNoBubbles != Bubbles7)
print("Bubbles6 - difference is: " + str(diffBubbles6))
print("Bubbles6 - difference in percent is: " + str(diffBubbles6/maximumDifference) + "%")

diffBubbles30pct = np.sum(referenceImageNoBubbles != Bubbles30pct)
print("Bubbles 30 pct - difference is: " + str(diffBubbles30pct))
print("Bubbles 30 pct - difference in percent is: " + str(diffBubbles30pct/maximumDifference) + "%")



#currentDifference = np.sum(Bubbles0 != Bubbles1)
#print("Current difference is: " + str(currentDifference))

#currentDifferencePercent = currentDifference/maximumDifference
#print("Current difference in percent is: " + str(currentDifferencePercent))














######################
#while __name__ == '__main__':
#    time.sleep(50)
#    imageSightGlass = cv2.imread("Images/TESTING/CurrentTestImage.png")
#    isolatedIndicator, isolatedGlass, rectangularIndicator, maskGlass = isolateIndicatorAndGlass(imageSightGlass)
#    #cv2.imwrite('Images/NumberedImages/Masks/MaskedIndicator' + str(imgNumber) + '.png', rectangularIndicator)
#    meanR, meanG, meanB = calculateMeanRGB(rectangularIndicator)
#    #print("Image number: " + str(imgNumber))
#    closestColor = closest_color(meanR, meanG, meanB)
#    yellowColorPercentage = closestColor[1] / (closestColor[0] + closestColor[1])
#    print("Moisture percentage: " + str(yellowColorPercentage))


cv2.waitKey(0)
cv2.destroyAllWindows()









#½doubleIsoIndicator = cv2.bitwise_and(isolatedIndicator, maskIndicator)
#v2.imshow('BLABLA', doubleIsoIndicator)
#print("MEAN IS:")
#print(mean)
#valR, valG, valB = calculateMeanRGB(rectangularIndicator)

#valR = valR/25
#valG = valG/25
#valB = valB/25

#print("RGB values for isolated indicator: " + str(valR) + ", " + str(valG) + ", " + str(valB))
#closestIndicator = closest_color(valR, valG, valB)
#print(closestIndicator)

#yellowPantone = cv2.imread("Images/Yellow_Pantone.png")
#yellowR, yellowG, yellowB = calculateMeanRGB(yellowPantone)
#yellowR = yellowR/25.5
#yellowG = yellowG/25.5
#yellowB = yellowB/25.5





#yellowPantone = cv2.imread("Images/Yellow_Pantone.png")
#yellowR, yellowG, yellowB = calculateMeanRGB(yellowPantone)
#yellowR = yellowR/25.5
#yellowG = yellowG/25.5
#yellowB = yellowB/25.5

#print("For yellow value: ")
#closestClrYellow = closest_color(yellowR, yellowG, yellowB)
#print(closestClrYellow)



#print(int(meanR[1]))
#closestClr = closest_color(int(meanR[1]), int(meanG[1]), int(meanB[1]))
#print(closestClr)
#print('Mean RGB for val 1: ' + str(meanR[1]) + ', ' + str(meanG[1]) + ', ' + str(meanB[1]))
#print('Mean RGB for val 1: ' + str(meanR[10]) + ', ' + str(meanG[10]) + ', ' + str(meanB[10]))
#print('Mean RGB for val 1: ' + str(meanR[20]) + ', ' + str(meanG[20]) + ', ' + str(meanB[20]))


#closest_color((23, 145, 234))



cv2.waitKey(0)
cv2.destroyAllWindows()
