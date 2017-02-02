#!python2
import sys
import cv2

faceCascade = cv2.CascadeClassifier(sys.argv[1])
eyesCascade = cv2.CascadeClassifier(sys.argv[2])
noseCascade = cv2.CascadeClassifier(sys.argv[3])

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Flip frame
    frame = cv2.flip(frame,1)

    nx, ny = 0, 0;

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame,"face", (x,y), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0))
        # ROI top for eyes
        roi_eye_gray = gray[y:y+(2*h/3), x:x+w]
        roi_eye_color = frame[y:y+(2*h/3), x:x+w]

        # ROI middle for nose
        roi_nose_gray = gray[y+(h/3):y+(3*h/4), x+(w/3):x+(2*w/3)]
        roi_nose_color = frame[y+(h/3):y+(3*h/4), x+(w/3):x+(2*w/3)]
        
        eyes = eyesCascade.detectMultiScale(roi_eye_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_eye_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)

        noses = noseCascade.detectMultiScale(roi_nose_gray)
        for (ex,ey,ew,eh) in noses:
            cv2.rectangle(roi_nose_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
            nx = ex + x
            ny = ey + y

        cv2.putText(frame,"Nose Coordinates: (" + str(nx) + "," + str(ny) + ")", (10,50), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0))
        cv2.putText(frame,"press Q to quit", (0,20), cv2.FONT_HERSHEY_PLAIN, 1, (255,0,0))

    # Display the resulting frame
    cv2.imshow('TIMOTHY DEBUG', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()