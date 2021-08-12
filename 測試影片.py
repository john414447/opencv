import cv2
import numpy as np
img = cv2.imread('./789.avi',cv2.IMREAD_ANYCOLOR)
cv2.imshow("789", img)
k=cv2.waitKey(0)
if k==27:    
    cv2.destroyAllWindows()
    