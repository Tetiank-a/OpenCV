import cv2 as cv

# Reading images
# img = cv.imread('Photos/17.jpg')
# cv.imshow('Khariv', img)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Reading videos
capture = cv.VideoCapture('Videos/1.mkv')

while True:
    isTrue, frame = capture.read()
    
    if isTrue:
        frame_resized = rescaleFrame(frame, 0.5)
        cv.imshow('Video', frame)
        cv.imshow('Video resized', frame_resized)

        # Close if Q is pressed
        if cv.waitKey(25) & 0xFF == ord('q'):
          break
    else:
        break


# Close all windows
capture.release()
cv.destroyAllWindows()