import cv2

image = cv2.imread('./4.jpg')
image = cv2.resize(image, (256, 256), interpolation=cv2.INTER_AREA)
cv2.imshow('4', image)
cv2.waitKey(0)