import cv2
import numpy as np

img = cv2.imread('./3.jpg')
img = cv2.resize(img,(500,600))
rows,cols,channel = img.shape
# M = np.float32([[1,0,100],[0,1,50]])
M= cv2.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),45,2)
dst = cv2.warpAffine(img,M,(rows*2,cols*2))
# dst = cv2.flip(img,-1)

cv2.imshow('3',img)
cv2.imshow('3',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()