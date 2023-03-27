import cv2 as cv

# face detection detect presence of a face in an image.
# face recognition involves identifying whose face it is.

# face detection is performed using a classifiers.
# two face classifiers:
# 1. Haar Cascade
# 2. Local Binary Pattern

# path = r'C:\Users\DELL\Downloads\photos_openCV\Photos\lady.jpg'
# path = r'C:\Users\DELL\Downloads\photos_openCV\Photos\group 2.jpg'
path = r'D:\From Downloads\photos_openCV\Photos\group 1.jpg'
img = cv.imread(path)
# cv.imshow('lady', img)
# cv.imshow('Group 2', img)
cv.imshow('Group 1', img)

# we use Haar Cascade classifier to detect faces that are present in the image.
# face detection does not involve skin tone or colours present in the image.
# Haar cascade look at the object in the image, and using the edges tries to determine whether it is
# a face or not.

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image', gray)

# reading haar_face.xml file
haar_cascade = cv.CascadeClassifier('haar_face.xml')
# CascadeClassifier() reads 33,000 line of XML code and store in the variable haar_cascade

# detect face
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)
# 1st parameter -> image
# 2nd parameter -> scale factor
# 3rd parameter -> minimum Neighbors -> specifies the number of neighbours a rectangle should have to be
# called a face.
# scaleFactor and minNeighbors detect the face and return the rectangle coordinates of the face as a
# list to faces_rect
# way to minimize the sensitivity to noise is modifying the scaleFactor and minNeighbors.

# can print number of faces found in the image by printing the length of 'faces_rect'
print(f"number of faces found = {len(faces_rect)}")

# we can loop over the list 'faces_rect' and grab the coordinates of those images and draw a rectangle
# over the detected face.
for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

cv.imshow('Detected faces', img)

cv.waitKey(0)