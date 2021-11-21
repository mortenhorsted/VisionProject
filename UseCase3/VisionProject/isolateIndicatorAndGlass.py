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


    #imgHeight = inputImage.shape[0]
    #imgWidth = inputImage.shape[1]
    #tempImage2 = inputImage.copy()


    tempImage = inputImage.copy()
    x_inner, y_inner, r_inner = detectCircle(tempImage, 150, 250)
    x_outer, y_outer, r_outer = detectCircle(tempImage, 300, 400)

    mask = np.zeros_like(inputImage)
    maskIndicator = cv2.circle(mask, (x_inner, y_inner), r_inner, (255, 255, 255), -1)
    isolatedIndicator = cv2.bitwise_and(inputImage, mask)



    widthHeightOfRect = int((r_inner*sqrt(2))/3)
    #rectangularIndicator = cv2.rectangle(inputImage,((int(x_inner-widthHeightOfRect)),int(y_inner-widthHeightOfRect)),(x_inner+widthHeightOfRect,y_inner+widthHeightOfRect),(255,0,0),2)
    #rectangularIndicator = inputImage[int(y_inner-widthHeightOfRect):y_inner+widthHeightOfRect, (int(x_inner-widthHeightOfRect)):x_inner+widthHeightOfRect]
    #cropped_im.show()

    indicator_x1 = int(x_inner-widthHeightOfRect)
    indicator_y1 = int(y_inner-widthHeightOfRect)
    indicator_x2 = int(x_inner+widthHeightOfRect)
    indicator_y2 = int(y_inner+widthHeightOfRect)


    #maskFrame = np.zeros_like(tempImage2)
    #maskedIndicator = cv2.rectangle(maskFrame, (int(x_inner-widthHeightOfRect), int(y_inner-widthHeightOfRect)), (int(x_inner+widthHeightOfRect), int(y_inner+widthHeightOfRect)), (255, 255, 255), -1)

    #####

    ### Extract mask for only glass section
    invertedIndicatorMask = cv2.bitwise_not(mask)
    imgMaskGlass = cv2.circle(mask, (x_outer, y_outer), r_outer, (255, 255, 255), -1)
    maskedGlass = cv2.bitwise_and(inputImage, imgMaskGlass)
    isolatedGlass = cv2.bitwise_and(maskedGlass, invertedIndicatorMask)
    maskGlass = cv2.bitwise_and(imgMaskGlass, invertedIndicatorMask)


    return isolatedGlass, maskGlass









