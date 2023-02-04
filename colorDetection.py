# references https://youtu.be/WQeoO7MI0Bs

import cv2
import numpy as np

def empty(a):
    pass

path = "Resources/t_1.jpeg"
cv2.namedWindow('TrackBars')
cv2.resizeWindow('TrackBars',640,240)
cv2.createTrackbar('Hue Min','TrackBars',10,179,empty)
cv2.createTrackbar('Hue Max','TrackBars',145,179,empty)
cv2.createTrackbar('Sat Min','TrackBars',99,255,empty)
cv2.createTrackbar('Sat Max','TrackBars',255,255,empty)
cv2.createTrackbar('Val Min','TrackBars',132,255,empty)
cv2.createTrackbar('Val Max','TrackBars',255,255,empty)
img = cv2.imread(path)
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

while True:
    h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max","TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min","TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max","TrackBars")
    v_min = cv2.getTrackbarPos("Val Min","TrackBars")
    v_max = cv2.getTrackbarPos("Val Max","TrackBars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow("Original",img)
    cv2.imshow("HSV Output",imgHSV)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", imgResult)

    cv2.waitKey(1)