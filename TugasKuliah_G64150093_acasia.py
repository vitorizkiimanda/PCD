import numpy as np
import cv2

img = cv2.imread('acasia.png')

#numpy manual cvtColor
row, col, ch = img.shape

#bikin kanvas kosong
graykanvas = np.zeros((row,col,1), np.uint8)

##translate image ke graykanvas perpixel menggunakan for

graykanvas[0:1000 , 185:210] = 255
graykanvas[150:175] = 255

#grayscale by rumus
for i in range(0,row):
    for j in range(0,col):
        blue, green ,red = img[i,j]
        gray = red * 0.299 + green * 0.587 + blue * 0.114
        graykanvas.itemset((i,j,0),gray)

#cv2.imshow('Acasia Grayscale', graykanvas)


#biner
for i in range(0,row):
    for j in range(0,col):
        gray = graykanvas[i,j]
        if(gray>180):
            gray=255
        else:
            gray=0

        graykanvas.itemset((i,j,0),gray)

cv2.imshow('Acasia Biner', graykanvas)



#output original
cv2.imshow('Acasia Original', img)

#print pixel value
print(graykanvas[150:175])

cv2.waitKey(0)
