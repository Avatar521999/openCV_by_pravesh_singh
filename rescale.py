import cv2 as cv

#display images

path = r'C:\Users\DELL\Downloads\photos_openCV\Photos\cat.jpg'
img = cv.imread(path)

cv.imshow('Cat', img)

def rescaleFrame(frame, scale = 0.65):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


resized_image = rescaleFrame(img)
cv.imshow('image', resized_image)

# Reading videos
path = r'C:\Users\DELL\Downloads\photos_openCV\videos\dog.mp4'
capture = cv.VideoCapture(path)

def changeRes(width, height):
    # for live videos
    capture.set(3, width)
    capture.set(4, height)

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('video', frame)
    cv.imshow('Video Resized ', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()


cv.waitKey(0)   # 0->infinite wait