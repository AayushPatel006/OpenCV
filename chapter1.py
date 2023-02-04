# references https://youtu.be/WQeoO7MI0Bs

import cv2
print('package imported')
import numpy as np

img = cv2.imread('Resources/Aayush.JPG')
kernal = np.ones( (5,5), np.uint8)

imgGrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGrey, (7,7) , 0)
imgCanny = cv2.Canny(img, 150, 200)
imgDialation = cv2.dilate(imgCanny, kernal, iterations=1)
imgEroded = cv2.erode(imgDialation, kernal, iterations=1)

cv2.imshow('Grey Image',imgGrey)
cv2.imshow('Blur Image',imgBlur)
cv2.imshow('Canny Image',imgCanny)
cv2.imshow('Dialation Image',imgDialation)
cv2.imshow('Errosion Image',imgEroded)

cv2.waitKey(0)