# Erik Kaufman
# fun to play with but really hard to get something useful out off if you don't have something in mind to do.

import numpy as np
import cv2
import pyautogui as pya
import math

# caputres the video from the camera 
cap = cv2.VideoCapture(0)

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

    # grap the color at the mouse and detect for it
    x, y = pya.position()
    px = pya.pixel(x, y)

    #reset the upper and lower turples
    upper = []
    lower = []

    # Set them to the ammount in the 
    for color in px:
        # scaled bassed on the the amount of color there is (basicly makes it a brightness detector)
        margin = (color * 100 ) / 255
        upper += [np.clip(color + math.floor(margin), 0, 255)] 
        lower += [np.clip(color - math.floor(margin), 0, 255)]
    
    print(lower)
    print(upper)

    # create NumPy arrays from the boundaries
    lower = np.array(tuple(lower), dtype = "uint8")
    upper = np.array(tuple(upper), dtype = "uint8")

    # find the colors within the specified boundaries and applythe mask
    mask = cv2.inRange(frame, lower, upper)
    output = cv2.bitwise_and(frame, frame, mask = mask)

    # show the frames
    cv2.imshow("filtered", np.hstack([frame, output]))

    # press q to quit
    if cv2.waitKey(1) == ord('q'):
        break
 
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()