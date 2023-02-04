# references https://youtu.be/WQeoO7MI0Bs

##########
import numpy as np

widthImg, heightImg = 480,640
##########
import cv2

cap = cv2.VideoCapture(0)
cap.set(3,widthImg) #setting width
cap.set(4,heightImg) #setting height
cap.set(10,100) #setting brightness

def preProcessing(img):
    imgGrey = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    imgBlur = cv2.GaussianBlur(imgGrey, (5,5), 1)
    imgCanny = cv2.Canny(imgBlur, 200, 200)
    kernel = np.ones((5,5))
    imgDial = cv2.dilate(imgCanny,kernel,iterations=2)
    imgThres = cv2.erode(imgDial,kernel,iterations=1)
    return imgThres

def getContours(img):
    biggest = np.array([])
    maxArea = 0
    contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) #getting individual contours
    for cnt in contours:
        area = cv2.contourArea(cnt) #getting area of each contour
        if area > 5000:
            #cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3) #drawing each contour
            peri = cv2.arcLength(cnt,True) #finding length of each contour
            approx = cv2.approxPolyDP(cnt,0.02*peri,True) #finds location of each points
            if len(approx) == 4 and area > maxArea:
                biggest = approx
                maxArea = area
    cv2.drawContours(imgContour, biggest, -1, (255, 0, 0), 20)
    return biggest

def reorder(myPoints):
    myPoints = myPoints.reshape((4,2))
    myPointsNew = np.zeros((4,1,2),np.int32)
    add = myPoints.sum(1)

    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]
    diff = np.diff(myPoints,axis=1)
    myPointsNew[1] = myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]
    # print(myPointsNew)
    return myPointsNew


def getWrap(img,biggest):
    biggest = reorder(biggest)
    # print(biggest.shape)
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])
    matrix = cv2.getPerspectiveTransform(pts1,pts2)
    imgOutput = cv2.warpPerspective(img, matrix, (widthImg, heightImg))
    imgCropped = imgOutput[20:imgOutput.shape[0]-20,20:imgOutput.shape[1]-20]
    imgCropped = cv2.resize(imgCropped,(widthImg,heightImg))
    return imgCropped

while True:
    success, img = cap.read()
    img = cv2.resize(img,(widthImg,heightImg))
    imgContour = img.copy()
    imgThres = preProcessing(img)
    biggest = getContours(imgThres)
    if biggest.size != 0:
        imgWrap = getWrap(img,biggest)
        cv2.imshow("Document",imgWrap)
    cv2.imshow("Camera",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break