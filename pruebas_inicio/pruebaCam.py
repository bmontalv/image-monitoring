#!/usr/bin/python

import numpy as np
import cv2

camara = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = camara.read()

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    #cv2.imshow('frame',gray)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
camara.release()
cv2.destroyAllWindows()
