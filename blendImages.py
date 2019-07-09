import cv2

e1 = cv2.getTickCount()
lion = cv2.imread('lion.jpg', 1)
cv2.imshow('lion', lion)

# deer = cv2.imread('deer.jpg', 1)
# print(deer.shape)

# img = cv2.add(lion, deer)
# cv2.imshow('image', img)

# img2 = cv2.addWeighted(lion, 0.9, deer, 0.1, 0)
# cv2.imshow('image1', img2)


# part = lion[140:540, 800:1300]
# cv2.imshow('part', part)

# lion[501:901, 800:1300] = part
# cv2.imshow('lion1', lion)

b, g, r = cv2.split(lion)
lion[:, :, 2] = 255
cv2.imshow('liongreen', lion)
e2 = cv2.getTickCount()
print((e2 - e1) / cv2.getTickFrequency())

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
