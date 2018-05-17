import numpy as np
import cv2
import vri_pcd as vri

img = cv2.imread('koinIPB.jpg', 0)
kernel = np.array([[-1,-1,-1], [-1,8,-1], [-1,-1,-1]])

result = vri.convolution(img, kernel)

cv2.imshow("original", img)
cv2.imshow("Result Convolution", result)

cv2.waitKey(0)
