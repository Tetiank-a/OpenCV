import cv2 as cv
import numpy as np
import modification

img = cv.imread('Photos/fox.jfif')
img = modification.rescaleFrame(img, 0.3)
img_pix = modification.rescaleFrame(img, 0.1)
img_pix = modification.rescaleFrame(img_pix, 10.0)

blank = np.zeros(img.shape[:2], dtype='uint8')
mask1 = blank.copy()
cv.circle(mask1, (mask1.shape[1] // 2, mask1.shape[0] // 2 - 50), 100, (255, 255, 255), -1)
mask2 = cv.bitwise_not(mask1)

face = cv.bitwise_and(img_pix, img_pix, mask=mask1)
body = cv.bitwise_and(img, img, mask=mask2)
total = face + body

cv.imshow('Result', total)

cv.waitKey(0)