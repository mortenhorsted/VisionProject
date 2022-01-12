
import numpy as np
import matplotlib.pyplot as plt
import cv2

# read image
#im = cv2.imread('Images/RealImages/v4/ImageNumber16.jpg')
#im = cv2.imread('Images/RPI_Images/RPI_BubbleManipulation/Image5.png')
im = cv2.imread('Images/BubblySG2.png')
# calculate mean value from RGB channels and flatten to 1D array
vals = im.mean(axis=2).flatten()
# calculate histogram
counts, bins = np.histogram(vals, range(257))
# plot histogram centered on values 0..255
plt.bar(bins[:-1] - 0.5, counts, width=1, edgecolor='none')
plt.xlim([-0.5, 255.5])
plt.show()
