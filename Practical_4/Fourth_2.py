# 2. Adjusting brightness and contrast (Method 1)

import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('img1.jpg')
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(image)
brightness = 10
contrast = 2.3
image2 = cv2.addWeighted(image, contrast, np.zeros(image.shape, image.dtype), 0, brightness)
cv2.imwrite('modified_image.jpg', image2)
plt.subplot(1, 2, 2)
plt.title("Brightness & contrast CS25D010")
plt.imshow(image2)
plt.show()