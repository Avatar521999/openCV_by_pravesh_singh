import cv2 as cv
import numpy as np


path = r'C:\Users\DELL\Downloads\photos_openCV\Photos\park.jpg'
img = cv.imread(path)
cv.imshow('Original Image', img)

# transformation -> translation, rotation, resizing, clipping and cropping

# 1. Translation
# shifting an image along X and Y axis
# using translation can shift an image up, down, left, right or combination of these

# def translate(img, x, y):
# # x, y -> no of pixel want to shift along x axis and y axis
#     transMat = np.float32([[1, 0, x], [0, 1, y]])
#     dimensions = (img.shape[1], img.shape[0])  # shape[1] -> width, shape[0] -> height
#     return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
#  x --> Right
#  y --> Down

# translated = translate(img, 100, 100)  # right, down
# translated = translate(img, -100, 100)   # left, down
# cv.imshow('Translated Image', translated)

# 2. Rotation
# rotating an image by an angle
# def rotate(img, angle, rotPoint=None):
#     (height, width) = img.shape[:2]
#
#     if rotPoint is None:
#         rotPoint = (width // 2, height // 2)
#
#     rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)   # 1.0 is default scale value
#     dimensions = (width, height)
#
#     return cv.warpAffine(img, rotMat, dimensions)   # destination is dimensions

# rotated = rotate(img, 45)
# rotate image anticlock wise by 45 degree
# rotated = rotate(img, -45)
# rotate image clockwise by 45 degree
# cv.imshow('Rotated', rotated)

# rotated_rotated = rotate(rotated, -45)
#rotate rotated image
# cv.imshow('Rotated Rotated', rotated_rotated)

# rotated = rotate(img, -90)
# rotate image clockwise by 90 degree
# cv.imshow('Rotated', rotated)

# 4. Resize
# resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
# cv.imshow('RESIZE', resized)

# 5. Flipping an image
# flip = cv.flip(img,0)
# flip = cv.flip(img,1)
# flip = cv.flip(img,-1)
# cv.imshow('Flip the image', flip)

# 0 -> flip vertically
# 1 -> flip horizontally
# -1 -> flip both vertically and horizontally


# 6. Cropping
# cropped = img[200:400, 300:400]  #array slicing
# cv.imshow('Cropped', cropped)


cv.waitKey(0)