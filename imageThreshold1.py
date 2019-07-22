import cv2
import numpy as np
from matplotlib import pyplot as plt

img_ = cv2.imread('sudokuPaper.jpeg', 0)
img = cv2.medianBlur(img_, 5)

# cv2.imshow('img', img)
# cv2.imshow('img_', img_)

ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
th3 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

titles = ['Original image', 'Global threshold (v=127)', 'Adaptive Mean threshold',
          'Adaptive Gaussian', 'Adaptive Gaussian Threshold']

images = [img, th1, th2, th3]

# for i in range(4):
#     plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
#     plt.title(titles[i])
#     plt.xticks([]), plt.yticks([])
# plt.show()

img = cv2.imread('sudokuPaper.jpeg')
gray = np.float32(cv2.cvtColor(cv2.imread('sudokuPaper.jpeg'), cv2.COLOR_BGR2GRAY))

th3_corner = cv2.cornerHarris(img, 2, 3, 0.04)
th3_corner = cv2.dilate(th3_corner, None)

img[th3_corner > 0.01 * th3_corner.max()] = [0, 0, 255]

cv2.imshow('th3', th3_corner)

cv2.waitKey(0)
cv2.destroyAllWindows()
