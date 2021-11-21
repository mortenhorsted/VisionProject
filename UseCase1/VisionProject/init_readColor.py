from isolateIndicatorAndGlass import isolateIndicatorAndGlass
import cv2
from detectMeanRGB import calculateMeanRGB
from detectMeanRGB import closest_color


def readColor(img):

    isolatedGlass, maskGlass, indicator_x1, indicator_y1, indicator_x2, indicator_y2 = isolateIndicatorAndGlass(img)
    rectangularIndicator = img[indicator_y1:indicator_y2, indicator_x1:indicator_x2]

    meanR, meanG, meanB = calculateMeanRGB(rectangularIndicator)
    print("Mean R: " + str(meanR))
    print("Mean B: " + str(meanB))
    print("Mean G: " + str(meanG))
    cv2.imshow("CURRENT COLOR", rectangularIndicator)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    closestColor = closest_color(meanR, meanG, meanB)
    yellowColorPercentage = closestColor[1] / (closestColor[0] + closestColor[1])
    yellowColorPercentage = round(yellowColorPercentage * 100)
    print("Yellow color percentage is: " + str(yellowColorPercentage) + "%")

