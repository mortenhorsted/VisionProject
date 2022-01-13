There are two different approaches for solving the problem, which is by classical image processing and machine learning.

Both solutions are able to determine the moisture level and detect the presence of vapor bubbles in the liquid line.


____________________________________________________

## Classical approach

The classical approach is utilizing sequential manipulation of the images to obtain an isolated image of each region of interest, which is the glass frame of the sight glass as well as the indicator.

The method for detecting the moisture level is by extracting a rectangular image of the indicator, only containing the colored pixels. Afterwards, the average RGB value of these pixels are compared to the two reference colors of the green and yellow indicator, hereby calculating the percentage of the yellow color between these two, which is equivalent to the moisture level.
The method for detecting vapor bubbles in the liquid line is performed by comparing the captured image to a reference image containing no vapor bubbles. Additionally, the captured image is also compared to the most recent captured image, in order to provide stability due to light fluctuations.
Each of the reference and recent images are compared to the captured image with a threshold, in order to determine the pixels that have achieved a certain degree of variance. Afterwards, these are dilated to provide a more accurate quantification of the size of the bubbles, as the threshold leads to the edges of the bubbles not being detected.

#### The following parameters within the code is to be manipulated, in order to obtain the desired results as well as for stability

* Hough circles, parameter 2: This setting is adjusting the accuracy of the circle detection. If the circles can not be detected, this value can be decreased. If an incorrect circle is detected, it can be increased. 
* Hough circles, minimum and maximum radius. A minimum and maximum radius is defined for both the inner and outer circle (indicator and glass frame separation). The min/max radius for each circle is to be manipulated for detecting the correct circle, which fluctuates according to the distance between the camera and sight glass, as well as the image resolution.
* Image comparison, threshold. This setting is adjusting the threshold for when a variance in a pixel is detected. With no threshold, minor changes in light can be observed as a variance. This threshold should be low enough to detect the bubbles as a variance upon occurance, but high enough to not detect minor fluctuations as a variance.
* Image comparison, dilation. 


____________________________________________________

## Machine learning approach


### Mask RCNN


### CNN






____________________________________________________

## Dependencies for each solution

### Classical approach

* Python 3.56
* tensor
* pip

### Mask RCNN

* Python 3.56
* tensor
* pip

### CNN

* Python 3.56
* tensor
* pip




The project is divided into three subprojects, one for each use case.

The following abbreviations are used:
	SGI: Sight glass with indicator ring
	SGG: Sight glass without indicator ring


UseCase1: Moisture and bubble detection. The device is monitoring a SGI, and outputting the yellow color percentage as well as the bubble intensity every second.

UseCase2: Bubble detection. The device is monitoring a SGI, but only looking for bubbles in the rear third of the glass area. The output is the bubble intensity within this area.

Usecase3: Bubble detection. The device is monitoring a SGG, while looking for bubbles within the whole glass area. The output is the bubble intensity within this area.
