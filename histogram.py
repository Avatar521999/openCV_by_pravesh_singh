import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


path = r'C:\Users\DELL\Downloads\photos_openCV\Photos\Cats.jpg'
img = cv.imread(path)
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

# Histogram allow us to visualize the distribution of pixel intensities in an image.

# 1. Computing histogram for grayscale images.

# convert to gray image:
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray Image', gray)

# circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
# cv.imshow('Circle', circle)

# mask = cv.bitwise_and(gray, gray, mask=circle)
# cv.imshow('Mask', mask)


# grayscale histogram:
# gray_his = cv.calcHist([gray], [0], None, [256], [0, 256])
# gray_his = cv.calcHist([gray], [0], mask, [256], [0, 256])
# 1st parameter --> is image parameter will pass -> list of images.
# 2nd parameter --> number of channels -> specify the index of the channel, want to compute a histogram for.
# 2nd parameter --> is zero, because image is gray scale image.
# 3rd parameter --> is mask -> if we want to computer a histogram for portion of an image.
# 4th parameter --> is number of bins that we want to use for computing the histogram.
# bins represent the interval of pixel intensities.
# 5th parameter --> range of all possible pixel value.
# example --> in this image there are close to 4000 pixel have an intensity of 60.


# we can also do this, create a mask and then compute the histogram only on that particular mask.

# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_his)
# plt.xlim([0, 256])   # limit across x axis
# plt.show()


# 2. Computing histogram for colour images.

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked', masked)

# mask need to be in binary format.

plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')

colors = ('b', 'g', 'r')

for i, col in enumerate(colors):
    # hist = cv.calcHist([img], [i], None, [256], [0, 256])
    hist = cv.calcHist([img], [i], mask, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.show()











cv.waitKey(0)