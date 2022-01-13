import numpy as np
import pixellib
from pixellib.instance import custom_segmentation
import time
SG_segmentation = custom_segmentation()
SG_segmentation.inferConfig(num_classes= 2, class_names= ["BG", "indicator", "glass"])
SG_segmentation.load_model("mask_rcnn_models/mask_rcnn_model.023-0.141302.h5")



for i in range(20):
    start = time.time()
    if i < 10:
        # Image from raspberry pi
        SG_segmentation.segmentImage("test_image/SG_RPI_Capture_scale_10.jpg", show_bboxes=True,
                                   output_image_name="test_image/SG_RPI_Capture_outpu.jpg",
                                   extract_segmented_objects=True, save_extracted_objects=True)
    else:
        # Image from raspberry pi
        SG_segmentation.segmentImage("test_image/SG_RPI_Capture.jpg", show_bboxes=True,
                                     output_image_name="test_image/SG_Phone_Capture_output.jpg",
                                     extract_segmented_objects=True, save_extracted_objects=True)
    done = time.time()
    elapsed = done - start
    print(i,": ELAPSED: ", elapsed)
