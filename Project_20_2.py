# Here, model recognize faces
import math

import cv2 as cv
import os
from tkinter import *
from tkinter import filedialog


haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = []

# add name present in the folder in the "people" list
people = []
for i in os.listdir(r'D:\From Downloads\photos_openCV\trainModelProject'):
    people.append(i)


face_recognizer = cv.face.LBPHFaceRecognizer_create()     # LBP -> Local Binary Pattern Histogram
face_recognizer.read('face_trained_project.yml')

# --- User Interface ---
# ---------------------------------------------------------------------------------------------


def open_image_file():
    # path of file

    image_path = filedialog.askopenfilename(initialdir="D:\\From Downloads\\photos_openCV",
                                            title="Choose Your File",
                                            filetypes=(("Video file", "*.mp4"), ("other files", "*.mkv")))

    return image_path


window = Tk()

window.geometry("400x200")

window.title("Face Recognition")

title_label = Label(text="Greeting To All,\n My name is Pravesh Singh\n Welcome! see my mini-project.", bg="red",
                    fg="white", padx=100, pady=50, font="copperplate 15 bold", borderwidth=3, relief=SUNKEN)
title_label.pack()


# ---------------------------------------------------------------------------------------------

capture = cv.VideoCapture(open_image_file())

while True:
    isTrue, frame = capture.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Detect the faces in the image and return no of faces
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)

    print(f"number of faces found = {len(faces_rect)}")

    for (x, y, w, h) in faces_rect:
        faces_roi = gray[y:y + h, x:x + w]  # roi -> region of interest

        label, confidence = face_recognizer.predict(faces_roi)
        print(f'Label = {people[label]} with a confidence of {math.ceil(confidence)}')

        # less the confidence is better
        if (people[label] == name for name in people) and confidence < 90:
            cv.rectangle(frame, (x, y), (x + w, y + h), (235, 52, 150), thickness=2)

            cv.putText(frame, str(people[label]), (x, y-10), cv.FONT_HERSHEY_COMPLEX, 1.0, (52, 235, 140), 1)
            # 1st parameter -> source image
            # 2nd parameter -> text -> string of people of label (the person involve in the image)
            # 3rd parameter -> origin
            # 4th parameter -> font-face
            # 5th parameter -> fontScale
            # 6th parameter -> color
            # 7th parameter -> thickness

    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF == ord('q'):
        break


capture.release()
cv.destroyAllWindows()

