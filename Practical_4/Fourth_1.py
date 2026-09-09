# 1. Negative Image

import cv2
import numpy as np

img = cv2.imread('img1.jpg', 0)
negative = 255 - img
combined = np.hstack((img, negative))
cv2.imshow('CS25D010', combined)
cv2.waitKey(0)
cv2.destroyAllWindows()