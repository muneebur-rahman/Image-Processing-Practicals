    import cv2
    import numpy as np
    from scipy.cluster.hierarchy import weighted

    img1=cv2.imread("mango.jpg")
    img2=cv2.imread("tomato1.jpg")
    img_xor=cv2.bitwise_xor(img2,img1,mask=None)
    cv2.imshow("CS25D010",img_xor)
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()