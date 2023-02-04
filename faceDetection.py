import cv2

faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml") # gettting database
img = cv2.imread("Resources/group.JPG")
imgGrey = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

faces = faceCascade.detectMultiScale(imgGrey,1.1,4) #getting faces data
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),( (x+w) , (y+h) ),(0,255,0),4) # drawing square over faces

cv2.imshow('Output',img)
cv2.waitKey(0)