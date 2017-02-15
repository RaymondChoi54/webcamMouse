import pyautogui

class MouseControl:

	class __init__(self, screen_x, screen_y, center_x, center_y, circ_raid, x_sensitivity, y_sensitivity):
		self.screen_x = screen_x
		self.screen_y = screen_y
		self.center_x = center_x
		self.center_y = center_y
		self.circ_raid = circ_raid
		self.x_sensitivity = x_sensitivity
		self.y_sensitivity = y_sensitivity
		
	def smart_mouse_move(self, x, y):
		
		int x_move = 0
		int y_move = 0
		
		current_x, current_y = pyautogui.position()
		if(x > self.center_x + circ_raid):
			x_move = - x_sensitivity
		elif(x < self.center_x - circ_raid):
			x_move = x_sensitivity
			
		if(y > self.center_y + circ_raid):
			y_move = y_sensitivity
		elif(y < self.center_y - circ_raid):
			y_move = -y_sensitivity
			
		pyautogui.moveTo(current_x + x_move, current_y + y_move, duration=0)

	def move_mouse(x, y):
		pyautogui.moveTo(x, y, duration=0)
		
	def recalibrate(self, x, y):
		self.center_x = x
		self.center_y = y

	def auto_res(self):
		self.screen_x = pyautogui.size()[0]
		self.screen_y = pyautogui.size()[1]

	def mouse_loc():
		pyautogui.position()

	def click(type):
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
