from CircleCalculations import areaOfCircle
from CircleDetection import detectCircle, justDetectCircle
from isolateIndicatorAndGlass import isolateIndicatorAndGlass
import numpy as np
import cv2
import math
#from PIL import Image

from matplotlib import image
from matplotlib import pyplot as plt
from matplotlib.pyplot import hsv

#img = cv2.imread("Images/YellowSG.png")
img = cv2.imread("Images/BubblySG.png")


x_inner, y_inner, r_inner = detectCircle(img, 70, 80)
x_outer, y_outer, r_outer = detectCircle(img, 90, 260)
#x_inner, y_inner, r_inner = detectCircle(img, 1, 100)
#x_outer, y_outer, r_outer = detectCircle(img, 10, 150)

cv2.imshow('Many circles', img)
img = cv2.imread("Images/BubblySG.png")

print('Radius of inner circle: ', r_inner)
print('Radius of outer circle: ', r_outer)
print('Area of inner circle: ', areaOfCircle(r_inner))
print('Area of outer circle: ', areaOfCircle(r_outer))
arealBetween = areaOfCircle(r_outer)-areaOfCircle(r_inner)
print('Area between the two circles: ', arealBetween)


#####################################################
# draw filled circle in white on black background as mask
mask = np.zeros_like(img)

maskIndicator = cv2.circle(mask, (x_inner,y_inner), r_inner, (255,255,255), -1)
#cv2.imshow('Before inverting', mask)
#inverted_mask = PIL.ImageOps.invert(mask)
#cv2.imshow('After interverting', inverted_mask)

# apply mask to image
isolatedIndicator = cv2.bitwise_and(img, mask)
#cv2.imshow('MASK', mask)



### Calculate RGB values for indicator
image_bgr = cv2.imread('isolatedIndicator.png', cv2.IMREAD_COLOR)
channels = cv2.mean(image_bgr)
observation = np.array([(channels[2], channels[1], channels[0])])
#print(observation)
plt.imshow(observation), plt.axis("off")
plt.show()

current_Rval = 255*channels[2]/10
current_Gval = 255*channels[1]/10
current_Bval = 255*channels[0]/10

print(current_Rval, ', ', current_Gval, ', ', current_Bval)

# Determine the color closest to the RGB measurement
TARGET_COLORS = {"Yellow (Pantone 108 U)": (255, 221, 53), "Green (Pantone 390 U)": (151, 169, 38), "Red": (255, 0, 0)}

def color_difference (color1, color2):
    return sum([abs(component1-component2) for component1, component2 in zip(color1, color2)])

my_color = (current_Rval, current_Gval, current_Bval)
differences = [[color_difference(my_color, target_value), target_name] for target_name, target_value in TARGET_COLORS.items()]
differences.sort()  # sorted by the first element of inner lists
my_color_name = differences[0][1]
print('The color is closest to: ', my_color_name)


### Invert indicator mask
invertedIndicatorMask = cv2.bitwise_not(mask)

maskGlass = cv2.circle(mask, (x_outer,y_outer), r_outer, (255,255,255), -1)

maskedGlass = cv2.bitwise_and(img, maskGlass)
isolatedGlass = cv2.bitwise_and(maskedGlass, invertedIndicatorMask)


# Show resulting images of isolated objects
#cv2.imshow('Isolated indicator', isolatedIndicator)
cv2.imshow('Isolated glass', isolatedGlass)
cv2.imwrite('isolatedGlass.png', isolatedGlass)

#######################################################################


nonBlackPixels = isolatedGlass.any(axis=-1).sum()
print(nonBlackPixels)

cv2.waitKey(0)
cv2.destroyAllWindows()

redSG = cv2.imread("Images/JagiBubbles.png")
redIndicator, redGlass = isolateIndicatorAndGlass(redSG)
cv2.imshow('Red indicator', redIndicator)
cv2.imshow('Red glass', redGlass)

cv2.waitKey(0)
cv2.destroyAllWindows()