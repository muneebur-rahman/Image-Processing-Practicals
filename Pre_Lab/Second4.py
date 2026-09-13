import cv2
import numpy as np
from scipy.cluster.hierarchy import weighted

img1=cv2.imread("mango.jpg")
img2=cv2.imread("tomato1.jpg")
weightedSum=cv2.addWeighted(img1,0.5,img2,0.4,0)
cv2.imshow("CS25D010",weightedSum)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()