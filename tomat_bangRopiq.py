import cv2
import numpy as np

import vri_pcd as vri

import glob
import os,sys

## Get all the png image in the PATH_TO_IMAGES
imgnames = sorted(glob.glob("1/*.jpg"))


for imgname in imgnames:

    kernel3 = np.ones((3,3),np.uint8)
    kernel5 = np.ones((5,5),np.uint8)
    kernel12 = np.ones((12,12),np.uint8)
    kernel24 = np.ones((24,24),np.uint8)

    tomat = cv2.imread(imgname)

    b,g,r = cv2.split(tomat)

    def subgraygray (gray1, gray2):
        row, col = gray2.shape
        output = np.zeros((row,col,1), np.uint8)
        for i in range(0,row):
            for j in range(0,col):
                if int(gray1[i,j])-int(gray2[i,j]) < 0 :
                    output.itemset((i,j,0),0)
                else:
                    output.itemset((i,j,0),int(gray1[i,j])-int(gray2[i,j]))
        return output

    def subrgbgray(rgb,treshold):
        row, col , raw = rgb.shape
        output = np.zeros((row,col,3), np.uint8)
        for i in range(0,row):
            for j in range(0,col):
                if treshold[i,j] != 255:
                    output.itemset((i,j,0),0)
                    output.itemset((i,j,1),0)
                    output.itemset((i,j,2),0)
                else:
                    output[i,j]=rgb[i,j]
        return output

    tomat_segmented = cv2.subtract(r,g)

    # ret, tomat_segmented = cv2.threshold(tomat_segmented, 63, 255, cv2.THRESH_BINARY)

    # tomat_segmented = cv2.adaptiveThreshold(tomat_segmented, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    #                                  cv2.THRESH_BINARY, 11, 0)

    tomat_segmented = cv2.adaptiveThreshold(tomat_segmented,255,cv2.ADAPTIVE_THRESH_MEAN_C,
            cv2.THRESH_BINARY,63,0)


    tomat_segmented = cv2.dilate(tomat_segmented,kernel3, iterations=1)
    tomat_segmented = cv2.erode(tomat_segmented, kernel3, iterations= 1)

    cv2.imshow('threshold', tomat_segmented)


    tomat_segmented = cv2.morphologyEx(tomat_segmented, cv2.MORPH_CLOSE, kernel24)
    # tomat_segmented = cv2.blur(tomat_segmented, (1,1))

    tomat_segmented = subrgbgray(tomat, tomat_segmented)

    # tomat_segmented = cv2.subtract(tomat,tomat_segmented)


    kernel_rectangular = np.array([[1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1]], np.uint8)

    kernel_eliptical = np.array([[0, 0, 1, 0, 0],
           [1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1],
           [0, 0, 1, 0, 0]], np.uint8)

    kernel_cross = np.array([[0, 0, 1, 0, 0],
           [0, 0, 1, 0, 0],
           [1, 1, 1, 1, 1],
           [0, 0, 1, 0, 0],
           [0, 0, 1, 0, 0]], np.uint8)

    # erosion3 = cv2.erode(tomat_segmented,kernel3,iterations = 2)
    # erosion5 = cv2.erode(tomat_segmented,kernel5,iterations = 2)
    # tomat_segmented = cv2.dilate(tomat_segmented,kernel3,iterations = 2)
    # dilation5 = cv2.dilate(img,kernel5,iterations = 2)

    # tomat_segmented = cv2.dilate(tomat_segmented, kernel3, iterations= 5)
    # closing = cv2.erode(closing, kernel3, iterations= 5)
    #
    # opening_otomatis = cv2.morphologyEx(img_opening, cv2.MORPH_OPEN, kernel12)

    # cv2.imshow('erosi3', erosion3)
    # cv2.imshow('erosi5', erosion5)
    # cv2.imshow('delation3', dilation3)
    # cv2.imshow('delation5', dilation5)

    # cv2.imshow('target', img)
    # cv2.imshow('ori closing', img_closing)
    # cv2.imshow('ori opening', img_opening)
    # cv2.imshow('opening', opening)
    # cv2.imshow('opening otomatis', opening_otomatis)
    # cv2.imshow('closing', closing)


    cv2.imshow('Ori', tomat_segmented)
    namaFoto = '%s.jpg' % (imgname)
    cv2.imwrite(namaFoto, tomat_segmented)
    print(namaFoto)

cv2.waitKey(0)