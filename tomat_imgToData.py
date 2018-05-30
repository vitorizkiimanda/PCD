import numpy as np
import cv2
import vri_pcd as vri

import glob
import os,sys

from random import randint

#make CSV
csv = open("tomatBerat.csv", "w")

header = '%s,%s,%s,%s,%s,%s,%s,%s,%s' % ("red", "green", "blue", "hue", "saturation", "value","pixels","berat", "kematangan")
header = '%s,%s,%s,%s,%s,%s,%s' % ("red", "green", "blue", "hue", "saturation", "value", "kematangan")
header = '%s,%s' % ("pixels","berat")
header = header + "\n"
#print(header)
#csv.write(header)

#loop all folder
for nomorFolder in range(1, 20):

    ## Get all the png image in the PATH_TO_IMAGES
    imgnames = sorted(glob.glob("penampakkan/"+'%s' % (nomorFolder)+"/*.jpg"))


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
                #print(b,g,r)
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


        totalPixel = merah + biru + hijau
        totalPixel = totalPixel/(row*col)

        img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

        for i in range(0, row):
            for j in range(0, col):
                h, s, v = img[i, j]
                #print(h,s,v)
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



        if(nomorFolder==1):
            Kematangan = 2
            Berat = randint(33,37)
        elif (nomorFolder == 2):
            Kematangan = 5
            Berat = randint(53,57)
        elif (nomorFolder == 3):
            Kematangan = 1
            Berat = randint(27,32)
        elif (nomorFolder == 4):
            Kematangan = 3
            Berat = randint(54,58)
        elif (nomorFolder == 5):
            Kematangan = 4
            Berat = randint(25,29)
        elif (nomorFolder == 6):
            Kematangan = 3
            Berat = randint(36,40)
        elif (nomorFolder == 7):
            Kematangan = 5
            Berat = randint(41,45)
        elif (nomorFolder == 8):
            Kematangan = 5
            Berat = randint(29,33)
        elif (nomorFolder == 9):
            Kematangan = 5
            Berat = randint(41,52)
        elif (nomorFolder == 10):
            Kematangan = 3
            Berat = randint(33,37)
        elif (nomorFolder == 11):
            Kematangan = 2
            Berat = randint(28,32)
        elif (nomorFolder == 12):
            Kematangan = 3
            Berat = randint(50,54)
        elif (nomorFolder == 13):
            Kematangan = 4
            Berat = randint(43,47)
        elif (nomorFolder == 14):
            Kematangan = 4
            Berat = randint(60,64)
        elif (nomorFolder == 15):
            Kematangan = 2
            Berat = randint(24,28)
        elif (nomorFolder == 16):
            Kematangan = 3
            Berat = randint(38,42)
        elif (nomorFolder == 17):
            Kematangan = 2
            Berat = randint(34,38)
        elif (nomorFolder == 18):
            Kematangan = 5
            Berat = randint(49,53)
        elif (nomorFolder == 19):
            Kematangan = 3
            Berat = randint(37,42)

        # data = imgname + "," + merah + "," + hijau + "\n"

        data = '%f,%d' % (totalPixel, Berat)
#        data = '%f,%f,%f,%f,%f,%f,%d' % (M,H,B,H2,S,V,Kematangan)
        data = data + "\n"
        print(nomorFolder)
        csv.write(data)

cv2.waitKey(0)
cv2.destroyAllWindows()
