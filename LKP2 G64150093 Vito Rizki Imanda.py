import numpy as np
import cv2
import vri_pcd as vri

def imageDiff(img1, img2):

    img1 = vri.grayscale(img1)
    img2 = vri.grayscale(img2)

    avg1 = vri.meanImage(img1)
    avg2 = vri.meanImage(img2)

    img1 = vri.intensity(img1, avg1)
    img2 = vri.intensity(img2, avg2)

    result = vri.substraction(img1, img2)

    return result


cameraman = cv2.imread("cameraman.jpg")
equalized = cv2.imread("equalized.jpg")

outputImageDiff = imageDiff(cameraman, equalized)

cv2.imshow('Result', outputImageDiff)
cv2.waitKey(0)
