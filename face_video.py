# this is for reference
import cv2
# for loading image

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# to capture video from webcam
cap = cv2.VideoCapture(0)
#we can use this as taking input as video files cap = cv2.VideoCapture('filename.mp4')
while True:
    #read the frame
    _, img = cap.read()
    #convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # draw the rectangle around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    # display
    cv2.imshow('img', img)
     # to stop if escape key is pressed syntax
    k = cv2.waitKey(30) & 0xff
    if k==27 :
        break
        # release the video capture object
cap.release()
#finally I completed basic tutorial of opencv I am so happy


