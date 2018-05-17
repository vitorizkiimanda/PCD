import numpy as np
import cv2
import vri_pcd as vri

img = cv2.imread('FACE DETECTION.png')
img_gray = vri.grayscale(img)

#canny -> double thresholding : x < y
img_canny = cv2.Canny(img, 100,240)

#sobel
img_sobelx = cv2.Sobel(img_gray, cv2.CV_8U, 1,0,ksize=3)
img_sobely = cv2.Sobel(img_gray, cv2.CV_8U, 0,1,ksize=3)
img_sobel  = img_sobelx + img_sobely

#prewitt
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx = cv2.filter2D(img_gray, -1 , kernelx)
img_prewitty = cv2.filter2D(img_gray, -1 , kernely)
img_prewitt = img_prewittx + img_prewitty


##manual Prewitt
img_prewittManual = vri.prewitt(img_gray, kernelx)

cv2.imshow("Original Image", img)
cv2.imshow("Canny", img_canny)
cv2.imshow("Sobel", img_sobel)
cv2.imshow("Prewitt X", img_prewittx)
cv2.imshow("Prewitt Y", img_prewitty)
cv2.imshow("Manual Prewitt", img_prewittManual)

cv2.imshow("Prewitt", img_prewitt)

cv2.waitKey(0)
cv2.destroyAllWindows()