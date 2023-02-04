# references https://youtu.be/WQeoO7MI0Bs

import cv2
import numpy as np
img = cv2.imread("Resources/cards.png")

imgHor = np.hstack((img,img))
imgVer = np.vstack((img,img))

cv2.imshow("Horizontal",imgHor)
cv2.imshow("Vertical",imgVer)

cv2.waitKey(0)