from xml.etree import ElementTree
import time
import sys
sys.path.insert(1, './lib/pyxhook')
import pyxhook
from workflow import Workflow

def keyDownEvent(event):
	print "Ascii: " + str(event.Ascii) + " Scan Code: " + str(event.ScanCode) + " Key Val: " + str(event.Key)
	for flow in workflows:
		flow.keyDown(event.Key)

	if event.Key == "space": #exit program when spacebar pressed
		global running
		running =  False

def keyUpEvent(event):
	for flow in workflows:
		flow.keyUp(event.Key)
	
def loadWorkflows():
	#Load settings file
	settings = ElementTree.parse('settings.xml').getroot()
	#Get number of workflows
	num_flows = settings.find('num_workflows').text

	for i in range(1, int(num_flows)+1): #For each workflow in the settings, create corresponding workflow class
		#Define Workflows
		workflow = Workflow(i)

		#Add workflow to list of workflows
		workflows.append(workflow)

if __name__ == "__main__":

	#Setup Hooks into keyboard
	hookman = pyxhook.HookManager()
	hookman.KeyDown = keyDownEvent #Bind keydown and keyup events
	hookman.KeyUp = keyUpEvent
	hookman.HookKeyboard()

	#Start event listener
	hookman.start()

	#Initialize workflows list
	global workflows
	workflows = []

	#Load all the workflows from settings
	loadWorkflows()

	#Start infinite loop
	running = True
	while running: 
		time.sleep(.1) #sleep for .1 seconds

	hookman.cancel() #Close listener when done