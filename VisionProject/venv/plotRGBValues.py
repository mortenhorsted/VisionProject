
from matplotlib import image
from matplotlib import pyplot as plt
import numpy as np

def plotRGBValues(meanR, meanG, meanB, samples):
    x = np.linspace(0,100,samples)
    plt.plot(x, meanR, color="red")
    plt.plot(x, meanG, color="green")
    plt.plot(x, meanB, color="blue")
    #plt.xlim([0, 100])
    plt.xlabel("Moisture level [%]")
    plt.ylim([0, 255])
    plt.ylabel("RGB values")
    plt.show()
