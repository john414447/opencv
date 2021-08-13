import cv2
import numpy as np

img = cv2.imread('1.jpg')
lower_reso = cv2.pyrDown(higher_reso)
higher_reso2 = cv2.pyrUp(lower_reso)