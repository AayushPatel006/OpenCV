# references https://youtu.be/WQeoO7MI0Bs

import cv2
print('cv2 imported successfully')

img = cv2.imread("Resources/Aayush.jpg")
print(img.shape)

imgResize = cv2.resize(img,(500,400))
print(imgResize.shape)

imgCrop = img[900:2800,900:2500]

cv2.imshow("Output",img)
cv2.imshow("Resized Image",imgResize)
cv2.imshow("Cropped Image",imgCrop)

cv2.waitKey(0)