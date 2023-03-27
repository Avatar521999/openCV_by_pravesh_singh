import cv2 as cv
import numpy as np

path = r'C:\Users\DELL\Downloads\photos_openCV\Photos\park.jpg'
img = cv.imread(path)
cv.imshow('Cats', img)

# -- An image gradient is a directional change in the intensity or color in an image. --

# edge detection method:
# 1. Laplacian
# 2. Sobel

gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow('GRAY', gray)

# 1. Laplacian edge detection
# Laplacian method compute gradient of the grayscale image.
# involves mathematics --> when transition from black to white and white to black that consider
# positive and negative slope, images itself cannot have negative pixel values, we do is we compute
# the absolute values of that image, so all the pixel values of the image are converted to the absolute values,
# and then we convert that to 'uint8' -> an image specific datatype.

lap =cv.Laplacian(gray, cv.CV_64F)
# 1st parameter -> source image
# 2nd parameter -> (ddepth) data depth
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian Edge', lap)
# look like as -> drawn with pencil and lighty smudge


# 2. Sobel gradient magnitude representation
# sobel compute gradient in two direction X and Y
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
cv.imshow('Sobel X', sobelx)
# 2nd parameter -> data depth
# 3nd parameter -> x direction
# 4th parameter -> y direction
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
cv.imshow('Sobel Y', sobely)

# combine sobelx and sobely
combined_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('Combined Sobel', combined_sobel)


# Compare with canny edge detection
canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)


# Notes-
# 'Canny' is advance edge detection algorithm and most use, it provides cleaner edges.
# In advance cases 'sobel' is used.


cv.waitKey(0)