import numpy as np
import cv2
from tqdm import _tqdm

#img = cv2.imread('rektor.jpg', 1)
img = cv2.imread('Lenna.png')

#numpy manual
row, col, ch = img.shape

#grayscale
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#openCV function
add = cv2.add(img, 50)
sub = cv2.subtract(img, 50)
mul = cv2.multiply(img, 2)
div = cv2.divide(img, 2)


#output original
cv2.imshow('LENNA ORI', img)

cv2.imshow('Addition', add)
cv2.imshow('Subtration', sub)
cv2.imshow('Multiply', mul)
cv2.imshow('division', div)


cv2.waitKey(0)
