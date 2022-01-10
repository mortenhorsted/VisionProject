# import the necessary packages
from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
from plotRGBValues import plotRGBValues
import time
from isolateIndicatorAndGlass import isolateIndicatorAndGlass


import Image
import ImageChops

im1 = Image.open("../Images/RealImages/v4/Isolated_glasses/ImageNumber12.png")
im2 = Image.open("../Images/RealImages/v4/Isolated_glasses/ImageNumber12.png")

diff = ImageChops.difference(im2, im1)


time.sleep(5)

# import the necessary packages
from skimage.metrics import structural_similarity as compare_ssim
import argparse
import imutils
import cv2
imgCount = 12
refImg = cv2.imread("Images/RealImages/v4/Isolated_glasses/ImageNumber12.png")
while imgCount < 200:
    imgCountplus = imgCount + 1
    imageA = cv2.imread("Images/RealImages/v4/Isolated_glasses/ImageNumber" + str(imgCount) + ".png")
    #imageB = refImg.copy()
    #imageB = cv2.imread("Images/RealImages/v4/Isolated_glasses/ImageNumber" + str(imgCount) + ".png")
    # convert the images to grayscale
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(refImg, cv2.COLOR_BGR2GRAY)

    # compute the Structural Similarity Index (SSIM) between the two
    # images, ensuring that the difference image is returned
    (score, diff) = compare_ssim(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")
    print("Image" + str(imgCount) + "     SSIM: {}".format(score))
    imgCount = imgCount + 1


# construct the argument parse and parse the arguments


# load the two input images
imageA = cv2.imread("Images/RealImages/v4/ImageNumber60.jpg")
imageB = cv2.imread("Images/RealImages/v4/ImageNumber100.jpg")
# convert the images to grayscale
grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)



# compute the Structural Similarity Index (SSIM) between the two
# images, ensuring that the difference image is returned
(score, diff) = compare_ssim(grayA, grayB, full=True)
diff = (diff * 255).astype("uint8")
print("SSIM: {}".format(score))


# threshold the difference image, followed by finding contours to
# obtain the regions of the two input images that differ
thresh = cv2.threshold(diff, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)



# loop over the contours
for c in cnts:
	# compute the bounding box of the contour and then draw the
	# bounding box on both input images to represent where the two
	# images differ
	(x, y, w, h) = cv2.boundingRect(c)
	cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
	cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)
# show the output images
cv2.imshow("Original", imageA)
cv2.imshow("Modified", imageB)
cv2.imshow("Diff", diff)
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)

















def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err


def compare_images(imageA, imageB, title):
    # compute the mean squared error and structural similarity
    # index for the images
    m = mse(imageA, imageB)
    s = ssim(imageA, imageB)
    # setup the figure
    fig = plt.figure(title)
    plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))
    # show first image
    ax = fig.add_subplot(1, 2, 1)
    plt.imshow(imageA, cmap=plt.cm.gray)
    plt.axis("off")
    # show the second image
    ax = fig.add_subplot(1, 2, 2)
    plt.imshow(imageB, cmap=plt.cm.gray)
    plt.axis("off")
    # show the images
    plt.show()
    return m, s


#
# refImage = cv2.imread("Images/RealImages/v4/ImageNumber24.jpg")
# isolatedGlass, maskGlass, maskIndicator, halvedMaskIndicator = isolateIndicatorAndGlass(refImage)
# refGlass = isolatedGlass.copy()
# MSE = np.array([])
# imgCounter = 25
# while imgCounter < 270:
#     currentImage = cv2.imread("Images/RealImages/v4/ImageNumber" + str(imgCounter) + ".jpg")
#     #isolatedGlass, maskGlass, maskIndicator, halvedMaskIndicator = isolateIndicatorAndGlass(currentImage)
#     currentGlass = cv2.bitwise_and(currentImage, maskGlass)
#     m = mse(refGlass, currentGlass)
#     #cv2.imshow("REF GLASS", refGlass)
#     #cv2.imshow("ISOLATED GLASS", isolatedGlass)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#     MSE = np.append(MSE, m)
#     print(m)
#     imgCounter = imgCounter + 1
#
#
#
# plotMSEValues(MSE, len(MSE))
#
# time.sleep(100)

def pctReturnFromMSE(mse):
    pct = ((mse-250)/2450)
    return pct


# load the images -- the original, the original + contrast,
# and the original + photoshop
image0 = cv2.imread("Images/RPI_Images/RPI_BubbleManipulation/Image0.png")
image1 = cv2.imread("Images/RPI_Images/RPI_BubbleManipulation/Image1.png")
image2 = cv2.imread("Images/RPI_Images/RPI_BubbleManipulation/Image2.png")
image3 = cv2.imread("Images/RPI_Images/RPI_BubbleManipulation/Image3.png")
image4 = cv2.imread("Images/RPI_Images/RPI_BubbleManipulation/Image4.png")
image5 = cv2.imread("Images/RPI_Images/RPI_BubbleManipulation/Image5.png")
image6 = cv2.imread("Images/RPI_Images/RPI_BubbleManipulation/Image6.png")
image7 = cv2.imread("Images/RPI_Images/RPI_BubbleManipulation/Image7.png")
image8 = cv2.imread("Images/RPI_Images/RPI_BubbleManipulation/Image8.png")

