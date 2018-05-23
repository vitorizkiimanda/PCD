import numpy as np
import cv2
import vri_pcd as vri

import glob
import os,sys

## Get all the png image in the PATH_TO_IMAGES
imgnames = sorted(glob.glob("penampakkan/*/*.jpg"))

csv = open("tomat.csv", "w")

for imgname in imgnames:
    img = cv2.imread(imgname)

    #deklarasi variabel counter warna
    merah = 0
    biru = 0
    hijau = 0

    merahTotal = 0
    biruTotal = 0
    hijauTotal = 0

    hue = 0
    saturation = 0
    value = 0

    hueTotal = 0
    saturationTotal = 0
    valueTotal = 0


    #menghitung proporsional warna
    ## merah , orange, hijau
    row, col, ch = img.shape
    output = np.zeros((row, col, 3), np.uint8)
    for i in range(0, row):
        for j in range(0, col):
            b, g, r = img[i, j]
            print(b,g,r)
            merahTotal = merahTotal + r
            hijauTotal = hijauTotal + g
            biruTotal = biruTotal + b

            if(r): merah = merah + 1
            if(g): hijau = hijau + 1
            if(b): biru = biru + 1

    M = merahTotal
    B = biruTotal
    H = hijauTotal

    M = M / merah
    B = B / biru
    H = H/ hijau

    img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

    for i in range(0, row):
        for j in range(0, col):
            h, s, v = img[i, j]
            print(h,s,v)
            hueTotal = hueTotal + h
            saturationTotal = saturationTotal + s
            valueTotal = valueTotal + v

            if(h): hue = hue + 1
            if(s): saturation = saturation + 1
            if(v): value = value + 1

    H2 = hueTotal
    S = saturationTotal
    V = valueTotal

    H2 = H2 / hue
    S = S / saturation
    V = V / value

    # data = imgname + "," + merah + "," + hijau + "\n"
    data = '%s,%f,%f,%f,%f,%f,%f' % (imgname, M,H,B,H2,S,V)
    data = data + "\n"
    print(data)
    csv.write(data)

cv2.waitKey(0)
cv2.destroyAllWindows()
