import numpy as np
import cv2


def grayscale(source):
    row, col, ch = source.shape
    graykanvas = np.zeros((row, col, 1), np.uint8)
    for i in range(0, row):
        for j in range(0, col):
            blue, green, red = source[i, j]
            gray = red * 0.299 + green * 0.587 + blue * 0.114
            graykanvas.itemset((i, j, 0), gray)
    return graykanvas


def meanImage(source):
    sum1 = 0
    row, col, ch = source.shape
    for i in range(0, row):
        for j in range(0, col):
            val = int(source[i, j])
            sum1 = sum1 + val
    avg = 0
    avg = sum1 / (row * col)
    return avg


def intensity(source, avg):
    row, col, ch = source.shape
    treshold = np.zeros((row, col, 1), np.uint8)
    for i in range(0, row):
        for j in range(0, col):
            val = int(source[i, j])
            if (val < avg):
                val = val * 0.5
            else:
                val = val * 2
            treshold.itemset((i, j, 0), val)
    return treshold


def substraction(img1, img2):
    row, col, ch = img1.shape
    treshold = np.zeros((row, col, 1), np.uint8)
    for i in range(0, row):
        for j in range(0, col):
            val1 = img1[i, j]
            val2 = img2[i, j]
            val = int(val1) - int(val2)

            if (val < 0):
                val = 0
            if (val > 255):
                val = 255

            treshold.itemset((i, j, 0), val)
    return treshold


def strecth(img ):
    row, col, ch = img.shape
    output = np.zeros((row, col, 1), np.uint8)
    min = max = img[0, 0]
    for i in range(0, row):
        for j in range(0, col):
            if img[i, j] < min:
                min = img[i, j]
            if img[i, j] > max:
                max = img[i, j]
    bawah = max - min
    for i in range(0, row):
        for j in range(0, col):
            normalize = (float(img[i, j] - min) / bawah) * 255
            output.itemset((i, j, 0), normalize)
    return output


def histogram(img):
    buckets = [0] * 300
    arraynorm = [0] * 300
    scale = 1
    histocol = 255
    historow = 150
    border = 30
    kanvashistogram = np.zeros(((historow + border), histocol, 1), np.uint8)
    row, col, raw = img.shape
    graykanvas = np.zeros((row, col, 1), np.uint8)
    for i in range(0, row):
        for j in range(0, col):
            buckets[int(img[i, j])] += 1
    maks = max(buckets)
    mins = min(buckets)
    for intent in range(0, 255):
        jumlahperbar = buckets[intent]
        normal = int(float(jumlahperbar) / float(maks) * float(historow))
        arraynorm[intent] = normal
        for y in range(int(historow - normal + border), historow + border):
            kanvashistogram.itemset((y, intent, 0), 255)
    return kanvashistogram


def equalization(img):
    row, col, ch = img.shape
    canvas = np.zeros((row, col, 1), np.uint8)

    # menghitung kemunculan tiap pixel
    pixel = [0] * 256
    for i in range(0, row):
        for j in range(0, col):
            nilai = int(img[i, j])
            pixel[nilai] += 1

    # menghitung peluang nilai kemunculan tiap pixel
    for i in range(0, 256):
        pixel[i] = float(pixel[i]) / float(row * col)

    # menghitung histogram kumulatif
    for i in range(0, 256):
        pixel[i] = pixel[i] + pixel[i - 1]

    # menghitung equalized histogram
    for i in range(0, 256):
        pixel[i] = pixel[i] * (256 - 1)

    # memasukkan ke dalam kanvas
    for i in range(0, row):
        for j in range(0, col):
            nilai = int(img[i, j])
            nilai = pixel[nilai]
            canvas.itemset((i, j, 0), nilai)

    return canvas

