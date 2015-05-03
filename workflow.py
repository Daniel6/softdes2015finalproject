from xml.etree import ElementTree
from xml.dom import minidom
from upload import imgur_Upload, dropbox_Upload, twitter_Upload
from edit_image import edit
from qr_code import generate_QRCode
import gtk
import subprocess

class Workflow(object):
	def __init__(self, workflowNumber):
		"""Initialize workflow settings based on workflow number"""
		self.workflowNumber = workflowNumber
		self.updateSettings()
		self.keys = [False for key in self.hotkeys]
		self.URL = ""

	def run(self):
		"""Activate the workflow"""
		#Handle different capture methods
		if self.capture_method == "def_rect":
			subprocess.call(["/usr/bin/python2.7", "./capture.py"]) #Spawn a new process that takes a screenshot

		#Handle things to do after capturing
		if "edit" in self.after_capture:
			edit("screenshot.png")
		if "upload" in self.after_capture:
			if "imgur" in self.destinations:
				self.URL = imgur_Upload("screenshot.png")
			if "dropbox" in self.destinations:
				self.URL = dropbox_Upload("screenshot.png", "screenshot.png")
			if "twitter" in self.destinations:
				self.URL = twitter_Upload("screenshot.png", "Test of UploadX")

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
		"""Register that a key was depressed"""
		self.updateSettings()
		if key in self.hotkeys:
			self.keys[self.hotkeys.index(key)] = True

		if all(key is True for key in self.keys): #If all keys are held down, run workflow
			self.run()

	def keyUp(self, key):
		"""Register that a key was unpressed"""
		if key in self.hotkeys:
			self.keys[self.hotkeys.index(key)] = False

	def updateSettings(self):
		"""Re-Read settings from settings.xml to update parameters"""
		self.settings = ElementTree.parse('settings.xml').getroot()
		self.subsettings = self.settings.find('workflows').find('workflow' + str(self.workflowNumber)) #Find sub-branch of settings for this workflow

		try:
			self.destinations = self.settings.find('destinations').text.split(',') #Grab destinations from top level settings
		except:
			self.destinations = ""

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
	workflow1.run()