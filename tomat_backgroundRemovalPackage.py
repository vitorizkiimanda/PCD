import numpy as np
import cv2
import vri_pcd as vri

import glob
import os,sys

## Get all the png image in the PATH_TO_IMAGES
imgnames = sorted(glob.glob("penampakkan/*/*.jpg"))

for imgname in imgnames:
    img = cv2.imread(imgname)

    # resizing
    img = cv2.resize(img, (0, 0), fx=0.1, fy=0.1)

    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    gray = cv2.cvtColor(hsv, cv2.COLOR_RGB2GRAY)

    ret,biner_threshold = cv2.threshold(gray, 150, 255,cv2.THRESH_BINARY )

    kernel3 = np.ones((5, 5), np.uint8)
    dilation3 = cv2.dilate(biner_threshold, kernel3, iterations=10)
    erotion3 = cv2.erode(dilation3, kernel3, iterations=10)

    cv2.imshow('gray', erotion3)

    biner_threshold = cv2.bitwise_not(erotion3)

    final = vri.substract(img, biner_threshold)


    #menghitung proporsional warna
    ## merah , orange, hijau

    # row, col, ch = img.shape
    # output = np.zeros((row, col, 3), np.uint8)
    # for i in range(0, row):
    #     for j in range(0, col):
    #         b, g, r = final[i, j]
    #         if(r-g > 90):
    #             print("red")
    #         elif(r-g >50):
    #             print("orange")
    #         else:
    #             print("green")

    # final = cv2.cvtColor(final, cv2.COLOR_RGB2GRAY)


    #cetak foto
    namaFoto = '%s' % (imgname);
    cv2.imwrite(namaFoto, final)
    print(namaFoto)

cv2.waitKey(0)
cv2.destroyAllWindows()
