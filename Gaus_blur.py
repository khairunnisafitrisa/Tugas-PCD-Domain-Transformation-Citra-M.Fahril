# Import library yang diperlukan
import numpy as np
import pandas as pd
import cv2

# Program Membaca Gambar
img_root='images'
img_name='Nisfit2.jpg'
img = cv2.imread(img_name,cv2.IMREAD_UNCHANGED)

# Program Gaussian Blur
gaussBlur = cv2.GaussianBlur(img,(5,5),cv2.BORDER_DEFAULT)

# Program Output
cv2.imshow("Gaussian Smoothing",np.hstack((img,gaussBlur)))
cv2.waitKey(0)
cv2.destroyAllWindows()


