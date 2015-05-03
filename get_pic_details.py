# import pygtk
import sys
sys.path.insert(1, './lib/pyxhook')
import pyxhook
import gtk
import time
from multiprocessing import Process, Queue

class ImageDetailPrompt(object):
	def __init__(self):
		"""Initialize a menu designed to get an image description from the user and store it for later use."""
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_title('Image Details')
		self.window.set_position(gtk.WIN_POS_CENTER)
		self.window.set_size_request(400, 600)
		self.window.connect("delete_event", self.delete_event) #When user presses orange X, quit out of gtk main loop

		self.vbox = gtk.VBox(False, 0)
		self.hbox = gtk.HBox(False, 0)
		self.hbox.size_allocate(gtk.gdk.Rectangle(0, 0, 40, 10))
		self.vbox.pack_start(self.hbox, False, False, 0)
		self.window.add(self.vbox)
		self.vbox.show()
		self.hbox.show()

		self.title = gtk.Entry(max=0)
		self.title.set_text('Title')
		self.title.connect("focus-in-event", self.title_focused)
		self.description = gtk.Entry(max=0)
		self.description.set_text('Description')
		self.description.connect("focus-in-event", self.description_focused)

		self.vbox.pack_start(self.title, False, False, 0)
		self.vbox.pack_start(self.description, False, False, 0)
		self.title.show()
		self.description.show()

		self.ctrl_mod = gtk.ToggleButton(label='Ctrl')
		self.shift_mod = gtk.ToggleButton(label='Shift')
		self.alt_mod = gtk.ToggleButton(label='Alt')
		self.hotkey = gtk.Entry(max=1)
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

		self.window.show()

	def getTitle(self):
		"""Return the current title of the image"""
		return self.title.get_text()

	def getDescription(self):
		"""Return the current description of the image"""
		return self.description.get_text()

	def title_focused(self, widget, event):
		print("Title Focused")
		self.title.select_region(0, len(self.title.get_text()))

	def description_focused(self, widget, event):
		print("Description Focused")
		# self.description.insert_text(self.queue.get(), len(self.description.get_text()))
		self.description.select_region(0, len(self.description.get_text()))

	def delete_event(self, widget, event):
		self.save_hotkey()
		gtk.main_quit()

	def start(self):
		gtk.main()

	def save_hotkey(self):
		

if __name__ == "__main__":

	prompt = ImageDetailPrompt()
	prompt.start()