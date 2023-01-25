import cv2 as cv
import numpy as np

def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimentions = (width, height)
    return cv.resize(frame, dimentions, interpolation=cv.INTER_AREA)

img = cv.imread('Photos/fox.jfif')
img = rescaleFrame(img, 0.3)

b, g, r = cv.split(img)

blank = np.zeros(img.shape[:2], dtype='uint8')
blue = cv.merge([b, blank, blank])

cv.imshow('blue', blue)

cv.waitKey(0)