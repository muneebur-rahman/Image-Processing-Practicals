import cv2
img = cv2.imread("tomato.jpg", cv2.IMREAD_COLOR)
cv2.imshow("CS25D010",img)
cv2.waitKey(0)
cv2.destroyAllWindows()