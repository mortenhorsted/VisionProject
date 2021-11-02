from CircleCalculations import areaOfCircle
from CircleDetection import detectCircle, justDetectCircle
from isolateIndicatorAndGlass import isolateIndicatorAndGlass
from detectMeanRGB import calculateMeanRGB
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


#img = cv2.imread("Images/BubblySG.png")


#x_inner, y_inner, r_inner = detectCircle(img, 70, 80)
#x_outer, y_outer, r_outer = detectCircle(img, 90, 260)


#cv2.imshow('Many circles', img)
#img = cv2.imread("Images/BubblySG.png")

#print('Radius of inner circle: ', r_inner)
#print('Radius of outer circle: ', r_outer)
#print('Area of inner circle: ', areaOfCircle(r_inner))
#print('Area of outer circle: ', areaOfCircle(r_outer))
#arealBetween = areaOfCircle(r_outer)-areaOfCircle(r_inner)
#print('Area between the two circles: ', arealBetween)


#####################################################
# draw filled circle in white on black background as mask
#mask = np.zeros_like(img)

#maskIndicator = cv2.circle(mask, (x_inner,y_inner), r_inner, (255,255,255), -1)


# apply mask to image
#isolatedIndicator = cv2.bitwise_and(img, mask)




### Calculate RGB values for indicator
#image_bgr = cv2.imread('isolatedIndicator.png', cv2.IMREAD_COLOR)
#channels = cv2.mean(image_bgr)
#observation = np.array([(channels[2], channels[1], channels[0])])


#current_Rval = 255*channels[2]/10
#current_Gval = 255*channels[1]/10
#current_Bval = 255*channels[0]/10

#print(current_Rval, ', ', current_Gval, ', ', current_Bval)

# Determine the color closest to the RGB measurement
#TARGET_COLORS = {"Yellow (Pantone 108 U)": (255, 221, 53), "Green (Pantone 390 U)": (151, 169, 38), "Red": (255, 0, 0)}

#def color_difference (color1, color2):
#    return sum([abs(component1-component2) for component1, component2 in zip(color1, color2)])

#my_color = (current_Rval, current_Gval, current_Bval)
#differences = [[color_difference(my_color, target_value), target_name] for target_name, target_value in TARGET_COLORS.items()]
#differences.sort()  # sorted by the first element of inner lists
#my_color_name = differences[0][1]
#print('The color is closest to: ', my_color_name)


### Invert indicator mask
#invertedIndicatorMask = cv2.bitwise_not(mask)

#maskGlass = cv2.circle(mask, (x_outer,y_outer), r_outer, (255,255,255), -1)

#maskedGlass = cv2.bitwise_and(img, maskGlass)
#isolatedGlass = cv2.bitwise_and(maskedGlass, invertedIndicatorMask)


# Show resulting images of isolated objects
#cv2.imshow('Isolated glass', isolatedGlass)
#cv2.imwrite('isolatedGlass.png', isolatedGlass)

#######################################################################


#nonBlackPixels = isolatedGlass.any(axis=-1).sum()
#print(nonBlackPixels)

#cv2.waitKey(0)
#cv2.destroyAllWindows()



######################## Looping functions



#____________________________________
#path = str(21)




######### PLOTTING SEQUENCE
meanR = np.zeros(21)
meanG = np.zeros(21)
meanB = np.zeros(21)

imgNumber = 1
while imgNumber < 22:
    imageSightGlass = cv2.imread("Images/NumberedImages/" + str(imgNumber) + ".png")
    isolatedIndicator, isolatedGlass, rectangularIndicator = isolateIndicatorAndGlass(imageSightGlass)
    #cv2.imwrite('Images/NumberedImages/Masks/MaskedIndicator' + str(imgNumber) + '.png', isolatedIndicator)
    meanR[imgNumber-1], meanG[imgNumber-1], meanB[imgNumber-1] = calculateMeanRGB(isolatedIndicator)
    imgNumber = imgNumber + 1


plotRGBValues(meanR, meanG, meanB, 21)
#while __name__ == '__main__':
#    time.sleep(2)



cv2.waitKey(0)
cv2.destroyAllWindows()


COLORS = (
    (255, 221, 53),
    (151, 169, 38)
)


def closest_color(r, g, b):
    #r, g, b = rgb
    color_diffs = []
    for color in COLORS:
        cr, cg, cb = color
        color_diff = sqrt(abs(r - cr)**2 + abs(g - cg)**2 + abs(b - cb)**2)
        print('Color difference: ' + str(color_diff))
        color_diffs.append((color_diff, color))
    return min(color_diffs)[1]


imageSightGlass = cv2.imread("Images/NumberedImages/21.png")
isolatedIndicator, isolatedGlass, rectangularIndicator = isolateIndicatorAndGlass(imageSightGlass)
cv2.imshow('Isolated indicator', rectangularIndicator)
cv2.imshow('Mask for indicator', isolatedGlass)



mean = cv2.mean(rectangularIndicator)
print("MEAN IS:")
print(mean)
print(mean[1])




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
