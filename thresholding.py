import cv2 as cv

path = r'C:\Users\DELL\Downloads\photos_openCV\Photos\cats.jpg'
img = cv.imread(path)
cv.imshow('Cats', img)

# thresholding is Binarizing of the image.
# in simple language, we want to take an image and convert it to a binary image, image where pixel is
# either 0 (black) or 255 (white).

# thresholding 2 type:
# 1. simple thresholding
# 2. adaptive thresholding

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GRAY', gray)

# 1. Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
# threshold, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
# return two things
# thresh --> thresholded image or binarize image
# threshold --> same, value of 2nd parameter (150) is returned to it.

# 1st parameter -> takes grayscale image
# 2nd parameter -> threshold value -> 150
# 3rd parameter -> maximum value -> if the pixel value is greater than 2nd parameter (150), what
# you want to set it to. we want to binarize the image so, set to 255.
# 4th parameter -> thresholding type -> it looks the image and compares each pixel value to the
# threshold value, and if it is above (150), it sets to 255 otherwise 0.
cv.imshow('simple threshold Image', thresh)


# inverse simple thresholded image.
# threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
# cv.imshow('simple inverted threshold Image', thresh_inv)


# 2. Adaptive Thresholding
# computer find the optimal threshold value by itself and binarize the image on that value.
# adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)

# 1st parameter -> source image.
# 2nd parameter -> maximum value.
# 3rd parameter -> take mean of neighbour pixel.
# 4th parameter -> threshold type
# 5th parameter -> Block size -> neighbourhood size of kernel size -> need to compute mean value
# for optimal threshold value. kernel size or window size -> (11 by 11).
# 6th parameter -> C value -> an integer that is subtracted from the mean, allow us to fine
# tune our threshold.
cv.imshow('Adaptive threshold Image', adaptive_thresh)

# inverse adaptive thresholded image
adaptive_thresh_invert = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 5)
cv.imshow('Adaptive inverse threshold Image', adaptive_thresh_invert)


cv.waitKey(0)