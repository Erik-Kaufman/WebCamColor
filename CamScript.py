# Erik Kaufman

import numpy as np
import cv2 as cv

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
    
    if (not useColor):
        adjFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    else:
        adjFrame = frame

    # Display the resulting frame
    cv.imshow('frame', adjFrame)
    
    # add toggle for color -- not the exact right one for the job
    if cv.waitKey(0) == ord('c'):
       useColor = not useColor

    # press q to quit
    if cv.waitKey(1) == ord('q'):
        break
 
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()