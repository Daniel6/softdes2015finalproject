from xml.etree import ElementTree
from xml.dom import minidom
from upload import imgur_Upload
from edit_image import edit
from qr_code import generate_QRCode
import gtk
import subprocess

class Workflow(object):
	def __init__(self, workflowNumber):
		self.workflowNumber = workflowNumber
		self.updateSettings()
		self.keys = [False for key in self.hotkeys]
		self.URL = ""

	def run(self):
		#Handle different capture methods
		if self.capture_method == "def_rect":
			subprocess.call(["/usr/bin/python2.7", "./capture.py"]) #Spawn a new process that takes a screenshot

		#Handle things to do after capturing
		if "edit" in self.after_capture:
			edit("screenshot.png")
		if "upload" in self.after_capture:
			if self.destination == "imgur":
				self.URL = imgur_Upload("screenshot.png")

		#Handle things to do after uploading
		if "copy_link_to_clipboard" in self.after_upload:
			if "upload" in self.after_capture:
				clipboard = gtk.clipboard_get()
				clipboard.set_text(self.URL)
				clipboard.store()
		if "generate_qr_code" in self.after_upload:
			if "upload" in self.after_capture:
				if self.URL != "":
					generate_QRCode(self.URL)
				

	def keyDown(self, key):
		self.updateSettings()
		if key in self.hotkeys:
			self.keys[self.hotkeys.index(key)] = True

		if all(key is True for key in self.keys): #If all keys are held down, run workflow
			self.run()

	def keyUp(self, key):
		if key in self.hotkeys:
			self.keys[self.hotkeys.index(key)] = False

	def updateSettings(self):
		self.settings = ElementTree.parse('settings.xml').getroot()
		self.subsettings = self.settings.find('workflows').find('workflow' + str(self.workflowNumber)) #Find sub-branch of settings for this workflow

		try:
			self.destination = self.settings.find('destination').text #Grab destination from top level settings
		except:
			self.destination = ""

		try:
			self.capture_method = self.subsettings.find('capture_method').text
		except:
			self.capture_method = ""

		try:
			old_len = len(self.hotkeys)
			self.hotkeys = self.subsettings.find('hotkeys').text.split('+')
			if old_len != len(self.hotkeys):
				self.keys = [False for key in self.hotkeys]
		except:
			self.hotkeys = [""]

		try:
			self.after_capture = self.subsettings.find('after_capture').text.split(',')
		except:
			self.after_capture = [""]

		try:
			self.after_upload = self.subsettings.find('after_upload').text.split(',')
		except:
			self.after_upload = [""]

		

if __name__ == "__main__":
	workflow1 = Workflow(1) #Workflow defined by number