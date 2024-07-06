# Erik Kaufman

import numpy as np
import cv2 as cv

blobDetector = cv.SimpleBlobDetector.create()

# caputres the video from the camera 
cap = cv.VideoCapture(0)

# Variable that can hold if the frame is displayed in color
useColor = False

if not cap.isOpened():
 print("Cannot open camera")
 exit()

# Main loop
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    # Process image
    keypoints = blobDetector.detect(frame)

    im_with_keypoints = cv.drawKeypoints(frame, keypoints, np.array([]), (0,0,255), cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # Display the resulting frame
    cv.imshow('keypoints', im_with_keypoints)

    # press q to quit
    if cv.waitKey(1) == ord('q'):
        break
 
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()