import cv2 as cv
import numpy as np

blank = np.zeros((500, 500 , 3), dtype='uint8')  # uint8 is datatype of image   # 3 -> no of colour channel
cv.imshow('blankImage', blank)

# path = r'C:\Users\DELL\Downloads\photos_openCV\Photos\cat.jpg'
# img = cv.imread(path)
# cv.imshow('catImage', img)

# 1.paint the image a certain colour
# blank[:] = 0,255,0   # : -> all reference all the pixels
# blank[200:300, 300:400] = 255,0,0  # providing set of area
# cv.imshow('Green', blank)

# 2.draw a rectangle
cv.rectangle(blank, (50, 50), (300, 200), (0, 0, 255), thickness=2)  # thickness of border is 2
# cv.rectangle(blank, (50, 50), (300, 200), (0, 0, 255), thickness=cv.FILLED)  # thickness -> filled with red
# cv.rectangle(blank, (50, 50), (300, 200), (0, 0, 255), thickness=-1)  # thickness -1 gives same result as cv.FILLED
cv.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (0, 250, 255), thickness=-1)
# thickness of -1 means filled  # has dimensions half of original image
cv.imshow('rectange', blank)

# 3.draw a circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 100, (0, 0, 255), thickness=3)
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 100, (0, 0, 255), thickness=-1)
# (blank.shape[1]//2, blank.shape[0]//2) -> gives center of original image , half of width , half of height
cv.imshow("Circle", blank)

# 4.draw a line
cv.line(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (200, 240, 200), thickness=3)
cv.imshow('Line', blank)

# 5. Write Text on a image
cv.putText(blank, 'HELLO', (200, 260), cv.FONT_HERSHEY_TRIPLEX, 2.0, (0, 255, 90), thickness=2)
# cv.FONT_HERSHEY_TRIPLEX is cv inbuit font  # 1.0 is default font scale
# cv.putText(blank, 'my name is pravesh', (0, 260), cv.FONT_HERSHEY_TRIPLEX, 1.0, (50, 255, 90), thickness=2)
cv.imshow('HELLO TEXT', blank)

cv.waitKey(0)