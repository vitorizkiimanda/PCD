import numpy as np
import cv2
import vri_pcd as vri

img = cv2.imread('tomatku.jpg')

cv2.imshow("ORIGINAL", img)

faceRough = vri.facedetection(img)
grayscale = vri.grayscale(faceRough)
median = vri.median_filter(grayscale, 7)
final = vri.substract(img, median)

cv2.imshow("faceRough", faceRough)
cv2.imshow("grayscale", grayscale)
cv2.imshow("median", median)

cv2.imshow("final", final)

cv2.waitKey(0)
cv2.destroyAllWindows()