import cv2

import numpy as np

faceCascade = cv2.CascadeClassifier('/Users/sasan/Anaconda3/pkgs/libopencv-3.4.2-h20b85fd_0/Library/etc/haarcascades/haarcascade_frontalface_default.xml')

 

# grab the reference to the webcam

vs = cv2.VideoCapture(0)

 

# keep looping

while True:

    # grab the current frame

    ret, frame = vs.read()

 

    # if we are viewing a video and we did not grab a frame,

    # then we have reached the end of the video

    if frame is None:

        break

       

    faces = faceCascade.detectMultiScale(frame)

 

    for (x, y, w, h) in faces:

        cv2.rectangle(frame, (x, y), (x+w, y+h), (255,0,0), 2)

   

    # show the frame to our screen

    cv2.imshow("Video", frame)

    key = cv2.waitKey(1) & 0xFF

 

    # if the 'q' key is pressed, stop the loop

    if key == ord("q"):

        break
