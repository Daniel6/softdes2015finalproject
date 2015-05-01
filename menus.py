from xml.etree import ElementTree
from xml.dom import minidom
import sys
import os
sys.path.insert(1, './lib')
import asynchronous_file_reader
import gtk
import time
import Queue
import subprocess

class MainMenu(object):
	def __init__(self):
		self.init_Window()
		self.init_Buttons()

	def init_Buttons(self):
		self.settings_button = gtk.Button(label='Settings')
		self.destination_button = gtk.Button(label='Destinations')
		self.man_capture_button = gtk.Button(label='Capture')
		self.man_edit_button = gtk.Button(label='Edit Image')

		self.settings_button.connect('button-press-event', self.openSettings)
		self.destination_button.connect('button-press-event', self.openDestinations)
		self.man_capture_button.connect('button-press-event', self.manCapture)
		self.man_edit_button.connect('button-press-event', self.manEdit)

		self.vbox.pack_start(self.settings_button, False, False, 1)
		self.vbox.pack_start(self.destination_button, False, False, 1)
		self.hbox = gtk.HBox(False, 0)
		self.hbox.pack_start(self.man_capture_button, True, True, 0)
		self.hbox.pack_start(self.man_edit_button, True, True, 0)
		self.vbox.pack_start(self.hbox)

		self.settings_button.show()
		self.destination_button.show()
		self.man_capture_button.show()
		self.man_edit_button.show()
		self.hbox.show()

	def openSettings(self, widget, event):
		self.settingsMenu.start()

	def openDestinations(self, widget, event):
		pass

	def manCapture(self, widget, event):
		subprocess.call(["/usr/bin/python2.7", "./capture.py"])

	def manEdit(self, widget, event):
		pass

	def init_Window(self):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_title('Main Menu')
		self.window.set_position(gtk.WIN_POS_CENTER)
		self.window.set_size_request(300, 200)
		self.window.connect("delete_event", self.delete_event) #When user presses orange X, quit out of gtk main loop
		self.vbox = gtk.VBox(False, 0)
		self.window.add(self.vbox)

		self.vbox.show()

	def start(self):
		self.window.show()
		self.startListener()
		gtk.main()

	def startListener(self):
		#Open listener in new process
		self.listener_process = subprocess.Popen(["/usr/bin/python2.7", "./listener.py"], stdout = subprocess.PIPE, stderr = subprocess.STDOUT, bufsize=1)
		self.stdout_queue = Queue.Queue()
		self.stdout_reader = asynchronous_file_reader.AsynchronousFileReader(self.listener_process.stdout, self.stdout_queue)
		self.stdout_reader.start()
		self.settingsMenu = SettingsMenu(self.stdout_reader, self.stdout_queue)

	def delete_event(self, widget, event):
		os.system("pkill python -15")
		gtk.main_quit()

