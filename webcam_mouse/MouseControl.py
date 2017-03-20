import pyautogui
import math
import time

class MouseControl(object):

	def __init__(self, webcam_x, webcam_y, center_x, center_y, circ_raid, x_sensitivity, y_sensitivity, mouse_acc=False, multiplier=1.1, invert=False):

		self.webcam_x = webcam_x
		self.webcam_y = webcam_y
		self.center_x = center_x #Where the middle of the circle is
		self.center_y = center_y
		self.circ_raid = (2 * circ_raid) / 3 #Have to pass 2/3 of the radius for the mouse to move
		self.x_sensitivity = x_sensitivity
		self.y_sensitivity = y_sensitivity
		self.mouse_acc = mouse_acc
		self.multiplier = multiplier #Mouse acceleration 
		self.invert = invert #If it's inverted or not
		self.screen_width, self.screen_height = pyautogui.size()
		self.start_time = time.time()
		pyautogui.FAILSAFE = False
		
	def smart_mouse_move(self, x, y):
		
		move_x = 0 #x displacement of the mouse
		move_y = 0 #y displacement of the mouse
		multiply_x = 1
		multiply_y = 1
		invert_multi = -1
		current_x, current_y = pyautogui.position() #Current position of the mouse

		if(self.mouse_acc):
			multiply_x = multiplier ** (math.fabs(x - self.center_x) / self.circ_raid)
			multiply_y = multiplier ** (math.fabs(y - self.center_y) / self.circ_raid)

		x_displacement = math.fabs(x - self.center_x) 
		y_displacement = math.fabs(y - self.center_y)

		displacement = (x_displacement ** 2 + y_displacement ** 2) ** 0.5 #How far the mouse moved from the middle

		if(self.invert):
			invert_multi = 1
		
		#To scroll or click
		if(time.time() - self.start_time > 5 and (current_y < 200 or current_y > self.screen_height - 200)):
			if(current_y < 200):
				pyautogui.click()
				pyautogui.scroll(30, x = self.screen_width / 2, y = self.screen_height / 2)
			elif(current_y > self.screen_height - 200):
				pyautogui.click()
				pyautogui.scroll(-30, x = self.screen_width / 2, y = self.screen_height / 2)
		elif(time.time() - self.start_time > 5):
			pyautogui.click()
			self.start_time = time.time()
		
		#To move
		if(displacement >= self.circ_raid):

			self.start_time = time.time()
			
			if(0 > x - self.center_x):
				current_x = x_displacement * self.x_sensitivity * multiply_x * invert_multi + current_x
			else:
				current_x = (- x_displacement * self.x_sensitivity * multiply_x * invert_multi) + current_x
				
			if(0 > y - self.center_y):
				current_y = y_displacement * self.y_sensitivity * multiply_y * invert_multi + current_y
			else:
				current_y = (- y_displacement * self.y_sensitivity * multiply_y * invert_multi) + current_y

			pyautogui.moveTo(current_x, current_y, duration=0)

	def move_mouse(self, x, y):
		pyautogui.moveTo(x, y, duration=0)
		
	def recalibrate(self, x, y):
		self.center_x = x
		self.center_y = y

	def mouse_loc(self):
		return pyautogui.position()
	
	def update_sensitivity(self, x, y):
		self.x_sensitivity = x
		self.y_sensitivity = y
	
	def get_sensitivity(self):
		return self.x_sensitivity, self.y_sensitivity

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

