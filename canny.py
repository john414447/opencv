import cv2
import numpy as np
from matplotlib import pyplot as plt
def nothing(x):
    pass

img = cv2.imread('./5.jpg', 0)
img = cv2.resize(img,(800,600))
cv2.namedWindow('5')
cv2.createTrackbar('min','5',0,255,nothing)
cv2.createTrackbar('max','5',0,255,nothing)
cv2.imshow('5',img)
while(True):
    min = cv2.getTrackbarPos('min','5')
    max = cv2.getTrackbarPos('max','5')
    edges = cv2.Canny(img, min, max)
    cv2.imshow('canny',edges)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()  