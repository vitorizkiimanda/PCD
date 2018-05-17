import numpy as np
import cv2
import vri_pcd as vri

import glob
import os,sys

## Get all the png image in the PATH_TO_IMAGES
imgnames = sorted(glob.glob("penampakkan/19/*.jpg"))
urutan = 1
folder = 19
for imgname in imgnames:
    img = cv2.imread(imgname)
    # print(imgname)

    # cetak foto
    namaFoto = 'penampakkan/%d\%d_%d.jpg' % (folder, folder,urutan);
    cv2.imwrite(namaFoto, img)
    print(namaFoto)
    urutan = urutan+1

cv2.waitKey(0)
cv2.destroyAllWindows()
