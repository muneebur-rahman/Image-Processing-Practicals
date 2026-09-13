import cv2
img = cv2.imread("bird2.jpg")
t_lower = 100
t_upper = 200
aperture_size = 5
L2Gradient = True
edge = cv2.Canny(img, t_lower, t_upper,
 apertureSize = aperture_size,
 L2gradient = L2Gradient )
cv2.imshow('original CS25D010', img)
cv2.imshow('edge CS25D010', edge)
cv2.waitKey(0)
cv2.destroyAllWindows()