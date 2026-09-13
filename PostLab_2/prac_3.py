# Python program to read image
# as YCrCb color space
# Import cv2 module
import cv2
# Reads the image
img = cv2.imread('bird2.jpg')
# Convert to YCrCb color space
img = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
# Shows the image
cv2.imshow('CS25D010', img)
cv2.waitKey(0)
cv2.destroyAllWindows()