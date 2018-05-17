import numpy as np
import cv2

img = cv2.imread('sudo.png')
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

cv2.imwrite('houghlines.jpg', img)
cv2.imshow('final', img)

img2 = cv2.imread('coin.jpg',0)
img2 = cv2.medianBlur(img2,5)
cimg = cv2.cvtColor(img2,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img2,cv2.HOUGH_GRADIENT,1,20,
                            param1=100,param2=100,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('img2',img2)
cv2.imshow('detected circles',cimg)

cv2.waitKey(0)
