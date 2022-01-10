import cv2




def returnMarkedBubbles(referenceGlass, currentGlass):
    temporaryRefGlass = referenceGlass.copy()
    temporaryCurrGlass = currentGlass.copy()
    first_gray = cv2.cvtColor(temporaryRefGlass, cv2.COLOR_BGR2GRAY)
    first_gray = cv2.GaussianBlur(first_gray, (21, 21), 0)

    gray = cv2.cvtColor(temporaryCurrGlass, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # In each iteration, calculate absolute difference between current frame and reference frame
    difference = cv2.absdiff(gray, first_gray)

    # Apply thresholding to eliminate noise
    thresh = cv2.threshold(difference, 30, 255, cv2.THRESH_BINARY)[1]
    #thresh = cv2.dilate(thresh, None, iterations=2)

    #cv2.imshow("thresh", thresh)
    return thresh