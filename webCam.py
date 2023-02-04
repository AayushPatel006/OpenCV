# references https://youtu.be/WQeoO7MI0Bs

import cv2

# cap = cv2.VideoCapture("Resources/test_video.mp4")
cap = cv2.VideoCapture(0)
cap.set(3,640) #setting width
cap.set(4,480) #setting height
cap.set(10,100) #setting brightness

while True:
    success, img = cap.read()
    cv2.imshow("Webcam",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break