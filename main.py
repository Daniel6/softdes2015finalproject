import time
import sys
import subprocess
sys.path.insert(0, './lib/pyxhook')
import pyxhook
from capture import takeScreenshot

def keyDownEvent(event):
	if event.ScanCode == 37: #If the scan code matches left control, signal that the ctrl button is pressed
		global ctrl
		ctrl = True

	if event.ScanCode == 50: #If the scan code matches left shift, signal that the shift button is pressed
		global shift
		shift = True

	if event.Ascii == 32: #If the ascii value matches spacebar, terminate the while loop
		global running
		running =  False
	elif event.Ascii == 52: #If the ascii value matches '4', and both ctrl and shift are pressed, run screenshot.py
		if ctrl and shift:
			print("Running Workflow #1")
			workflow1()

def keyUpEvent(event):
	if event.ScanCode == 37: #If the scan code matches left control, signal that the ctrl button is not pressed
		global ctrl
		ctrl = False

	if event.ScanCode == 50: #If the scan code matches left shift, signal that the shift button is not pressed
		global shift
		shift = False

def workflow1(): #Workflow #1
	subprocess.call(["python2", "./capture.py"]) #Spawn a new process that takes a screenshot

if __name__ == "__main__":
	hookman = pyxhook.HookManager()
	hookman.KeyDown = keyDownEvent #Bind keydown and keyup events
	hookman.KeyUp = keyUpEvent
	hookman.HookKeyboard()
	hookman.start() #Start event listener
	running = True
	while running: #Stall
		time.sleep(.1)
	hookman.cancel() #Close listener