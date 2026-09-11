# 3. Median Filter
import cv2
import numpy
# using imread()
img = cv2.imread("img1.jpg")
dst = cv2.medianBlur(img, 5)

cv2.imshow('CS25D010', numpy.hstack((img, dst)))
cv2.waitKey(0);
cv2.destroyAllWindows();
cv2.waitKey(1)