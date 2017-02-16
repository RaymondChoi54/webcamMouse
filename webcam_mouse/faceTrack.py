#!python2
import sys
import cv2
from MouseControl import MouseControl


# Create mousecontrol ocject for controlling use
mouseControl = MouseControl(0, 0, 0, 0,0,0,0)

faceCascade = cv2.CascadeClassifier(sys.argv[1])
eyesCascade = cv2.CascadeClassifier(sys.argv[2])
leftEyeOpen = cv2.CascadeClassifier(sys.argv[3])
rightEyeOpen = cv2.CascadeClassifier(sys.argv[4])

video_capture = cv2.VideoCapture(0)

nx, ny = 0, 0;

while True:
	# Capture frame-by-frame
	ret, frame = video_capture.read()
	frameWidth, frameHeight = frame.shape[:2]

	# Flip frame
	frame = cv2.flip(frame,1)
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
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)
		
		# ROI top for both eyes
		roi_eyes_gray = gray[y+(h/4):y+(3*h/5), x:w+x]
		roi_eyes_color = frame[y+(h/4):y+(3*h/5), x:w+x]

		eyes = eyesCascade.detectMultiScale(roi_eyes_gray)
		for (ex,ey,ew,eh) in eyes:
			# ROI top for left eye
			roi_left_eye_gray = roi_eyes_gray[ey:ey+eh, ex:ex+(ew/2)]
			roi_left_eye_color = roi_eyes_color[ey:ey+eh, ex:ex+(ew/2)]

			# ROI top for right eye
			roi_right_eye_gray = roi_eyes_gray[ey:ey+eh, ex+(ew/2):ex+ew]
			roi_right_eye_color = roi_eyes_color[ey:ey+eh, ex+(ew/2):ex+ew]

			# Debug
			cv2.imshow('Face Crop', cv2.resize(frame[y:y+h, x:w+x], (200, 200)))
			cv2.imshow('Eyes Crop', cv2.resize(roi_eyes_color[ey:ey+eh, ex:ex+ew], (200, 80)))
			cv2.imshow('Left Eye Crop', cv2.resize(roi_left_eye_color, (150, 120)))
			cv2.imshow('Right Eye Crop', cv2.resize(roi_right_eye_color, (150, 120)))

			# TODO: Blink detection
			#lefteye = leftEyeOpen.detectMultiScale(roi_left_eye_gray)
				#for (ex,ey,ew,eh) in lefteye:
		#		cv2.rectangle(roi_left_eye_color,(ex,ey),(ex+ew,ey+eh),(0,255,255),1)

			#righteye = rightEyeOpen.detectMultiScale(roi_left_eye_gray)
				#for (ex,ey,ew,eh) in righteye:
		#		cv2.rectangle(roi_right_eye_color,(ex,ey),(ex+ew,ey+eh),(0,255,255),1)

		# Draw crosshair on person
		cv2.line(frame, ((x + w / 2), 0), ((x + w / 2), frameWidth), (0,0,255), 1)
		cv2.line(frame, (0, (y + h / 2)), (frameHeight, (y + h / 2)), (0,0,255), 1)

		# Get nose coordinates
		nx = (x + w / 2)
		ny = (y + h / 2)

		cv2.putText(frame,"Track Coordinates: (" + str(nx) + "," + str(ny) + ")", (10,50), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0))
		cv2.putText(frame,"press Q to quit", (0,20), cv2.FONT_HERSHEY_PLAIN, 1, (255,0,0))

		# Send coordinates over to mouse control
		mouseControl.move_mouse(nx, ny) # TODO: Speed up

	# Display the resulting frame
	cv2.imshow('Face Tracking', frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()


# Helper Functions
def playAudio(sound):
	pass