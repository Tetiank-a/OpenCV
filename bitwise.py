import cv2 as cv
import numpy as np

def resizeFrame(frame, scale=0.3):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimentions = (width, height)
    return cv.resize(frame, dimentions, interpolation=cv.INTER_AREA)

# Read and resize image
img = cv.imread('Photos/fox.jfif')
img = resizeFrame(img)

img_gray = cv.cvtColor(img, cv.COLOR_BGR2HSV)

blank = np.zeros(img.shape[:2], dtype='uint8')

mask_1 = blank.copy()
cv.circle(mask_1, (img.shape[1] // 2, img.shape[0] // 2 - 50), 100, (255, 255, 255), -1)

mask_2 = cv.bitwise_not(mask_1)

masking1 = cv.bitwise_and(img, img, mask=mask_2)
cv.imshow('Masking 1', masking1)

masking2 = cv.bitwise_and(img_gray, img_gray, mask=mask_1)
cv.imshow('Masking 2', masking2)

final_res = masking1 + masking2
cv.imshow('Final', final_res)

cv.waitKey(0)