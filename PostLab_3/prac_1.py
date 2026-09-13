import cv2
img = cv2.imread("bird2.jpg")
t_lower = 50
t_upper = 150
edge = cv2.Canny(img, t_lower, t_upper)
cv2.imshow('original CS25D010', img)
cv2.imshow('edge CS25D010', edge)
cv2.waitKey(0)
cv2.destroyAllWindows()