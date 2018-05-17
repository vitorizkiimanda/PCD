import numpy as np
import cv2
import vri_pcd as vri

img = cv2.imread('REKTORAT.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 200, 250, apertureSize=3)
lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
cv2.imshow('gray', gray)
cv2.imshow('edges', edges)

print(lines)
for x in range(0, len(lines)):
    for rho, theta in lines[x]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))

        cv2.line(img , (x1,y1), (x2,y2), (0,0,255), 2)

cv2.imwrite('houghlines3.jpg', img)
cv2.imshow('final', img)


cv2.waitKey(0)
