# 6. Removing noise from images

#Import the necessary libraries
import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('img1.jpg')
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(image)
filtered_image = cv2.medianBlur(image, 11)
cv2.imwrite('Median Blur.jpg', filtered_image)
plt.subplot(1, 2, 2)
plt.title("Median Blur CS25D010")
plt.imshow(filtered_image)
plt.show()