import cv2 as cv
import numpy as np

# bitWise operator in openCV
blank = np.zeros((400, 400), dtype='uint8')

# 4 bitwise operator -
# AND
# OR
# XOR
# NOT

# a pixel is turned off -> 0
# a pixel is turned on -> 1

# use blank to draw
rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, thickness=-1)
# 4th parameter is colour -> 230 -> single value because, this is not a colour image rather a binary image
cv.imshow('Rectangle', rectangle)

circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)
# last parameter is thickness which is -1
# 2nd parameter is center ( another way to find center is -> (blank.shape[1]//2, blank.shape[0]//2) ).
# 3rd parameter is radius which is 200.
cv.imshow("Circle", circle)


# 1. bitwise AND
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND', bitwise_and)
# bitwise AND return intersection of two image
# uncommon region -> set to 0 (black)
# common region returned


# 2. bitwise OR
# return both intersecting and non-intersecting regions.
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR', bitwise_or)


# 3. bitwise XOR
# return non-intersecting regions.
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('bitwise_xor', bitwise_xor)


# 4. bitwise NOT
# does not return anything.
# invert the binary colour.
# bitwise_not = cv.bitwise_not(rectangle)
bitwise_not = cv.bitwise_not(circle)
cv.imshow('Bitwise NOT', bitwise_not)













cv.waitKey(0)