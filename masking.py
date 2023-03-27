import cv2 as cv
import numpy as np

path = r'C:\Users\DELL\Downloads\photos_openCV\Photos\cats 2.jpg'
img = cv.imread(path)
cv.imshow('Cats', img)

# masking allows us to focus on certain part of an image that we like to focus on.

blank = np.zeros(img.shape[:2], dtype='uint8')
# dimension of mask have to be the same as that of the image.
cv.imshow('Blank', blank)

# mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, thickness=-1)
# mask = cv.rectangle(blank, ((img.shape[1]//2)//2, (img.shape[0]//2)//2), (300, 300), 255, -1)
# cv.imshow('Mask', mask)

# masked = cv.bitwise_and(img, img, mask=mask)
# cv.imshow('Masked Image', masked)

circle = cv.circle(blank.copy(), (img.shape[1]//2 + 45, img.shape[0]//2), 100, 255, thickness=-1)
cv.imshow('Circle', circle)
rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
cv.imshow('Rectangle', rectangle)

weired_shape = cv.bitwise_and(circle, rectangle)
cv.imshow('Weired Shape', weired_shape)

masked = cv.bitwise_and(img, img, mask=weired_shape)
cv.imshow('Weired Shape Masked Image', masked)


cv.waitKey(0)