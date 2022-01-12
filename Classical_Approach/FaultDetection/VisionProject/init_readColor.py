from isolateIndicatorAndGlass import isolateIndicatorAndGlass
import cv2
from detectMeanRGB import calculateMeanRGB
from detectMeanRGB import closest_color
from skimage.color import rgb2hsv






def readColor(img):

    isolatedGlass, maskGlass, indicator_x1, indicator_y1, indicator_x2, indicator_y2 = isolateIndicatorAndGlass(img)
    rectangularIndicator = img[indicator_y1:indicator_y2, indicator_x1:indicator_x2]

    meanR, meanG, meanB = calculateMeanRGB(rectangularIndicator)
    cv2.imshow("CURRENT COLOR", rectangularIndicator)
    cv2.imwrite("Images/rectangularIndicator.jpg", rectangularIndicator)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    closestColor = closest_color(meanR, meanG, meanB)
    yellowColorPercentage = closestColor[1] / (closestColor[0] + closestColor[1])
    yellowColorPercentage = round(yellowColorPercentage * 100)
    print("Yellow color percentage is: " + str(yellowColorPercentage) + "%")

