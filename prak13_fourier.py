import cv2
import numpy as np
from matplotlib import pyplot as plt

size = 30
img = cv2.imread('REKTORAT.jpg', 0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 1 * np.log(np.abs(fshift))

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])

plt.show()

rows, cols = img.shape
crow, ccol = int(rows/2 ), int(cols /2)
fshift[crow - size:crow + size, ccol - size:ccol + size] = 0
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

plt.subplot(131), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(20 * np.log(np.abs(fshift)), cmap='gray')
plt.title('Magnitude Filter'), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(img_back, cmap='gray')

plt.show()

cv2.imshow('res2', img_back)
cv2.waitKey(0)
cv2.destroyAllWindows()
