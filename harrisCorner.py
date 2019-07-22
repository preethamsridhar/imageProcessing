import cv2
import numpy as np

filename = 'sudokuPaper.jpeg'
img = cv2.imread(filename)
# th2 = cv2.adaptiveThreshold(
#     img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

# result is dilated for marking the corners, not important
dst = cv2.dilate(dst, None)

# Threshold for an optimal value, it may vary depending on the image.
img[dst > 0.01 * dst.max()] = [255, 0, 0]

# cv2.imshow('dst', img)
cv2.imwrite('harriscorner.jpeg', img)

# if cv2.waitKey(0) & 0xff == 27:
#     cv2.destroyAllWindows()
