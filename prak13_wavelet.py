#import pywt
import numpy as np

im = np.array([71, 67,24,26,36,32,14,18])

#library
#coeff = pywt.dwt(im, "haar")  #Dekomposisis lv 1
#LL, (HH) = coeff
#print(LL,HH)

#manual
LL1 = list()
HH1 = list()
i = 0
rows = int(len(im)/2)
for j in range(rows):
    L = (im[i]+im[i+1])/np.sqrt(2) #lowpass
    LL1.append(L)
    H = (im[i]-im[i+1])/np.sqrt(2) #highpass
    HH1.append(H)
    i += 2

print(LL1,HH1)