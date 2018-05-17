import cv2
import numpy as np


kernel3 = np.ones((3,3),np.uint8)
kernel5 = np.ones((5,5),np.uint8)
kernel12 = np.ones((12,12),np.uint8)
kernel24 = np.ones((24,24),np.uint8)

# img = cv2.imread('original.jpg',0)
# img_opening = cv2.imread('opening.jpg',0)
# img_closing = cv2.imread('closing.jpg',0)
tomat = cv2.imread('tomat-single.jpg')

b,g,r = cv2.split(tomat)

def subgraygray (gray1, gray2):
    #catatan ukuran gray 1 dan 2 harus sama dan inten sitas gray2 berupa 0 atau 255 (treshold)
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

tomat_segmented = cv2.subtract(r,g)

ret, tomat_segmented = cv2.threshold(tomat_segmented, 63,255,cv2.THRESH_BINARY)

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

# erosion3 = cv2.erode(img,kernel3,iterations = 2)
# erosion5 = cv2.erode(img,kernel5,iterations = 2)
# dilation3 = cv2.dilate(img,kernel3,iterations = 2)
# dilation5 = cv2.dilate(img,kernel5,iterations = 2)

# opening = cv2.erode(img_opening, kernel3, iterations= 5)
# opening = cv2.dilate(opening,kernel3, iterations=5)
#
# closing = cv2.dilate(img_closing, kernel3, iterations= 5)
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

cv2.waitKey(0)