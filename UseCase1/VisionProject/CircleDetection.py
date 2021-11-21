import numpy as np
import cv2

from matplotlib import image
from matplotlib import pyplot as plt


def detectCircle(image, minRadius, maxRadius):
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


def justDetectCircle(image, minRadius, maxRadius):
    minDist = 100
    param1 = 30  # 500
    param2 = 50  # 200 #smaller value-> more false circles
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


