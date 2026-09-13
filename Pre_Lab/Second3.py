import cv2
path = r'mango.jpg'
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
cv2.imshow("CS25D010", img)
cv2.waitKey(0)
cv2.destroyAllWindows()