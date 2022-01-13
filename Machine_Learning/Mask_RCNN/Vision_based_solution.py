from VBS_functions import *
count = 0
while count < 11:
    SG_segmentation.segmentImage('testing/ImageNumber'+str(count)+'.jpg', show_bboxes=True,
                               output_image_name="SegmentedImages/SG_RPI_Capture_outpu.jpg",
                               extract_segmented_objects=True, save_extracted_objects=True)
    indic_img = cv2.imread('segmented_object_1.jpg')
    indic_glass_img = cv2.imread('segmented_object_2.jpg')
    buble_img = cv2.imread('segmented_object_3.jpg')

    #Moisture detection
    yellowColorPercentage = moisture_detect(indic_img)
    moistureLevel = np.append(moistureLevel, yellowColorPercentage)

    #Quality detection
    quality_detect(indic_img, indic_glass_img, buble_img)

    count = count + 1