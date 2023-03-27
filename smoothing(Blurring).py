import cv2 as cv

path = r'C:\Users\DELL\Downloads\photos_openCV\Photos\women.png'
img = cv.imread(path)
cv.imshow('Cats', img)

# we smooth an image when it, have a lot of noise.
# kernel or window --> window has a size known as kernel size.
# kernel size --> number of rows and no of columns
# something happens to middle pixel due to surrounding pixel.


# 1. Averaging Blurring technique
# we define a kernel window over a specific portion of an image and this window will compute the pixel
# intensity of the middle pixel of the true center as the average of the surrounding pixel intensities.
# this process happens throughout the image.
average = cv.blur(img, (3,3))
cv.imshow('Average Blur Image', average)
# higher the kernel size --> higher the blur


# 2. Gaussian Blur technique
# does same thing as averaging except that instead computing average of all surrounding pixel intensity
# each surrounding pixel is given a particular weight and the average of the product of surrounding weights
# gives the value for true center.
# using this method --> get less blur as compared to averaging blur method.
# Gaussian blur is more natural as compared to averaging blur method.
gauss = cv.GaussianBlur(img, (3, 3), 0)
# third parameter is -> sigmaX -> standard deviation in the x direction.
cv.imshow('Gaussian Blur', gauss)


# 3. Median Blur technique
# median blurring is same thing as averaging except that instead of finding the average of the surrounding
# pixels, it finds the median of the surrounding pixel.
# more effective in reducing noise in an image as compared to Averaging and Gaussian blur.
# very good, in removing "salt & pepper" noise.
median = cv.medianBlur(img, 3)
# kernel size (second parameter) will be --> integer value.
# because automatically assume it will be 3 by 3 (kernel size).
cv.imshow("Median Blur", median)
# is not meant for higher kernel size 5 or 7


# 4. Bilateral Blur technique
# most effective blurring technique.
# bilateral apply blurring but retains the edges in the image.
bilateral = cv.bilateralFilter(img, 10, 30, 20)
# 2nd parameter -> diameter of the pixel neighbour
# 3rd parameter -> sigma color, means there are more colours in the neighbour
# 4th parameter -> sigma space, larger values of this space sigma, means that pixels further out from the
# center of pixel, will influence the blurring calculation.
# ( keep value low or will look like a smudge image similar to median blurring )
cv.imshow('Bilateral Blur', bilateral)


















cv.waitKey(0)