from CircleCalculations import areaOfCircle
from CircleDetection import detectCircle, justDetectCircle
import numpy as np
import cv2
import math
from math import sqrt
# from PIL import Image

from matplotlib import image
from matplotlib import pyplot as plt
from matplotlib.pyplot import hsv
from PIL import Image

def isolateIndicatorAndGlass(inputImage):



    tempImage = inputImage.copy()
    x_inner, y_inner, r_inner = detectCircle(tempImage, 5, 90)
    x_outer, y_outer, r_outer = detectCircle(tempImage, 60, 210)
    # draw filled circle in white on black background as mask
    mask = np.zeros_like(inputImage)


    maskIndicator = cv2.circle(mask, (x_inner, y_inner), r_inner, (255, 255, 255), -1)

    # apply mask to image
    isolatedIndicator = cv2.bitwise_and(inputImage, mask)

    #croppedIndicator = isolatedIndicator[y_inner:int((r_inner*sqrt(2))), x_inner:int((r_inner*sqrt(2)))]
    #nputImagg = cv2.imread("Images/NumberedImages/21.png")
    #croppedIndicator = inputImage[int(y_inner+((r_inner*sqrt(2))/2)):int((y_inner+(r_inner*sqrt(2)))), x_inner:int((x_inner+(r_inner*sqrt(2))))]
    #cv2.imshow('croppedIndicator', croppedIndicator)

    widthHeightOfRect = int((r_inner*sqrt(2))/2.5)
    #rectangularIndicator = cv2.rectangle(inputImage,((int(x_inner-widthHeightOfRect)),int(y_inner-widthHeightOfRect)),(x_inner+widthHeightOfRect,y_inner+widthHeightOfRect),(255,0,0),2)
    rectangularIndicator = inputImage[int(y_inner-widthHeightOfRect):y_inner+widthHeightOfRect, (int(x_inner-widthHeightOfRect)):x_inner+widthHeightOfRect]
    #cropped_im.show()

    #mask = np.zeros_like(inputImage)
    #reducedMaskIndicator = cv2.circle(mask, (x_inner, y_inner), int((r_inner*0.75)), (255, 255, 255), -1)
    #reducedIndicatorMask = reducedMaskIndicator.copy()
    #####
    #x_inner, y_inner, r_inner = detectCircle(isolatedIndicator, 5, 120)
    #doubleMaskedIndicator = cv2.circle(mask, (x_inner, y_inner), r_inner, (255, 255, 255), -1)
    #doubleIsolatedIndicator = cv2.bitwise_and(isolatedIndicator, indicatorMask)
    #####

    ### Invert indicator mask
    invertedIndicatorMask = cv2.bitwise_not(mask)

    maskGlass = cv2.circle(mask, (x_outer, y_outer), r_outer, (255, 255, 255), -1)

    maskedGlass = cv2.bitwise_and(inputImage, maskGlass)
    isolatedGlass = cv2.bitwise_and(maskedGlass, invertedIndicatorMask)

    onlyMaskGlass = maskGlass.copy()
    maskIndicator = cv2.circle(onlyMaskGlass, (x_inner, y_inner), r_inner, (0, 0, 0), -1)
    #cv2.imshow('Mask for glass', onlyMaskGlass)
    #hsv = cv2.cvtColor(isolatedIndicator, cv2.COLOR_BGR2HSV)
    #lower = np.array([20, 60, 60])
    #upper = np.array([140, 255, 255])
    #mask = cv2.inRange(hsv, lower, upper)
    #isolatedIndicator = cv2.bitwise_and(isolatedIndicator, isolatedIndicator, mask=mask)
    #cv2.imshow('REduced mask indicator2', reducedMaskIndicator)


    return isolatedIndicator, isolatedGlass, rectangularIndicator, onlyMaskGlass





cv2.waitKey(0)
cv2.destroyAllWindows()



