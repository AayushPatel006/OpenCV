# references https://youtu.be/WQeoO7MI0Bs

import cv2
import numpy as np




cap = cv2.VideoCapture(0)
cap.set(3,640) #setting width
cap.set(4,480) #setting height
cap.set(10,100) #setting brightness

myColors = [ [9,63,79,42,255,255],  # green
             [143,0,203,179,192,255] ]    #pink

myColorValues = [ [0,255,0], #bgr  green
                  [255,0,255] ] # pink

myPoints = []    #[ x, y, colorId]

def findColor(img,myColors,myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    count = 0
    newPoints = []
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x,y = getContours(mask)
        cv2.circle(imgResult,(x,y),10,myColorValues[count],cv2.FILLED)
        if x != 0 and y!=0:
            newPoints.append([x,y,count])
        count += 1
        #cv2.imshow(str(color[0]), mask)
    return newPoints

def getContours(img):
    contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) #getting individual contours
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt) #getting area of each contour
        if area > 500:
            cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3) #drawing each contour
            peri = cv2.arcLength(cnt,True) #finding length of each contour
            approx = cv2.approxPolyDP(cnt,0.02*peri,True) #finds location of each points
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)  #gives the (x,y) and width, height of each shapes
    return x+w//2,y

def drawOnCanvas(myPoints, myColorValues):
    for points in myPoints:
        cv2.circle(imgResult, (points[0], points[1]), 10, myColorValues[points[2]], cv2.FILLED)

while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img,myColors,myColorValues)
    if len(newPoints) != 0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints) != 0:
        drawOnCanvas(myPoints,myColorValues)

    cv2.imshow("Webcam", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break