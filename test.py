import cv2
import numpy as np
img = cv2.imread('./123.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow("123", img)
k=cv2.waitKey(0)
if k==27:    
    cv2.destroyAllWindows()
elif k==ord('s'):
     cv2.imwrite('output.png',img)
     cv2.destroyAllWindows()