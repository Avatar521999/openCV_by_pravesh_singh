import cv2 as cv
import matplotlib.pyplot as plt


path = r'C:\Users\DELL\Downloads\photos_openCV\Photos\park.jpg'
img = cv.imread(path)
cv.imshow('Boston', img)

# opencv display as BGR images
# matplotlib display as RGB images
# plt.imshow(img)
# plt.show()


# convert BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.color_BGR2GRAY is colour code
cv.imshow("Gray Image", gray)
# grayscale show the distribution of pixel intensity


# convert BGR to HSV
# HSV --> Hue Saturation value
# Based on how human think and conceive colours
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV Image', hsv)


# convert BGR to LAB (L*A*B)
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB Image', lab)

# way to convert BGR to RGB images
# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB Image', rgb)

# plt.imshow(rgb)
# plt.show()

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('hsv_bgr Image', hsv_bgr)

# LAB to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('lab_bgr Image', lab_bgr)




cv.waitKey(0)