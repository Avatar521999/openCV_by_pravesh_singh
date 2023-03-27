import cv2 as cv

path = r'D:\From Downloads\photos_openCV\Photos\park.jpg'
img = cv.imread(path)
cv.imshow('Boston', img)

# 1. converting an image to greyScale
# why convert -> to see intensity of pixel not colours(BGR)
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray image', gray)

# 2. blur the image
# why blur -> removes some of the noise from the image
# blur -> Gaussian blur
# blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
# kernel size is a tuple { above -> (3, 3) },should be odd number
# blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
# increase kernel size to increase blur -> (7, 7)
# cv.imshow('Blur Image', blur)

# 3. Edge Cascade
# find edges present in the image
# using ->  Canny edge detector
# there are multiple steps
canny = cv.Canny(img, 125, 175)
# 125, 175 -> threshold values
# canny = cv.Canny(blur, 125, 175)
# reduce edge by sending blur image
# cv.imshow('Canny Edge', canny)

# 4. Dilating the image
# dilate an image using a specific structuring element
# structuring element -> edges
dilated = cv.dilate(canny, (7, 7), iterations=2)
cv.imshow('Dilated Image', dilated)
# making edge more visible (adding more pixel to en edge)

# 5. Eroding the image
# eroding dilated image to normal
# eroded = cv.erode(dilated, (7, 7), iterations=2)
# cv.imshow('Eroded Image', eroded)

# 6. Resize an image
# resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
# change the size to (500, 500) of original image , ignoring the aspect ratio
# INTER_AREA is useful -> shrinking the image dimension then original dimensions
# INTER_LINEAR and INTER_CUBIC is useful -> enlarge the image dimension then original dimensions
# INTER_CUBIC is slowest, result is higher quality
# cv.imshow('Resize Image', resized)

# 7. Cropping an image
# using the fact -> images are array and can use -> array slicing
# Select a portion of the image on the basic of their pixel values
# cropped = img[50:200, 200:400]
# 50:200 means -> from 50 to 200
# select the region 50:200 is width and 200:400 is height
# cv.imshow('Cropped', cropped)

cv.waitKey(0)