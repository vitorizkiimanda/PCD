import cv2
import numpy as np

def grayscale(source):
		row, col, ch = source.shape
		graykanvas = np.zeros((row,col,1), np.uint8)
		for i in range(0, row):
			for j in range(0, col):
				blue, green, red = source[i,j]
				gray = red * 0.299 + green * 0.587 + blue * 0.114
				graykanvas.itemset((i, j, 0), gray)
		return graykanvas

def strecth(image):
	row, col, ch = image.shape
	output = np.zeros((row,col,1), np.uint8)
	min=max=image[0,0]
	for i in range(0, row):
		for j in range(0, col):
			if image[i,j] < min:
				min = image[i,j]
			if image[i,j] > max:
				max = image[i,j]
	bawah = max - min
	for i in range(0, row):
		for j in range(0, col):
			normalize = (float(image[i,j] - min)/bawah)*255
			output.itemset((i,j,0), normalize)
	return output
	
def histogram(image):
	buckets = [0] * 300
	arraynorm = [0] * 300
	scale = 1
	histocol = 255
	historow = 150
	border = 30
	kanvashisto = np.zeros(((historow+border),histocol,1), np.uint8)
	row, col, raw = image.shape
	graykanvas = np.zeros((row,col,1), np.uint8)
	for i in range(0, row):
		for j in range(0, col):
			buckets[int(image[i,j])]+=1
	maks = max(buckets)
	mins = min(buckets)
	for intent in range(0, 255):
		jumlahperbar = buckets[intent]
		normal = int(float(jumlahperbar) / float(maks) * float(historow))
		arraynorm[intent] = normal
		for y in range(int(historow-normal+border), historow+border):
			kanvashisto.itemset((y, intent, 0), 255)
	return kanvashisto

def equalization(image):	
	row, col, ch = image.shape
	canvas = np.zeros((row,col,1), np.uint8)
	
	#hitung kemunculan tiap pixel
	pixel=[0]*256
	for i in range(0, row):
		for j in range(0, col):
			nilai = int(image[i,j])
			pixel[nilai]+=1
			
	#hitung peluang nilai kemunculan tiap pixel
	for i in range(0, 256):
		pixel[i] = float(pixel[i])/float(row*col)
		
	#hitung histogram kumulatif
	for i in range(0, 256):
		pixel[i] = pixel[i]+pixel[i-1]
		
	#hitung equalized histogram
	for i in range(0,256):
		pixel[i]=pixel[i]*(256-1)
		
	#masukkan ke dalam kanvas
	for i in range(0, row):
		for j in range(0, col):
			nilai = int(image[i,j])
			nilai = pixel[nilai]
			canvas.itemset((i,j,0),nilai)

	return canvas

image = cv2.imread('car.png')
image = grayscale(image)
img_contrast = strecth(image)
img_equalized = equalization(image)

cv2.imshow("aseli", image)
cv2.imshow("contrast", img_contrast)
cv2.imshow("equalized", img_equalized)

cv2.imshow("histo aseli", histogram(image))
cv2.imshow("histo contrast", histogram(img_contrast))
cv2.imshow("histo equalized", histogram(img_equalized))

cv2.waitKey(0)
