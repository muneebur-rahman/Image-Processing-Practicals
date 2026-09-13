# Gray Color
import cv2
# Read image directly in grayscale mode
img = cv2.imread('bird2.jpg', cv2.IMREAD_GRAYSCALE)
# Check if the image was loaded properly
if img is None:
 print("Error: Image not found or unable to load.")
else:
 # Show the grayscale image
 cv2.imshow('CS25D010', img)
 cv2.waitKey(0)