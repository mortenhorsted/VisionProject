from CircleCalculations import areaOfCircle
from CircleDetection import detectCircle, justDetectCircle
import numpy as np
import cv2
import math
# from PIL import Image

from matplotlib import image
from matplotlib import pyplot as plt
from matplotlib.pyplot import hsv


def isolateIndicatorAndGlass(inputImage):


    # img = cv2.imread("Images/YellowSG.png")
    #inputImage = cv2.imread("Images/BothSG.png")

    x_inner, y_inner, r_inner = detectCircle(inputImage, 5, 80)
    x_outer, y_outer, r_outer = detectCircle(inputImage, 5, 170)
    # x_inner, y_inner, r_inner = detectCircle(img, 1, 100)
    # x_outer, y_outer, r_outer = detectCircle(img, 10, 150)

    #cv2.imshow('Many circles', inputImage)
    #img = cv2.imread("Images/BubblySG.png")

    #print('Radius of inner circle: ', r_inner)
    #print('Radius of outer circle: ', r_outer)
    #print('Area of inner circle: ', areaOfCircle(r_inner))
    #print('Area of outer circle: ', areaOfCircle(r_outer))
    #arealBetween = areaOfCircle(r_outer) - areaOfCircle(r_inner)
    #print('Area between the two circles: ', arealBetween)

    #####################################################
    # draw filled circle in white on black background as mask
    mask = np.zeros_like(inputImage)

    maskIndicator = cv2.circle(mask, (x_inner, y_inner), r_inner, (255, 255, 255), -1)
    # cv2.imshow('Before inverting', mask)
    # inverted_mask = PIL.ImageOps.invert(mask)
    # cv2.imshow('After interverting', inverted_mask)

    # apply mask to image
    isolatedIndicator = cv2.bitwise_and(inputImage, mask)
    # cv2.imshow('MASK', mask)

    ### Invert indicator mask
    invertedIndicatorMask = cv2.bitwise_not(mask)

    maskGlass = cv2.circle(mask, (x_outer, y_outer), r_outer, (255, 255, 255), -1)

    maskedGlass = cv2.bitwise_and(inputImage, maskGlass)
    isolatedGlass = cv2.bitwise_and(maskedGlass, invertedIndicatorMask)

    # Show resulting images of isolated objects
    # cv2.imshow('Isolated indicator', isolatedIndicator)
    #cv2.imshow('Isolated glass', isolatedGlass)
    return isolatedIndicator, isolatedGlass

    #######################################################################

    #cv2.waitKey(0)
    #cv2.destroyAllWindows()



