import numpy as np
import cv2
import vri_pcd as vri

img = cv2.imread('car.png')
img = vri.grayscale(img)
img_contrast = vri.strecth(img)
img_equalized = vri.equalization(img)

cv2.imshow("original", img)
cv2.imshow("After Contrast", img_contrast)
cv2.imshow("After Equalized", img_equalized)

cv2.imshow("Histogram Original", vri.histogram(img))
cv2.imshow("Histogram Contrast", vri.histogram(img_contrast))
cv2.imshow("Histogram Equalized", vri.histogram(img_equalized))

cv2.waitKey(0)
