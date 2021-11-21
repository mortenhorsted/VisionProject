














#_____________________________________________________________________________________
#_____________________________________________________________________________________
#Filtering out noise from bubble images

markedBubbles = TEST_returnMarkedBubbles(currentGlass, referenceGlass)

markedBubbles = cv2.cvtColor(markedBubbles, cv2.COLOR_BGR2GRAY)
nonZeroPixels = cv2.countNonZero(markedBubbles)

markedBubblesRS = cv2.resize(markedBubbles, (960, 540))
cv2.imshow("Before marking bubbles", markedBubblesRS)

threshold = 60
markedBubbles[markedBubbles < threshold] = 0
markedBubblesRS2 = cv2.resize(markedBubbles, (960, 540))
cv2.imshow("After marking bubbles", markedBubblesRS2)


#_____________________________________________________________________________________
#_____________________________________________________________________________________
#Plotting MSE values

from matplotlib import image
from matplotlib import pyplot as plt
import numpy as np


def plotMSEValues(MSE, samples):
    x = np.linspace(0,100,samples)
    plt.plot(x, MSE, color="red")
    #plt.plot(x, meanG, color="green")
    #plt.plot(x, meanB, color="blue")
    #plt.xlim([0, 100])
    plt.xlabel("Bubble intensity")
    plt.ylim([0, 150])
    plt.ylabel("MSE value")
    plt.show()

