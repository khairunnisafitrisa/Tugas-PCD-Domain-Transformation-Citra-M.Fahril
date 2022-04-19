# Mengimpor Library yang diperlukan
import numpy as np
import pandas as pd
import cv2

# Membaca Gambar
img_root='images'
img_name='fahril.jpg'
img = cv2.imread(img_name,cv2.IMREAD_UNCHANGED)

# Program Filter Mean
kernel = np.ones((10,10),np.float32)/25
meanFilter = cv2.filter2D(img,-1,kernel)

# Menampilkan Output
cv2.imshow("Mean Filtered Image",np.hstack((img, meanFilter)))
cv2.waitKey(0)
cv2.destroyAllWindows()

