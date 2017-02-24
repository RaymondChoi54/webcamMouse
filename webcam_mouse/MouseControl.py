import pyautogui
import math

class MouseControl(object):

	def __init__(self, webcam_x, webcam_y, center_x, center_y, circ_raid, x_sensitivity, y_sensitivity, mouse_acc=false, multiplier=1.1, invert=false):

		self.webcam_x = webcam_x
		self.webcam_y = webcam_y
		self.center_x = center_x
		self.center_y = center_y
		self.circ_raid = circ_raid
		self.x_sensitivity = x_sensitivity
		self.y_sensitivity = y_sensitivity
		self.mouse_acc = mouse_acc
		self.multiplier = multiplier
		self.invert = invert
		self.screen_width, self.screen_height = pyautogui.size() 
		
	def smart_mouse_move(self, x, y):
		
		move_x = 0
		move_y = 0
		multiply_x = 1
		multiply_y = 1
		invert_multi = 1
		current_x, current_y = pyautogui.position()

		x_displacement = math.fabs(x - self.center_x) 
		y_displacement = math.fabs(y - self.center_y)

		displacement = (x_displacement ** 2 + y_displacement ** 2) ** 0.5

		if(self.invert):
			invert_multi = -1
		
		if(displacement >= self.circ_raid):

			if(self.mouse_acc):
				multiply_x = multiplier ** (math.fabs(x - self.center_x) / self.circ_raid)
				multiply_y = multiplier ** (math.fabs(y - self.center_y) / self.circ_raid)
			
			if(0 > x - self.center_x):
				current_x = self.x_sensitivity * multiply_x * invert_multi + current_x
			else:
				current_x = - self.x_sensitivity * multiply_x * invert_multi + current_x
				
			if(0 > y - self.center_y):
				current_y = self.y_sensitivity * multiply_y * invert_multi + current_y
			else:
				current_y = - self.y_sensitivity * multiply_y * invert_multi + current_y

			if(current_x < 0):
				current_x = 0
			elif(current_x > self.screen_width):
				current_x = self.screen_width

			if(current_y < 0):
				current_y = 0
			elif(current_y > self.screen_height):
				current_y = self.screen_height

			pyautogui.moveTo(current_x, current_y, duration=0)

	def move_mouse(self, x, y):
		pyautogui.moveTo(x, y, duration=0)
		
	def recalibrate(self, x, y):
		self.center_x = x
		self.center_y = y

	def mouse_loc(self):
		return pyautogui.position()

	def click(self, type):
		if(type == "left"):
			pyautogui.click()
		elif(type == "right"):
			pyautogui.rightClick()
		elif(type == "middle"):
			pyautogui.middleClick()
		elif(type == "double"):
			pyautogui.doubleClick()
		elif(type == "hold"):
			pyautogui.mouseDown()
		elif(type == "release"):
			pyautogui.mouseUp()

