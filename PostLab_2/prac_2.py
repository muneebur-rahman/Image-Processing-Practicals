import cv2
# Read the image
image = cv2.imread('bird2.jpg')
# Check if image is loaded properly
if image is None:
    print("Error: Image not found or unable to load.")
else:
    # Split the image into B, G, R channels
    B, G, R = cv2.split(image)
    # Show the original image and wait for a key press
    cv2.imshow("Original CS25D010", image)
    cv2.waitKey(0)
    # Show blue channel
    cv2.imshow("Blue CS25D010", B)
    cv2.waitKey(0)
    # Show green channel
    cv2.imshow("Green CS25D010", G)
    cv2.waitKey(0)
    # Show red channel
    cv2.imshow("Red CS25D010", R)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
