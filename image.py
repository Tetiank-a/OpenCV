import cv2 as cv
import numpy as np

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    new_size = (width, height)
    return cv.resize(frame, new_size, interpolation=cv.INTER_AREA)

img = cv.imread('Photos/fox.jfif')
img = rescaleFrame(img, 0.3)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)

canny = cv.Canny(blur, 125, 175)

# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found')

blank = np.zeros(img.shape)

cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow('Blank', blank)

cv.waitKey(0)