import cv2
import numpy as np
img = cv2.imread('./456.jpg',cv2.IMREAD_COLOR)
cv2.imshow("456", img)
k=cv2.waitKey(0)
if k==27:    
    cv2.destroyAllWindows()
    