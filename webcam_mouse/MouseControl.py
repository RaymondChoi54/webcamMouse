import pyautogui

class MouseControl:

	class __init__(self, screen_x, screen_y, center_x, center_y):
		self.screen_x = screen_x
		self.screen_y = screen_y
		self.center_x = center_x
		self.center_y = center_y
		
	def smart_mouse_move(self, x, y):
		pyautogui.moveTo(x, y, duration=0)

	def move_mouse(x, y):
		pyautogui.moveTo(x, y, duration=0)

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
