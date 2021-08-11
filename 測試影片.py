import cv2
import numpy as np
img = cv2.imread('./789.mp4',cv2.IMREAD)
cv2.imshow("123", img)
k=cv2.waitKey(0)
if k==27:    
    cv2.destroyAllWindows()
    