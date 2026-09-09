# 7. Histogram equalization

import cv2
import numpy as np
img = cv2.imread('img1.jpg', 0)
equ = cv2.equalizeHist(img)
res = np.hstack((img, equ))
cv2.imshow('CS25D010', res)
cv2.waitKey(0)
cv2.destroyAllWindows()