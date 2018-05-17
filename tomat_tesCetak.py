import numpy as np
import cv2
import vri_pcd as vri

import glob
import os,sys

final = cv2.imread("tomatku.jpg")

cv2.imwrite(str(final)+"aw.jpg", final);
print(str(final))
cv2.waitKey(0)
cv2.destroyAllWindows()
