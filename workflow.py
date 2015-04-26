from xml.etree import ElementTree
from xml.dom import minidom
from capture import takeScreenshot
from anon_upload import anonymous_Upload
from edit_image import edit
import gtk
import subprocess

class Workflow(object):
	def __init__(self, workflowNumber):

		self.settings = ElementTree.parse('settings.xml').getroot()
		self.subsettings = self.settings.find('workflows').find('workflow' + str(workflowNumber)) #Find sub-branch of settings for this workflow


		self.destination = self.settings.find('destination').text #Grab destination from top level settings
		self.capture_method = self.subsettings.find('capture_method').text
		self.hotkeys = self.subsettings.find('hotkeys').text.split('+')
		self.after_capture = self.subsettings.find('after_capture').text.split(',')
		self.after_upload = self.subsettings.find('after_upload').text.split(',')

		self.keys = [False for key in self.hotkeys]
		self.URL = ""

	def run(self):
		#Handle different capture methods
		if self.capture_method == "def_rect":
			subprocess.call(["/usr/bin/python2.7", "./capture.py"]) #Spawn a new process that takes a screenshot

		#Handle things to do after capturing
		if "edit" in self.after_capture:
			edit()
		if "upload" in self.after_capture:
			if self.destination == "imgur_anon":
				self.URL = anonymous_Upload("screenshot.png")

		#Handle things to do after uploading
		if "copy_link_to_clipboard" in self.after_upload:
			if "upload" in self.after_capture:
				clipboard = gtk.clipboard_get()
				clipboard.set_text(self.URL)
				clipboard.store()
				

	def keyDown(self, key):
		if key in self.hotkeys:
			self.keys[self.hotkeys.index(key)] = True

		if all(key is True for key in self.keys): #If all keys are held down, run workflow
			self.run()

		# print(self.keys)

	def keyUp(self, key):
		if key in self.hotkeys:
			self.keys[self.hotkeys.index(key)] = False
		# print(self.keys)

	def prettify(self, elem): #Method for formatting xml tree for printing
		"""Return a pretty-printed XML string for the Element.
		"""
		rough_string = ElementTree.tostring(elem, 'utf-8')
		reparsed = minidom.parseString(rough_string)
		return reparsed.toprettyxml(indent="  ")

if __name__ == "__main__":
	workflow1 = Workflow(1) #Workflow defined by number