#convolution manual
def convolution(img, mask):
    row, col,ch = img.shape
    kanvas = np.zeros((row, col, 1), np.uint8)
    rowMask, colMask = mask.shape
    for i in range(0, row):
        for j in range(0, col):
            imageSum = maskSum = 0
            for a in range(int(-rowMask/2), int(rowMask-rowMask/2)):
                for b in range(int(-colMask/2), int(colMask-colMask/2)):
                    if((1+a)>=0 and (j+b)>=0):
                        imageSum += img[i+a, j+b] * mask[a+int(rowMask)//2, b+int(colMask)//2]
                        maskSum += mask[a+int(rowMask)//2, b+int(colMask)//2]
            intensitas = imageSum/maskSum
            if(intensitas > 255):
                intensitas = 255
            elif(intensitas < 0):
                intensitas = 0
            kanvas.itemset((i, j, 0), intensitas)
    return kanvas



#manual RGB2HSV
def RGB2HSV(img):
    row, col, ch = img.shape
    graykanvas = np.zeros((row, col, 3), np.uint8)
    for i in range(0, row):
        for j in range(0, col):
            blue, green, red = img[i, j]

            #casting value for calculation
            blue = float(blue)
            red = float(red)
            green = float(green)

            V = max(blue,green,red)

            if V!=0:
                S =  (V- min(red,green,blue))/V
            else :
                S = 0

            if S!=0:
                if V == red:
                    H = (60*(green-blue))/(V - min(red,green,blue))
                elif V == green:
                    H = 120 + (60*(blue-red))/(V - min(red,green,blue))
                elif V == blue:
                    H = 240 + (60*(blue-red))/(V - min(red,green,blue))

                if H < 0:
                    H = H + 360

                #normalisasi 8 bit
                S = 255 * S
                H = H / 2
                V = V

            else :
                H = 0


            #input to canvas by channel
            graykanvas.itemset((i, j, 0), H)
            graykanvas.itemset((i, j, 1), S)
            graykanvas.itemset((i, j, 2), V)

    return graykanvas


#facedetection
def facedetection(img):
    row, col,ch = img.shape
    output = np.zeros((row, col, 3), np.uint8)
    for i in range (0, row):
        for j in range (0, col):
            b, g, r = img[i,j]
            blue = 1.0*b/255
            green = 1.0*g/255
            red = 1.0*r/255

            maks = max([blue, green, red])
            mins = min([blue, green, red])

            #Calculate V
            v = maks

            #Calculate S
            if(v != 0):
                s = float((v-mins)/v)
            else:
                s = 0
            #Calculate H
            if(maks == mins):
                h=0
            elif (v == red):
                h = (60*(green - blue)/(v - mins))
            elif (v == green):
                h = (120 + 60*(blue - red)/(v-mins))
            else:
                h = (240+60*(red - green)/(v - mins))
            if(h < 0):
                h = h+360

            if((s>=0.04)&(s<=0.68)&(h>=0.0)&(h<=50.0)):
                output.itemset((i,j,0), 0)
                output.itemset((i,j,1), 0)
                output.itemset((i,j,2), 0)
            else:
                output.itemset((i, j, 0), 255)
                output.itemset((i, j, 1), 255)
                output.itemset((i, j, 2), 255)

    return output

def median_filter(img, m):
    size = m*m
    mid = int(m*m/2)
    m = int(m/2)
    row, col, ch = img.shape
    arr = [0]*size
    canvas = np.zeros((row,col,1), np.uint8)
    for i in range (m,row-m):
        for j in range (m,col-m):
            cot = 0
            for k in range (i-m, i+m+1):
                for l in range (j-m, j+m+1):
                    arr[cot] = img[k,l]
                    cot += 1
            arr.sort()
            median = arr[mid]
            canvas.itemset((i,j,0), median)
    return canvas

def substract(img, subtractor):
    grey = grayscale(img)
    row, col, ch = img.shape
    canvas = np.zeros((row, col, 3), np.uint8)
    for i in range (0, row):
        for j in range(0, col):
            b, g, r = img[i,j]
            subs = int(grey[i,j]) - int(subtractor[i,j])
            if(subs<0):
                canvas.itemset((i, j, 0), 0)
                canvas.itemset((i, j, 1), 0)
                canvas.itemset((i, j, 2), 0)
            else:
                canvas.itemset((i, j, 0), b)
                canvas.itemset((i, j, 1), g)
                canvas.itemset((i, j, 2), r)
    return canvas

#prewitt manual
def prewitt(img, mask):
    row, col,ch = img.shape
    kanvas = np.zeros((row, col, 1), np.uint8)
    rowMask, colMask = mask.shape
    for i in range(0, row):
        for j in range(0, col):
            imageSum = maskSum = 0
            for a in range(int(-rowMask/2), int(rowMask-rowMask/2)):
                for b in range(int(-colMask/2), int(colMask-colMask/2)):
                    if((1+a)>=0 and (j+b)>=0):
                        imageSum += img[i+a, j+b] * mask[a+int(rowMask)//2, b+int(colMask)//2]
                        maskSum += mask[a+int(rowMask)//2, b+int(colMask)//2]
            intensitas = imageSum/maskSum
            if(intensitas > 255):
                intensitas = 255
            elif(intensitas < 0):
                intensitas = 0
            kanvas.itemset((i, j, 0), intensitas)
    return kanvas