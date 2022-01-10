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



    #maskFrame = np.zeros_like(tempImage2)
    #maskedIndicator = cv2.rectangle(maskFrame, (int(x_inner-widthHeightOfRect), int(y_inner-widthHeightOfRect)), (int(x_inner+widthHeightOfRect), int(y_inner+widthHeightOfRect)), (255, 255, 255), -1)

    #####

    ### Extract mask for only glass section
    invertedIndicatorMask = cv2.bitwise_not(mask)
    imgMaskGlass = cv2.circle(mask, (x_outer, y_outer), r_outer, (255, 255, 255), -1)
    maskedGlass = cv2.bitwise_and(inputImage, imgMaskGlass)
    isolatedGlass = cv2.bitwise_and(maskedGlass, invertedIndicatorMask)
    maskGlass = cv2.bitwise_and(imgMaskGlass, invertedIndicatorMask)

    maskGlass_grayscale = cv2.cvtColor(maskGlass, cv2.COLOR_BGR2GRAY)
    glassROI_x1 = int(x_outer + ((r_outer*2)/6))
    glassROI_y1 = int(y_outer - r_outer)
    glassROI_x2 = int(x_outer + r_outer)
    glassROI_y2 = int(y_outer + r_outer)

    #snippedMaskGlass = maskGlass[glassROI_y1:glassROI_y2, glassROI_x1:glassROI_x2]
    #snippedGlass = isolatedGlass[glassROI_y1:glassROI_y2, glassROI_x1:glassROI_x2]

    rectangularMaskGlass = np.zeros_like(inputImage)
    cv2.rectangle(rectangularMaskGlass, (glassROI_x1, glassROI_y2), (glassROI_x2, glassROI_y1), (255, 255, 255), -1)

    croppedMaskGlass = cv2.bitwise_and(rectangularMaskGlass, maskGlass)

    croppedGlass = cv2.bitwise_and(isolatedGlass, croppedMaskGlass)
    cv2.imshow("rect glass mask", croppedMaskGlass)
    cv2.imshow("Masked glass", croppedGlass)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    return croppedGlass, croppedMaskGlass









