import cv2
import numpy as np
from scipy.cluster.hierarchy import weighted

img1=cv2.imread("mango.jpg")
img2=cv2.imread("tomato1.jpg")
sub=cv2.subtract(img1,img2)
cv2.imshow("CS25D010",sub)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()