This GitHub repository is containing the designed solutions for the bachelor thesis "Vision-based refrigerant quality detection" in collaboration with Danfoss. The purpose is to design a solution that is able to monitor a sight glass within a refrigeration system, to detect the moisture level as well as the presence of vapor bubbles in the liquid line. 


There are two different approaches for solving the problem, which is by classical image processing and machine learning.
Both solutions are able to determine the moisture level and detect the presence of vapor bubbles in the liquid line.

In case further explanations or material is desired, feel free to contact any of the three authors of the report by the information below.

Name | E-mail address
------------ | -------------
Morten Horsted Kristensen | morten-hk@hotmail.com
Dominic Okumu Vuga | dominicvuga@live.dk
Jageesh Sivasothy | XXXXXX


____________________________________________________

## Classical approach

The classical approach is utilizing sequential manipulation of the images to obtain an isolated image of each region of interest, which is the glass frame of the sight glass as well as the indicator.

The method for detecting the moisture level is by extracting a rectangular image of the indicator, only containing the colored pixels. Afterwards, the average RGB value of these pixels are compared to the two reference colors of the green and yellow indicator, hereby calculating the percentage of the yellow color between these two, which is equivalent to the moisture level.
The method for detecting vapor bubbles in the liquid line is performed by comparing the captured image to a reference image containing no vapor bubbles. Additionally, the captured image is also compared to the most recent captured image, in order to provide stability due to light fluctuations.
Each of the reference and recent images are compared to the captured image with a threshold, in order to determine the pixels that have achieved a certain degree of variance. Afterwards, these are dilated to provide a more accurate quantification of the size of the bubbles, as the threshold leads to the edges of the bubbles not being detected.

#### Current implementation

Currently, the solution is not implemented for running in real-time. Instead, it is designed for analyzing a set of captured images of the sight glass. The reason for this is that the algorithm has several parameters that should be manipulated in order to obtain the desired results, which are depending on the camera angle and distance. During the testing process of the solutions, a 3D printed encapsulation was designed and altered due to several different sizes of sight glasses, which provided an un-static point of view from the camera. 

The current implementation is to be performed on a folder containing several images. The code is set up to load all images from a given folder, given they are numbered from 1 and upwards.

#### The following parameters within the code is to be manipulated, in order to obtain the desired results as well as for stability

* **Hough circles, parameter 2:** This setting is adjusting the accuracy of the circle detection. If the circles can not be detected, this value can be decreased. If an incorrect circle is detected, it can be increased. 
* **Hough circles, minimum and maximum radius:** A minimum and maximum radius is defined for both the inner and outer circle (indicator and glass frame separation). The min/max radius for each circle is to be manipulated for detecting the correct circle, which fluctuates according to the distance between the camera and sight glass, as well as the image resolution.
* **Image comparison, threshold:** This setting is adjusting the threshold for when a variance in a pixel is detected. With no threshold, minor changes in light can be observed as a variance. This threshold should be low enough to detect the bubbles as a variance upon occurance, but high enough to not detect minor fluctuations as a variance.
* **Image comparison, dilation:** This setting is adjusting the amount of dilation for the pixels that are detected as a variance. The reason for dilating is that the comparison threshold is disregarding minor variances, which means that the edges of the vapor bubbles are not detected - the dilation can provide a more accurate quantification of the bubbles, in case this is desired. This value should be altered to achieve an approximate quantification of bubbles that are close to the true value, by comparing it visually to the captured images.

#### Preparation procedure

As the algorithm is depending on two reference images of the indicator, to determine the moisture level by the captured image, these should be provided before the algorithm is executed. Alternatively, the corresponding RGB values can be inserted by determining the manually. It should be noted that these reference RGB values are dependant on the light and focus of the lens, of which these should be determined by images of the indicator captured by the device once mounted.

In addition to the two reference colors, the algorithm requires a reference image of the sight glass without vapor bubbles. 

#### Displaying the results

To visualize at which point the algorithm is detecting vapor bubbles, a plotting function is implemented, of which the measured amount of bubbles are displayed for each image within the folder. The plotting is performed in three different ways: plotting the value for each image, as well as calculating the mean average of 3 or 10 images, respectively, and plotting these. The plotting for each image provides a precise visualization of when bubbles are detected, while the averaging plots are smoothening out the curve to prevent the spikes that are occuring. 

Besides the plotting, the detected amount of vapor bubbles is also exported as a .csv file, for further analysis of the data.

____________________________________________________

## Machine learning approach


### Mask RCNN


### CNN






____________________________________________________

## Dependencies for each solution

The version of Python that has been used during the implementation, as well as the various libraries and version numbers, is listed here, for each of the three solutions.

### Classical approach

* Python		3.9 (3.7+ should be sufficient)
* Pillow		8.4.0	
* PyWavelets		1.2.0
* cycler		0.11.0
* fonttools		4.28.3
* imageio		2.13.1	
* kiwisolver		1.3.2	
* matplotlib		3.5.0	
* networkx		2.6.3	
* numpy			1.21.4	
* opencv-python		4.5.4.60	
* packaging		21.3	
* pip			21.1.2	
* pyparsing		3.0.6	
* python-dateutil	2.8.2	
* scikit-image		0.19.0	
* scipy			1.7.3	
* setuptools		57.0.0	
* setuptools-scm	6.3.2	
* six			1.16.0	
* tifffile		2021.11.2	
* tomli			1.2.2	
* wheel			0.36.2	

### Mask RCNN

* Python 3.56
* tensor
* pip

### CNN

* Python 3.56
* tensor
* pip



