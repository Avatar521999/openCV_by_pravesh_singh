import cv2 as cv
import numpy as np


path = r'C:\Users\DELL\Downloads\photos_openCV\Photos\park.jpg'
img = cv.imread(path)
cv.imshow('Boston', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
# img.shape[:2] --> means passing height and width not colour channel only passing 2 values
# img.shape --> (427, 640, 3) --> shape have three values

# split an image into its respective colour channels.
# take BGR image and split it into blue, green, red components.

b, g, r = cv.split(img)

# Display blue channel image
blue = cv.merge([b, blank, blank])
cv.imshow('Blue', blue)
# Display green channel image
green = cv.merge([blank, g, blank])
cv.imshow('Green', green)
# Display red channel image
red= cv.merge([blank, blank, r])
cv.imshow('Red', red)


# blue colour channel
# cv.imshow('Blue', b)

# green colour channel
# cv.imshow('Green', g)

# red colour channel
# cv.imshow('Red', r)

# above, shows the distribution of pixel intensities
# region --> lighter --> far more concentration of those pixels value
# region --> darker --> little or no pixel in that region

# visualise shape & dimensions of the image
print(img.shape)   # have 3 color channel
# below shape of these images is gray scale images
print(b.shape)   # has single color channel
print(g.shape)   # has single color channel
print(r.shape)    # has single color channel

# merge b, r, g
merged = cv.merge([b, g, r])
cv.imshow("Merged Image", merged)


# way to see actual colour channel involved in the gray scale image
# example --> for blue colour channel, get blue image
# way to do --> reconstruct the image
# create blank image



cv.waitKey(0)