#!python2
import sys
import cv2
from MouseControl import MouseControl
import threading
import time
import pygame


# Create mousecontrol ocject for controlling use
mouseControl = None

# Import Haar Classifiers
faceCascade = cv2.CascadeClassifier(sys.argv[1])
eyesCascade = cv2.CascadeClassifier(sys.argv[2])
leftEyeOpen = cv2.CascadeClassifier(sys.argv[3])
rightEyeOpen = cv2.CascadeClassifier(sys.argv[4])

# Set up
video_capture = cv2.VideoCapture(0)
mouseInstructionImg = cv2.imread('assets\pictures\moveFace.png')
clickInstructionImg = cv2.imread('assets\pictures\holdClick.png')
nx, ny = 0, 0;
maxX, maxY, minX, minY = None, None, None, None
centerX, centerY = None, None

# Begin Program
cv2.namedWindow("calibrate", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("calibrate",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

file = 'assets/voice_training/calibrationonly.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()
startTime = time.time()
debug_training = 1

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

	for (x, y, w, h) in faces:
		# Calibration
		if ((time.time() - startTime) > 6 and (time.time() - startTime) < 13):
			cv2.putText(frame,"Stage 1 Calibration -- Seconds Left: " + str((startTime + 13 - time.time())), (10,400), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255))
			
			# Obtain center
			centerX = x + (w/2)
			centerY = y + (h/2)

			# Set max and min
			if not maxX:
				maxX = centerX
				minX = centerX
				maxY = centerY
				minY = centerY
		elif ((time.time() - startTime) > 12 and (time.time() - startTime) < 37):
			cv2.putText(frame,"Stage 2 Calibration -- Seconds Left: " + str((startTime + 37 - time.time())), (10,400), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255))
			if ((time.time() - startTime) > 12 and (time.time() - startTime) < 27):
				frame[0:0+mouseInstructionImg.shape[0], 0:0+mouseInstructionImg.shape[1]] = mouseInstructionImg
			else:
				frame[0:0+clickInstructionImg.shape[0], 0:0+clickInstructionImg.shape[1]] = clickInstructionImg

			# Keep getting max and min
			if (x + (w/2) < minX):
				minX = x + (w/2)
			if (y + (h/2) < minY):
				minY = y + (h/2)
			if ((x + (w/2)) > maxX):
				maxX = x + (w/2)
			if ((y + (h/2)) > maxY):
				maxY = y + (h/2)

			# Obtain center
			centerX = (maxX + minX)/2
			centerY = (maxY + minY)/2
			cv2.rectangle(frame, (centerX, centerY), (centerX + 1, centerY + 1), (255, 255, 255), 1) # Draw a center dot
			cv2.rectangle(frame, (minX, minY), (maxX, maxY), (255, 0, 0), 1) # Draw a rectangle around the calibration

		# Draw crosshair on person
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1) # Draw a rectangle around the faces	
		cv2.line(frame, ((x + w / 2), 0), ((x + w / 2), frameWidth), (0,0,255), 1)
		cv2.line(frame, (0, (y + h / 2)), (frameHeight, (y + h / 2)), (0,0,255), 1)

		# Get nose coordinates
		nx = (x + w / 2)
		ny = (y + h / 2)

		#cv2.putText(frame,"Track Coordinates: (" + str(nx) + "," + str(ny) + ")", (10,50), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0))
		cv2.putText(frame,"press Q to quit", (0,20), cv2.FONT_HERSHEY_PLAIN, 1, (255,0,0))

		# Send coordinates over to mouse control only if not in calibration mode
		if ((time.time() - startTime) > 37):
			# Create Mouse Control if not created
			if not mouseControl:
				mouseControl = MouseControl(frame.shape[1], frame.shape[0], centerX, centerY, min((maxX - centerX), (maxY - centerY), (centerY - minY), (centerX - minX)), 50, 50)
			
			thr = threading.Thread(target=mouseControl.smart_mouse_move, args=(nx, ny), kwargs={})
			thr.start()

	# Display the resulting frame
	if ((time.time() - startTime) > 0 and (time.time() - startTime) < 37):
		cv2.imshow("calibrate", frame)
	else:
		cv2.circle(frame, (centerX, centerY), min((maxX - centerX), (maxY - centerY), (centerY - minY), (centerX - minX)), (255, 255, 255), 1) # Draw curcle around area
		cv2.destroyWindow('calibrate')
		cv2.destroyWindow('Instructions')
		cv2.imshow("Face Track", frame)
	
	# Quit Detection
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()