import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('blackWhiteGradient.jpg')
print(img.shape)

ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)


plt.subplot(231)
plt.imshow(img)
plt.title('original')

plt.subplot(232)
plt.imshow(thresh1)
plt.title('binary')

plt.subplot(233)
plt.imshow(thresh2)
plt.title('binary inversion')

plt.subplot(234)
plt.imshow(thresh3)
plt.title('truncate')

plt.subplot(235)
plt.imshow(thresh4)
plt.title('to zero')

plt.subplot(236)
plt.imshow(thresh5)
plt.title('to zero inv')

plt.show()
