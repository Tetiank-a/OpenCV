import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# Reading images
img = cv.imread('Photos/2.jpg')
named_window = 'Kharkiv'
cv.namedWindow(named_window)
cv.moveWindow(named_window, 100, 100)
cv.imshow(named_window, rescaleFrame(img, 3.0))

cv.waitKey(0)
cv.destroyAllWindows()