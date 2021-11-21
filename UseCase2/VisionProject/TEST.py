#import cv2
#import numpy as np

#cimg = cv2.imread('isolatedGlass.png')
#cv2.imshow("origin", cimg)
#cv2.waitKey(0)
#img = cv2.cvtColor(cimg,cv2.COLOR_BGR2GRAY)
#img = cv2.medianBlur(img, 5)
#cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

#- img: grayscale image to be detected
# - cv2.HOUGH_ Gradient: detection method, Hoff gradient
#- 1: the detected circle has the same size as the original image, DP = 2, and the detected circle is half of the original image
#- 20: the minimum distance of the center of the detected circle (if the parameter is too small, multiple adjacent circles may be detected incorrectly in addition to a real circle. If it is too large, some circles may be missed.)
#- Param1: in #hough Š In the case of u gradient, it is higher. Two thresholds are passed to Canny edge detector (the lower one is twice as small).
#- param2: at #hough Š In the case of u gradient, it is the accumulator threshold of the center of the detection stage. The smaller it is, the more likely it is to detect false circles;
#- minradius: minimum circle radius, false circle may also be detected
#- maxradius: maximum circle radius. If < = 0, the maximum image size is used. If < 0, returns the center of the radius not found.
#circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20,
#                           param1=20, param2=22, minRadius=2, maxRadius=30)
#If the minimum circle radius is not set properly, false circles may also be detected
# circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20,
#                            param1=50, param2=40, minRadius=0, maxRadius=0)
# circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20,
#                            param1=50, param2=30, minRadius=10, maxRadius=0)

#circles = np.uint16(np.around(circles))

#print(len(circles))
#print(circles)
#for i in circles[0, :]:
    #Draw outer circle (blue)
#    cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)

    #Draw Center (red)
#    cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)

#cv2.imshow('detected circles', cimg)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

print('Hi Raspberry Pi!')
