from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor

import pandas as pd
import numpy as np
import cv2
import vri_pcd as vri

import pickle
import time

from sklearn.metrics import confusion_matrix

#########image preparation
imgname = "TOMAT/tomat_test/1_1.jpg"
img = cv2.imread(imgname)

# resizing
img = cv2.resize(img, (0, 0), fx=0.1, fy=0.1)

hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
gray = cv2.cvtColor(hsv, cv2.COLOR_RGB2GRAY)

ret,biner_threshold = cv2.threshold(gray, 150, 255,cv2.THRESH_BINARY )

kernel3 = np.ones((5, 5), np.uint8)
dilation3 = cv2.dilate(biner_threshold, kernel3, iterations=10)
erotion3 = cv2.erode(dilation3, kernel3, iterations=10)
biner_threshold = cv2.bitwise_not(erotion3)

final = vri.substract(img, biner_threshold)

#cv2.imshow('mask', erotion3)
#cv2.imshow("masking result",final)
#cv2.imshow("original",img)
#cv2.waitKey()


#######imgage processing
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
        b, g, r = final[i, j]
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
#print(totalPixel)

final = cv2.cvtColor(final, cv2.COLOR_RGB2HSV)

for i in range(0, row):
    for j in range(0, col):
        h, s, v = final[i, j]
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

##########making csv of input image
csv = open("tomatInput.csv", "w")
header = '%s,%s,%s,%s,%s,%s,%s' % ("red", "green", "blue", "hue", "saturation", "value","pixels")
header = header + "\n"
csv.write(header)

dataKematangan = ([M,H,B,H2,S,V],[M,H,B,H2,S,V])
#print(dataKematangan)
dataBerat = ([totalPixel],[totalPixel])

##########prediction
# load the model from disk
filename = 'modelTomatBerat.sav'
modelBerat = pickle.load(open(filename, 'rb'))

filename = 'modelTomatKematangan.sav'
modelKematangan = pickle.load(open(filename, 'rb'))


#prediction
kematanganPredict = modelKematangan.predict(dataKematangan)  #nnti ini test : inputan baru

if(kematanganPredict[0]==1): kematangan = "Sangat Matang"
elif(kematanganPredict[0]==2): kematangan = "Matang"
elif(kematanganPredict[0]==3): kematangan = "Cukup Matang"
elif(kematanganPredict[0]==4): kematangan = "Setengah Matang"
elif(kematanganPredict[0]==5): kematangan = "Mentah"

print("prediksi tomat","'",imgname,"'")
print("kematangan :",kematangan)

beratPredict = modelBerat.predict(dataBerat)  #nnti ini test : inputan baru
print("berat",beratPredict[0],"gram")