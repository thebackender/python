import cv2
import numpy as np
 
WIDTH = 320
HEIGHT = 180

cap = cv2.VideoCapture('tik.mp4')
 
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4',fourcc, 30, (WIDTH,HEIGHT))
 
while True:
    ret, frame = cap.read()
    if ret == True:
        b = cv2.resize(frame,(WIDTH,HEIGHT),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
        out.write(b)
    else:
        break
    
cap.release()
out.release()
cv2.destroyAllWindows()