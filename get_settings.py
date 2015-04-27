from xml.etree import ElementTree
from xml.dom import minidom
import sys
sys.path.insert(1, './lib/pyxhook')
import pyxhook
import gtk
import time
from multiprocessing import Process, Queue

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

		self.ctrl_mod = gtk.ToggleButton(label='Ctrl')
		self.shift_mod = gtk.ToggleButton(label='Shift')
		self.alt_mod = gtk.ToggleButton(label='Alt')
		self.hotkey = gtk.Entry(max=10)
		self.add_label1 = gtk.Label(str='+')
		self.add_label2 = gtk.Label(str='+')
		self.add_label3 = gtk.Label(str='+')
		self.hbox.pack_start(self.alt_mod, False, False, 5)
		self.hbox.pack_start(self.add_label1, False, False, 0)
		self.hbox.pack_start(self.ctrl_mod, False, False, 5)
		self.hbox.pack_start(self.add_label2, False, False, 0)
		self.hbox.pack_start(self.shift_mod, False, False, 5)
		self.hbox.pack_start(self.add_label3, False, False, 0)
		self.hbox.pack_start(self.hotkey, False, False, 5)
		self.alt_mod.show()
		self.ctrl_mod.show()
		self.shift_mod.show()
		self.add_label1.show()
		self.add_label2.show()
		self.add_label3.show()
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

		self.window.show()

	def delete_event(self, widget, event):
		root = ElementTree.parse('settings.xml').getroot()
		root.find('workflows').find('workflow1').find('after_capture').text = self.get_after_capture_functions()
		root.find('workflows').find('workflow1').find('after_upload').text = self.get_after_upload_functions()
		root.find('workflows').find('workflow1').find('hotkeys').text = self.get_hotkey()
		self.save_xml(root)
		gtk.main_quit()

	def start(self):
		gtk.main()

	def save_xml(self, root):
		f = open("settings.xml", "w")
		f.write(ElementTree.tostring(root))
		f.close()

	def get_after_capture_functions(self):
		function = ""
		if self.edit_option.get_active():
			function = "edit,"
		if self.upload_option.get_active():
			function = function + "upload,"
		return function

	def get_after_upload_functions(self):
		function = ""
		if self.copy_link_option.get_active():
			function = function + "copy_link_to_clipboard,"
		return function

	def get_hotkey(self):
		hotkey_string = ""
		if self.alt_mod.get_active():
			hotkey_string = "Alt_L+" + hotkey_string
		if self.ctrl_mod.get_active():
			hotkey_string = hotkey_string + "Control_L+"
		if self.shift_mod.get_active():
			hotkey_string = hotkey_string + "Shift_L+"
		hotkey_string = hotkey_string + self.hotkey.get_text()
		return hotkey_string

if __name__ == "__main__":
	prompt = SettingsPrompt()
	prompt.start()