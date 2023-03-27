import cv2 as cv

# Reading videos
path = r'C:\Users\DELL\Downloads\photos_openCV\videos\Sumit.mp4'
capture = cv.VideoCapture(path)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

while True:
    isTrue, frame = capture.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

    print(f"number of faces found = {len(faces_rect)}")

    for (x, y, w, h) in faces_rect:
        cv.rectangle(frame, (x, y), (x + w, y + h), (124, 59, 229), thickness=3)

        cv.putText(frame, str("Sumit"), (20, 20), cv.FONT_HERSHEY_COMPLEX, 1.0, (188, 139, 32), 2)

    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