class SettingsMenu(object):
	def __init__(self, stdout_reader, stdout_queue):
		self.init_listener(stdout_reader, stdout_queue)
		self.init_Window()
		self.init_HotkeySettings()
		self.init_AfterCaptureSettings()
		self.init_AfterUploadSettings()
		self.init_SaveButton()

	def init_listener(self, stdout_reader, stdout_queue):
		self.stdout_reader = stdout_reader
		self.stdout_queue = stdout_queue
		self.count = 0

	def init_Window(self):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_title('Workflow Settings')
		self.window.set_position(gtk.WIN_POS_CENTER)
		self.window.set_size_request(400, 300)
		self.window.connect("delete_event", self.delete_event) #When user presses orange X, quit out of gtk main loop
		self.vbox = gtk.VBox(False, 0)
		self.window.add(self.vbox)

		self.vbox.show()

	def init_HotkeySettings(self):
		self.hotkey_label = gtk.Label(str='Set Hotkey')
		self.vbox.pack_start(self.hotkey_label, False, False, 2)

		self.hbox = gtk.HBox(False, 0)
		self.hotkey = gtk.Entry(max=0)
		self.hotkey.connect('focus-in-event', self.startListening)
		self.hotkey.set_editable(False)
		self.hbox.pack_start(self.hotkey, False, False, 5)
		self.vbox.pack_start(self.hbox, False, False, 0)

		self.hbox.show()
		self.hotkey_label.show()
		self.hotkey.show()

	def init_AfterCaptureSettings(self):
		self.after_capture_box = gtk.HBox(False, 0)
		self.after_capture_label = gtk.Label(str='What to do after capturing image')
		self.vbox.pack_start(self.after_capture_label, False, False, 2)
		self.upload_option = gtk.ToggleButton(label='Upload')
		self.edit_option = gtk.ToggleButton(label='Edit')
		self.after_capture_box.pack_start(self.upload_option, False, False, 0)
		self.after_capture_box.pack_start(self.edit_option, False, False, 0)
		self.vbox.pack_start(self.after_capture_box, False, False, 0)
		
		self.after_capture_label.show()
		self.upload_option.show()
		self.edit_option.show()
		self.after_capture_box.show()

	def init_AfterUploadSettings(self):
		self.after_upload_box = gtk.HBox(False, 0)
		self.after_upload_label = gtk.Label(str='What to do after uploading image')
		self.vbox.pack_start(self.after_upload_label, False, False, 2)
		self.copy_link_option = gtk.ToggleButton(label='Copy link to clipboard')
		self.after_upload_box.pack_start(self.copy_link_option, False, False, 0)
		self.vbox.pack_start(self.after_upload_box, False, False, 0)

		self.after_upload_label.show()
		self.copy_link_option.show()
		self.after_upload_box.show()

	def init_SaveButton(self):
		self.save_button = gtk.Button(label='Save')
		self.save_button.connect('button-press-event', self.save_button_pressed)
		self.vbox.pack_end(self.save_button, False, False, 2)
		self.save_button.show()

	def startListening(self, widget, event):
		print("Started Listening")
		self.hotkey.set_text("")
		self.save_xml()
		running = True
		while not self.stdout_reader.eof():

			while not self.stdout_queue.empty():
				self.count += 1
				out = (self.stdout_queue.get())
				print(out.rstrip())
				if out == "Return\n":
					print("Stopping")
					running = False
					break
				if self.count > 3: #Ignore first three messages
					print("Adding key")
					self.hotkey.set_text(self.hotkey.get_text() + out.rstrip() + "+")
				else:
					print(self.count)
				
			if not running:
				break
			time.sleep(.02)

		self.count = 3 #Reset to 3 instead of 0 so that we don't ignore the first three outputs next time
		print("Done Listening")

	def save_button_pressed(self, widget, event):
		self.save_xml()

	def delete_event(self, widget, event):
		self.window.hide()
		return True

	def start(self):
		self.window.show()
		gtk.main()

	def save_xml(self):
		root = ElementTree.parse('settings.xml').getroot()
		root.find('workflows').find('workflow1').find('after_capture').text = self.get_after_capture_functions()
		root.find('workflows').find('workflow1').find('after_upload').text = self.get_after_upload_functions()
		root.find('workflows').find('workflow1').find('hotkeys').text = self.get_hotkey()
		f = open("settings.xml", "w")
		f.write(ElementTree.tostring(root))
		f.close()

	def get_after_capture_functions(self):
		function = ""
		if self.edit_option.get_active():
			function = "edit,"
		if self.upload_option.get_active():
			function = function + "upload,"
		return function[:-1]

	def get_after_upload_functions(self):
		function = ""
		if self.copy_link_option.get_active():
			function = function + "copy_link_to_clipboard,"
		return function[:-1]

	def get_hotkey(self):
		return self.hotkey.get_text()[:-1]

if __name__ == "__main__":
	menu = SettingsMenu()
	menu.start()