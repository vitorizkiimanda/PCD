import cv2
import numpy as np


kernel3 = np.ones((3,3),np.uint8)
kernel5 = np.ones((5,5),np.uint8)
kernel12 = np.ones((12,12),np.uint8)
kernel24 = np.ones((24,24),np.uint8)
kernel48 = np.ones((48,48),np.uint8)
kernel100 = np.ones((100,100),np.uint8)

face = cv2.imread('faceBald.jpg')

b,g,r = cv2.split(face)

def subrgbgray(rgb,treshold):
    row, col , raw = rgb.shape
    #print row*col
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

face_segmented = cv2.subtract(r,g)

ret, face_segmented = cv2.threshold(face_segmented, 25,255,cv2.THRESH_BINARY)

face_segmented = cv2.morphologyEx(face_segmented, cv2.MORPH_CLOSE, kernel12)

face_segmented = subrgbgray(face, face_segmented)




cv2.imshow('face only', face_segmented)
cv2.imshow('Ori', face)

cv2.waitKey(0)