# 3. Adjusting brightness and contrast (Method 2)

import cv2
import matplotlib.pyplot as plt
import numpy as np
image = cv2.imread('img1.jpg')
#Plot the original image
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(image)
alpha = 1.5
beta = 50
image2 = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
cv2.imwrite('Brightness & contrast.jpg', image2)
plt.subplot(1, 2, 2)
plt.title("Brightness & contrast CS25D010")
plt.imshow(image2)
plt.show()