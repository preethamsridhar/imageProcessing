import cv2

lion = cv2.imread('lion.jpg', 1)
print(lion.shape)

deer = cv2.imread('deer.jpg', 1)
print(deer.shape)

img = cv2.add(lion, deer)
cv2.imshow('image', img)

img2 = cv2.addWeighted(lion, 0.9, deer, 0.1, 0)
cv2.imshow('image1', img2)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
