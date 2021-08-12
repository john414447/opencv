import numpy as np
import cv2

img_path = './1.jpg'
img = cv2.imread(img_path)
cv2.namedWindow("image", flags= cv2.WINDOW_NORMAL | cv2.WINDOW_FREERATIO)
cv2.namedWindow("image_roi", flags= cv2.WINDOW_NORMAL | cv2.WINDOW_FREERATIO)
cv2.imshow("image", img)
showCrosshair = True
fromCenter = False
rect = cv2.selectROI("image", img, showCrosshair, fromCenter)
print("選中矩形區域")
(x, y, w, h) = rect
imCrop = img[y : y+h, x:x+w]
cv2.imshow("image_roi", imCrop)
cv2.imwrite("image_roi.png", imCrop)
cv2.waitKey(0)
