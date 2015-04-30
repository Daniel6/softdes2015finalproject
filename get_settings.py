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

class SettingsPrompt(object):
	def __init__(self):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_title('Workflow Settings')
		self.window.set_position(gtk.WIN_POS_CENTER)
		self.window.set_size_request(400, 300)
		self.window.connect("delete_event", self.delete_event) #When user presses orange X, quit out of gtk main loop

		self.vbox = gtk.VBox(False, 0)
		self.hbox = gtk.HBox(False, 0)
		# self.hbox.size_allocate(gtk.gdk.Rectangle(0, 0, 40, 10))
		self.hotkey_label = gtk.Label(str='Set Hotkey')
		self.vbox.pack_start(self.hotkey_label, False, False, 2)
		self.hotkey_label.show()
		self.vbox.pack_start(self.hbox, False, False, 0)
		self.window.add(self.vbox)
		self.vbox.show()
		self.hbox.show()

		self.hotkey = gtk.Entry(max=0)
		self.hotkey.connect('focus-in-event', self.startListening)
		self.hotkey.set_editable(False)
		self.hbox.pack_start(self.hotkey, False, False, 5)
		self.hotkey.show()

		self.after_capture_label = gtk.Label(str='What to do after capturing image')
		self.upload_option = gtk.ToggleButton(label='Upload')
		self.edit_option = gtk.ToggleButton(label='Edit')
		self.after_upload_label = gtk.Label(str='What to do after uploading image')
		self.copy_link_option = gtk.ToggleButton(label='Copy link to clipboard')

		self.after_capture_box = gtk.HBox(False, 0)
		self.after_capture_box.pack_start(self.upload_option, False, False, 0)
		self.after_capture_box.pack_start(self.edit_option, False, False, 0)

		self.after_upload_box = gtk.HBox(False, 0)
		self.after_upload_box.pack_start(self.copy_link_option, False, False, 0)

		self.vbox.pack_start(self.after_capture_label, False, False, 2)
		self.vbox.pack_start(self.after_capture_box, False, False, 0)
		self.vbox.pack_start(self.after_upload_label, False, False, 2)
		self.vbox.pack_start(self.after_upload_box, False, False, 0)

		self.after_upload_box.show()
		self.after_capture_box.show()
		self.after_capture_label.show()
		self.upload_option.show()
		self.edit_option.show()
		self.after_upload_label.show()
		self.copy_link_option.show()

		self.save_button = gtk.Button(label='Save')
		self.save_button.connect('button-press-event', self.save_button_pressed)
		self.vbox.pack_end(self.save_button, False, False, 2)
		self.save_button.show()
		self.window.show()
		self.startListener()
		self.count = 0

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

	def startListener(self):
		#Open listener in new process
		self.listener_process = subprocess.Popen(["/usr/bin/python2.7", "./listener.py"], stdout = subprocess.PIPE, stderr = subprocess.STDOUT, bufsize=1)
		self.stdout_queue = Queue.Queue()
		self.stdout_reader = asynchronous_file_reader.AsynchronousFileReader(self.listener_process.stdout, self.stdout_queue)
		self.stdout_reader.start()

	def save_button_pressed(self, widget, event):
		self.save_xml()

	def delete_event(self, widget, event):
		os.system("pkill python -15")
		gtk.main_quit()

	def start(self):
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
	prompt = SettingsPrompt()
	prompt.start()