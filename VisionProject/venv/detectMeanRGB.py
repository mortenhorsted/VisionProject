### Calculate RGB values for indicator
image_bgr = cv2.imread('isolatedIndicator.png', cv2.IMREAD_COLOR)
channels = cv2.mean(image_bgr)
observation = np.array([(channels[2], channels[1], channels[0])])
# print(observation)
plt.imshow(observation), plt.axis("off")
plt.show()

current_Rval = 255 * channels[2] / 10
current_Gval = 255 * channels[1] / 10
current_Bval = 255 * channels[0] / 10

print(current_Rval, ', ', current_Gval, ', ', current_Bval)

# Determine the color closest to the RGB measurement
TARGET_COLORS = {"Yellow (Pantone 108 U)": (255, 221, 53), "Green (Pantone 390 U)": (151, 169, 38),
                 "Red": (255, 0, 0)}


def color_difference(color1, color2):
    return sum([abs(component1 - component2) for component1, component2 in zip(color1, color2)])


my_color = (current_Rval, current_Gval, current_Bval)
differences = [[color_difference(my_color, target_value), target_name] for target_name, target_value in
               TARGET_COLORS.items()]
differences.sort()  # sorted by the first element of inner lists
my_color_name = differences[0][1]
print('The color is closest to: ', my_color_name)
