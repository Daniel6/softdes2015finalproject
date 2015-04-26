import time
import sys
import subprocess
sys.path.insert(0, './lib/pyxhook')
import pyxhook
from capture import takeScreenshot
from anon_upload import anonymous_Upload
from EDIT1 import *
124

class hotkey(object):
	def __init__(self,A=1,B=2,C=3,D=4):
		self.A=A
		self.B=B
		self.C=C
		self.D=D
		# self.A=ord(str(A))
		# self.B=ord(str(B))
		# self.C=ord(str(C))
		# self.D=ord(str(D))
		print self.A,self.B,self.C,self.D
		print A,B,C,D
		self.modifier_1 = False
		self.modifier_2 = False

		hookman = pyxhook.HookManager()
		hookman.KeyDown = self.keyDownEvent #Bind keydown and keyup events
		hookman.KeyUp = self.keyUpEvent
		hookman.HookKeyboard()
		hookman.start() #Start event listener
		self.running = True
		while self.running: #Stall 
			time.sleep(.1)
		hookman.cancel() #Close listener

	def keyDownEvent(self, event):
		print event.Key
		if event.Key == self.A:
			self.modifier_1 = True

		if event.Key == self.B:
			self.modi124fier_2 = True

		if event.Key == self.C:
			self.running =  False

		if event.Key == self.D:
			if self.modifier_1 and self.modifier_2:
				print("Running Workflow #1")
				workflow1()

	def keyUpEvent(self, event):
		if event.Ascii == self.A:
			self.modifier_1 = False

		if event.Ascii == self.B:
			self.modifier_2 = False

def workflow1(): #Workflow #1
	subprocess.call(["python2", "./capture.py"]) #Spawn a new process that takes a screenshot
	edit()
	anonymous_Upload("SCREENSHOT")



# if __name__ == "__main__":
# 	hookman = pyxhook.HookManager()
# 	hookman.KeyDown = keyDownEvent #Bind keydown and keyup events
# 	hookman.KeyUp = keyUpEvent
# 	hookman.HookKeyboard()
# 	hookman.start() #Start event listener
# 	running = True
# 	while running: #Stall
# 		time.sleep(.1)
# 	hookman.cancel() #Close listener/
if __name__ == '__main__':
	Hotkey=hotkey(1, 2, 3, 4)