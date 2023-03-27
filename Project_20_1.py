# Here, we make model to learn about given faces
# ---- Training Phase ----

import os
import cv2 as cv
import numpy as np


# add name present in the folder in the "people" list
people = []
for i in os.listdir(r'D:\From Downloads\photos_openCV\trainModelProject'):
    people.append(i)

DIR = r'D:\From Downloads\photos_openCV\trainModelProject'

# training set consist of two list:
# 1. features -> image array of faces
# 2. labels -> whose face does it belong to

# haar_cascade XML file
# Loading the model state from a given XML.
haar_cascade = cv.CascadeClassifier('haar_face.xml')


features = []
labels = []


def create_train():
    for person in people:
        path = os.path.join(DIR, person)    # joins the path
        label = people.index(person)

        # inside give name folder
        for img in os.listdir(path):
            img_path = os.path.join(path, img)  # path to an image, read image from the path

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]                             # region of interest
                features.append(faces_roi)
                labels.append(label)     # label variable is index of people list


create_train()
print("Training Done --------------------------------")
# print(f'Length of the features list = {len(features)}')
# print(f"Length of the labels list = {len(labels)}")

# convert features and labels list to numpy array
features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer.create()     # instantiate the face recognizer

# use features and label list to train the recognizer
face_recognizer.train(features, labels)

# Saving the model state to a given XML or YAML.
face_recognizer.save('face_trained_project.yml')
# save features and labels list
np.save('features.npy', features)
np.save('labels.npy', labels)

cv.waitKey(0)
