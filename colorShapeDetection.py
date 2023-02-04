# references https://youtu.be/WQeoO7MI0Bs

import cv2
import numpy as np

def getContours(img):
    contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) #getting individual contours
    for cnt in contours:
        area = cv2.contourArea(cnt) #getting area of each contour
        print(area)
        if area > 500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3) #drawing each contour
            peri = cv2.arcLength(cnt,True) #finding length of each contour
            print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True) #finds location of each points
            print(len(approx))  #finding no. of sides of the shape
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)  #gives the (x,y) and width, height of each shapes
            if objCor == 3:
                objectType = "Tri"
            elif objCor == 4:
                aspectRatio = w/float(h)
                if aspectRatio > 0.95 and aspectRatio < 1.05:
                    objectType = "Square"
                else:
                    objectType = "Rectengle"
            elif objCor > 4:
                objectType = "Circles"
            else:
                objectType = "Null"
            cv2.rectangle(imgContour,(x,y),( (x+w) , (y+h) ),(0,255,0),2)
            cv2.putText(imgContour,objectType,
                        ( x+(w//2)-10 , y+(h//2)-10 ),cv2.FONT_HERSHEY_SIMPLEX,0.5, (0,0,0),2)

path = "Resources/shapes.png"
img = cv2.imread(path)
imgContour = img.copy()
imgGrey = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
imgBlur = cv2.GaussianBlur(imgGrey,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50) #identifing the borders of the image
imgBlank = np.zeros_like(img)
getContours(imgCanny)

cv2.imshow("Original",img)
cv2.imshow("Grey Image",imgGrey)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Blank Image",imgBlank)
cv2.imshow("Contour Image",imgContour)

cv2.waitKey(0)
