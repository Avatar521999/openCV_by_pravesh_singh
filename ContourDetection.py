import cv2 as cv
import numpy as np


path = r'C:\Users\DELL\Downloads\photos_openCV\Photos\cats.jpg'
img = cv.imread(path)
cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank Image', blank)


# Discuss -> how to identify Contour?
# Contour is boundaries of objects
# contour is useful tool -> shape Analysis, object Detection and recognition

# convert to gray image
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# Blur the image
# blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# detect edge using canny edge detection
# canny = cv.Canny(img, 125, 175)
# canny = cv.Canny(blur, 125, 175)
# 125 and 175 are threshold values
# cv.imshow("Canny Edges", canny)


# can use another function instead on canny, which is threshold function
# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('Thresh image', thresh)
# 125 -> threshold value
# 255 -> maximum value
# threshold try to binaries images
# if a particular pixel density is below 125 it is set to '0'(black) if it is above 125 it is set to '1'(white)
# cv.THRESH_BINARY is type means binaries the image


# find contour using findContours() method
# this method returns two values , ->contours  and  ->hierarchies

# contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# findContours() method looks at the structuring element or the edge found in the image and returns 2 values
# first value is "contours" -> a python list of all the coordinates of the contour found in the image
# "hierarchies" -> hierarchical representation of contours
# example -> have rectangle, inside rectangle have square, and inside square have circle.

# cv.RETR_LIST is a mode in which findContour() method returns and find the contour
# second parameter is mode, which find the contour
# it can be
# -> cv.RETR_TREE --> if want hierarchical contours, present in hierarchical manner
# -> cv.RETR_EXTERNAL --> if want external contours
# -> cv.RETR_LIST --> if want all the contours

# third parameter is contour approximation method --> cv.CHAIN.APPROX_NONE
# this is basically how we want to approximate the contour
# cv.CHAIN.APPROX_NONE , does nothing, just return all the contours
# cv.CHAIN.APPROX_SIMPLE --> compress all the contour that are returned, in the simple one that make sense.
# example -> if line in an image if, use CHAIN_APPROX_NONE -> get all the contour, all coordinates of the points
# of the line if, use CHAIN_APPROX_SIMPLE -> takes all the points of that line compress it into 2 end points only.

# print(f"{len(contours)} contour's found!") # because contours is a list so, we can find its length.

# we can visualize the contours that is found in the images by essentially drawing over the image
# cv.drawContours(blank, contours, -1, (0, 0, 255), thickness=1)
# 2nd parameter contours list
# 3rd parameter is contour index -> how many contours we want in the image   # -1 --> all contours
# cv.imshow('Contours Drawn', blank)


# two method to find contour
# 1. find the edge cascade of the image using canny edge detector and find contour using that.
# 2. try to binaries the image using cv.threshold() method and find contour using that.


cv.waitKey(0)