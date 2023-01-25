import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')

# Paint all image a color
# blank[200:300, 300:400] = 0,255,0

# Draw a rectangle
cv.rectangle(blank, (0, 0), (blank.shape[0] // 2, blank.shape[1] // 2), (50, 100, 0), thickness=cv.FILLED)
cv.circle(blank, (blank.shape[0] // 2, blank.shape[1] // 2), 50, (100, 0, 100), thickness=-1)
cv.line(blank, (0, 0), (250, 250), (255, 255, 255), thickness=3)
cv.putText(blank, 'Hello', (225, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), thickness=2)
cv.imshow('Draw', blank)

cv.waitKey(0)