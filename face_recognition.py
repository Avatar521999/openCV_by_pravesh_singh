import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = ['Ben Afflek', 'joe', 'Modi']

# load feature and label array
# features = np.load('features.npy', allow_pickle=True)
# label = np.load('labels.npy', allow_pickle=True)
# since, datatype are objects , use allow_pickle=True

face_recognizer = cv.face.LBPHFaceRecognizer_create()     # LBP -> Local Binary Pattern Histogram
face_recognizer.read('face_trained.yml')

path = r'D:\From Downloads\photos_openCV\validation\modi\3.jpg'
img = cv.imread(path)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Person', gray)

# Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]             # roi -> region of interest

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (20, 20), cv.FONT_HERSHEY_COMPLEX, 1.0, (100, 255, 200), 2)
    # 1st parameter -> source image
    # 2nd parameter -> text -> string of people of label (the person involve in the image)
    # 3rd parameter -> origin
    # 4th parameter -> fontface
    # 5th parameter -> fontScale
    # 6th parameter -> color
    # 7th parameter -> thickness
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), thickness=2)

cv.imshow('Detected Face', img)

cv.waitKey(0)