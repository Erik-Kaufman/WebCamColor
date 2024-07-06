# Erik Kaufman

import numpy as np
import cv2


# caputres the video from the camera 
cap = cv2.VideoCapture(0)

boundaries = [
    ([17, 15, 100], [50, 56, 200]), # red range
	([86, 31, 4], [220, 88, 50]), #
	([25, 146, 190], [62, 174, 250]),
	([103, 86, 65], [145, 133, 128])
]
color = 0

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
    # loop over the boundaries
    lower, upper = boundaries[color]
    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")

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