# import pygtk
import gtk
import time

class ImageDetailPrompt(object):
	def __init__(self):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_title('Image Details')
		self.window.set_position(gtk.WIN_POS_CENTER)
		self.window.set_size_request(200, 100)
		self.window.connect("delete_event", self.delete_event) #When user presses orange X, quit out of gtk main loop

		self.vbox = gtk.VBox(False, 0)
		self.window.add(self.vbox)
		self.vbox.show()

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

		self.window.show()

	def getTitle(self):
		return self.title.get_text()

	def getDescription(self):
		return self.description.get_text()

	def title_focused(self, widget, event):
		print("Title Focused")
		self.title.select_region(0, len(self.title.get_text()))

	def description_focused(self, widget, event):
		print("Description Focused")
		self.description.select_region(0, len(self.description.get_text()))

	def delete_event(self, widget, event):
		gtk.main_quit()

	def start(self):
		gtk.main()

prompt = ImageDetailPrompt()
prompt.start()