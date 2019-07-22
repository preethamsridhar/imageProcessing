import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("sudoku.png")
cv2.imshow('sudoku', img)

rows, cols, ch = img.shape
print(rows, cols)
# shift image
# M = np.float32([[1, 0, 100], [0, 1, 50]])
# dst = cv2.warpAffine(lion, M, (cols, rows))
# cv2.imshow('dst', dst)

# rotate image
# M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)
# dst = cv2.warpAffine(lion, M, (cols, rows))
# cv2.imshow('dst', dst)

# Affine transformation
# pts1 = np.float32([
#     [50, 50],
#     [200, 50],
#     [50, 200]
# ])
# pts2 = np.float32([
#     [10, 100],
#     [200, 50],
#     [100, 250]
# ])

# M = cv2.getAffineTransform(pts1, pts2)
# dst = cv2.warpAffine(img, M, (cols, rows))

# plt.subplot(121), plt.imshow(img), plt.title('Input')
# plt.subplot(122), plt.imshow(dst), plt.title('Output')
# plt.show()

# perspective transformation
pts1 = np.float32([
    [30, 30],
    [270, 30],
    [30, 270],
    [270, 270]
])

pts2 = np.float32([
    [0, 0],
    [300, 0],
    [0, 300],
    [300, 300]
])

M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img, M, (300, 300))

# plt.subplot(121), plt.imshow(img), plt.title('Input')
# plt.subplot(122), plt.imshow(dst), plt.title('Output')
# plt.show()
cv2.imshow('dst', dst)

# if cv2.waitKey(10000) & 0xFF == 27:
#     cv2.destroyAllWindows()

cv2.waitKey(0)
cv2.destroyAllWindows()
