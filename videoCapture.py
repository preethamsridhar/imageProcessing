import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# green = np.uint8([[[0, 127, 0]]])
# red = np.uint8([[[127, 0, 0]]])
# blue = np.uint8([[[0, 0, 127]]])

# print("green: ", cv2.cvtColor(green, cv2.COLOR_BGR2HSV))
# print("red: ", cv2.cvtColor(red, cv2.COLOR_BGR2HSV))
# print("blue: ", cv2.cvtColor(blue, cv2.COLOR_BGR2HSV))

green_lower = [130, 50, 100]
red_lower = [0, 50, 100]
blue_lower = [230, 50, 100]

green_upper = [110, 100, 100]
red_upper = [10, 100, 100]
blue_upper = [250, 100, 100]


while 1:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array(blue_lower)
    upper_blue = np.array(blue_upper)

    # define range of red color in HSV
    lower_red = np.array(red_lower)
    upper_red = np.array(red_upper)

    # Threshold the HSV image to get only blue colors
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_red = cv2.inRange(hsv, lower_red, upper_red)

    # Bitwise-AND mask and original image
    res_blue = cv2.bitwise_and(frame, frame, mask=mask_blue)
    res_red = cv2.bitwise_and(frame, frame, mask=mask_red)

    cv2.imshow('frame', frame)
    cv2.imshow('hsv', hsv)
    cv2.imshow('mask_blue', mask_blue)
    cv2.imshow('res_blue', res_blue)
    cv2.imshow('mask_red', mask_red)
    cv2.imshow('res_red', res_red)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
