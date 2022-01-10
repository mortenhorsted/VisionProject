import numpy as np
import cv2
import math
#from PIL import Image

from matplotlib import image
from matplotlib import pyplot as plt
from matplotlib.pyplot import hsv
from math import sqrt



COLORS = (
    (255, 221, 53),
    (151, 169, 38)
)

#def closest_color(r, g, b):
    #r, g, b = rgb
#    color_diffs = []
#    for color in COLORS:
#        cr, cg, cb = color
#        color_diff = sqrt(abs(r - cr)**2 + abs(g - cg)**2 + abs(b - cb)**2)
#        print('Color difference: ' + str(color_diff))
#        color_diffs.append((color_diff, color))
#    return min(color_diffs)[1]

def closest_color(r, g, b):
    #r, g, b = rgb
    color_diffs = []
    for color in COLORS:
        cr, cg, cb = color
        color_diff = sqrt(abs(r - cr)**2 + abs(g - cg)**2 + abs(b - cb)**2)
        #print('Color difference: ' + str(color_diff))
        color_diffs.append((color_diff, color))
    return (color_diffs)[0][0], (color_diffs)[1][0]






def calculateMeanRGB(inputImage):

    ### Calculate RGB values for indicator

    #channels = cv2.mean(inputImage)
    #observation = np.array([(channels[2], channels[1], channels[0])])
    # print(observation)
    #plt.imshow(observation), plt.axis("off")
    #plt.show()

    #current_Rval = 255 * channels[2] / 10
    #current_Gval = 255 * channels[1] / 10
    #current_Bval = 255 * channels[0] / 10
    meanBGR = cv2.mean(inputImage)
    current_Rval = meanBGR[2]
    current_Gval = meanBGR[1]
    current_Bval = meanBGR[0]
    #print(current_Rval, ', ', current_Gval, ', ', current_Bval)

    # Determine the color closest to the RGB measurement
    #TARGET_COLORS = {"Yellow (Pantone 108 U)": (255, 221, 53), "Green (Pantone 390 U)": (151, 169, 38),
    #                 "Red": (255, 0, 0)}


    #def color_difference(color1, color2):
    #    return sum([abs(component1 - component2) for component1, component2 in zip(color1, color2)])


    #my_color = (current_Rval, current_Gval, current_Bval)
    #differences = [[color_difference(my_color, target_value), target_name] for target_name, target_value in
    #               TARGET_COLORS.items()]
    #differences.sort()  # sorted by the first element of inner lists
    #my_color_name = differences[0][1]
    #print('The color is closest to: ', my_color_name)
    return current_Rval, current_Gval, current_Bval
