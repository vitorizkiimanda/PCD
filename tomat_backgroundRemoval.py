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
    img = cv2.resize(img, (0,0), fx=0.1 , fy=0.1)
    
    hsv = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)


    #numpy manual cvtColor
    row, col, ch = img.shape

    #bikin kanvas kosong
    graykanvas = np.zeros((row,col,1), np.uint8)

    ##translate image ke graykanvas perpixel menggunakan for

    graykanvas[0:1000 , 185:210] = 255
    graykanvas[150:175] = 255

    manual_rgb2hsv = vri.RGB2HSV(img)
    cv2.imshow("manual_RGB2HSV", manual_rgb2hsv)

    #grayscale by rumus
    for i in range(0,row):
        for j in range(0,col):
            blue, green ,red = hsv[i,j]
            gray = red * 0.299 + green * 0.587 + blue * 0.114
            graykanvas.itemset((i,j,0),gray)


    #biner
    for i in range(0,row):
        for j in range(0,col):
            gray = graykanvas[i,j]
            if(gray>150):
                gray=255
            else:
                gray=0

            graykanvas.itemset((i,j,0),gray)



    kernel3 = np.ones((5,5), np.uint8)
    dilation3 = cv2.dilate(graykanvas, kernel3, iterations=10)
    erotion3 = cv2.erode(dilation3, kernel3, iterations=10)


    cv2.imshow("threshold", graykanvas)

    for i in range(0,row):
        for j in range(0,col):
            gray = erotion3[i,j]
            if(gray>150):
                gray=0
            else:
                gray=255

            graykanvas.itemset((i,j,0),gray)

    final = vri.substract(img, graykanvas)

    # cv2.imshow("tomatku", final)
    namaFoto = '%s.jpg' % (imgname);
    cv2.imwrite(namaFoto, final)
    print(namaFoto)

cv2.waitKey(0)
cv2.destroyAllWindows()
