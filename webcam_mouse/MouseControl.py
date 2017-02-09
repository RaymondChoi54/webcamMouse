import pyautogui


class MouseControl:

	class __init__(self, x, y, center_x, center_y):
		self.x = x
		self.y = y
		self.center_x = center_x
		self.center_y = center_y

	def move_mouse(x, y):
		pyautogui.moveTo(x, y, duration=0)

	def auto_res():
		x = pyautogui.size()[0]
		y = pyautogui.size()[1]

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
