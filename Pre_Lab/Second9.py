import cv2
import numpy as np
from scipy.cluster.hierarchy import weighted

img1=cv2.imread("mango.jpg")
img2=cv2.imread("tomato1.jpg")
img_not1=cv2.bitwise_not(img1,mask=None)
img_not2=cv2.bitwise_not(img2,mask=None)
cv2.imshow("CS25D010",img_not1)
cv2.imshow("CS25D010",img_not2)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()