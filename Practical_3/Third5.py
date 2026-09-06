import numpy as np

import cv2 as cv
img = cv.imread('img1.jpg', 0)
cropped_img = img[100:300, 100:300]
cv.imshow("CS25D010", cropped_img)
cv.waitKey(0)
cv.destroyAllWindows()