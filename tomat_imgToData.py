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
    jingga = 0
    hijau = 0

    #menghitung proporsional warna
    ## merah , orange, hijau
    row, col, ch = img.shape
    output = np.zeros((row, col, 3), np.uint8)
    for i in range(0, row):
        for j in range(0, col):
            b, g, r = img[i, j]
            print(b,g,r)
            if(b & g  & r):
                if(r-g > 90):
                    # print("red")
                    merah = merah + 1
                elif(r-g >50):
                    # print("orange")
                    jingga = jingga + 1
                else:
                    # print("green")
                    hijau = hijau + 1

    M = merah
    J = jingga
    H = hijau

    M = float(M / (M + J + H))
    J = float(J / (M + J + H))
    H = float(H / (M + J + H))

    # data = imgname + "," + merah + "," + hijau + "\n"
    data = '%s,%f,%f,%f' % (imgname, M,J,H)
    data = data + "\n"
    print(data)
    csv.write(data)

cv2.waitKey(0)
cv2.destroyAllWindows()