#image0 = cv2.imread("Images/RealImages/v4/ImageNumber10.jpg")
#image1 = cv2.imread("Images/RealImages/v4/ImageNumber40.jpg")
#image2 = cv2.imread("Images/RealImages/v4/ImageNumber70.jpg")
#image3 = cv2.imread("Images/RealImages/v4/ImageNumber100.jpg")
#image4 = cv2.imread("Images/RealImages/v4/ImageNumber120.jpg")
#image5 = cv2.imread("Images/RealImages/v4/ImageNumber140.jpg")
#image6 = cv2.imread("Images/RealImages/v4/ImageNumber155.jpg")
#image7 = cv2.imread("Images/RealImages/v4/ImageNumber167.jpg")


#image0 = cv2.imread("Images/RPI_Images/RPI_BubbleManipulation/TEST/Image0.png")
#image1 = cv2.imread("Images/RPI_Images/RPI_BubbleManipulation/TEST/Image1.png")
#image2 = cv2.imread("Images/RPI_Images/RPI_BubbleManipulation/TEST/Image2.png")
#image3 = cv2.imread("Images/RPI_Images/RPI_BubbleManipulation/TEST/Image3.png")
#image4 = cv2.imread("Images/RPI_Images/RPI_BubbleManipulation/TEST/Image4.png")
#image5 = cv2.imread("Images/RPI_Images/RPI_BubbleManipulation/TEST/Image5.png")





image0 = cv2.cvtColor(image0, cv2.COLOR_BGR2GRAY)
image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
image3 = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)
image4 = cv2.cvtColor(image4, cv2.COLOR_BGR2GRAY)
image5 = cv2.cvtColor(image5, cv2.COLOR_BGR2GRAY)
image6 = cv2.cvtColor(image6, cv2.COLOR_BGR2GRAY)
image7 = cv2.cvtColor(image7, cv2.COLOR_BGR2GRAY)
image8 = cv2.cvtColor(image8, cv2.COLOR_BGR2GRAY)

original = cv2.imread("Images/RPI_Images/RPI_BubbleManipulation/Image0.png")
contrast = cv2.imread("Images/RPI_Images/RPI_BubbleManipulation/Image1.png")
shopped = cv2.imread("Images/RPI_Images/RPI_BubbleManipulation/Image8.png")
# convert the images to grayscale
original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
contrast = cv2.cvtColor(contrast, cv2.COLOR_BGR2GRAY)
shopped = cv2.cvtColor(shopped, cv2.COLOR_BGR2GRAY)

MSE = np.array([])
SSIM = np.array([])

# initialize the figure
fig = plt.figure("Images")
images = ("Original", original), ("Contrast", contrast), ("Photoshopped", shopped)
# loop over the images
for (i, (name, image)) in enumerate(images):
	# show the image
	ax = fig.add_subplot(1, 3, i + 1)
	ax.set_title(name)
	plt.imshow(image, cmap = plt.cm.gray)
	plt.axis("off")
# show the figure
plt.show()
# compare the images
m, s = compare_images(image0, image0, "Original vs. Original")
pct = pctReturnFromMSE(m)
print("Image0 and Image 0:   MSE = " + str(m) + "    SSIM = " + str(s) + "    PCT = " + str(pct))
MSE = np.append(MSE,m)
SSIM = np.append(SSIM,s)
m, s = compare_images(image0, image1, "Original vs. Original")
pct = pctReturnFromMSE(m)
print("Image0 and Image 1:   MSE = " + str(m) + "    SSIM = " + str(s) + "    PCT = " + str(pct))
MSE = np.append(MSE,m)
SSIM = np.append(SSIM,s)
m, s = compare_images(image0, image2, "Original vs. Original")
pct = pctReturnFromMSE(m)
print("Image0 and Image 2:   MSE = " + str(m) + "    SSIM = " + str(s) + "    PCT = " + str(pct))
MSE = np.append(MSE,m)
SSIM = np.append(SSIM,s)
m, s = compare_images(image0, image3, "Original vs. Original")
pct = pctReturnFromMSE(m)
print("Image0 and Image 3:   MSE = " + str(m) + "    SSIM = " + str(s) + "    PCT = " + str(pct))
MSE = np.append(MSE,m)
SSIM = np.append(SSIM,s)
m, s = compare_images(image0, image4, "Original vs. Original")
pct = pctReturnFromMSE(m)
print("Image0 and Image 4:   MSE = " + str(m) + "    SSIM = " + str(s) + "    PCT = " + str(pct))
MSE = np.append(MSE,m)
SSIM = np.append(SSIM,s)
m, s = compare_images(image0, image5, "Original vs. Original")
pct = pctReturnFromMSE(m)
print("Image0 and Image 5:   MSE = " + str(m) + "    SSIM = " + str(s) + "    PCT = " + str(pct))
MSE = np.append(MSE,m)
SSIM = np.append(SSIM,s)
m, s = compare_images(image0, image6, "Original vs. Original")
pct = pctReturnFromMSE(m)
print("Image0 and Image 6:   MSE = " + str(m) + "    SSIM = " + str(s) + "    PCT = " + str(pct))
MSE = np.append(MSE,m)
SSIM = np.append(SSIM,s)
m, s = compare_images(image0, image7, "Original vs. Original")
pct = pctReturnFromMSE(m)
print("Image0 and Image 7:   MSE = " + str(m) + "    SSIM = " + str(s) + "    PCT = " + str(pct))
MSE = np.append(MSE,m)
SSIM = np.append(SSIM,s)
m, s = compare_images(image0, image8, "Original vs. Original")
pct = pctReturnFromMSE(m)
print("Image0 and Image 8:   MSE = " + str(m) + "    SSIM = " + str(s) + "    PCT = " + str(pct))
MSE = np.append(MSE,m)
SSIM = np.append(SSIM,s)
#compare_images(original, contrast, "Original vs. Contrast")
#compare_images(original, shopped, "Original vs. Photoshopped")

plotMSEValues(MSE, len(MSE))