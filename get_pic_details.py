# import pygtk
import sys
sys.path.insert(1, './lib/pyxhook')
import pyxhook
import gtk
import time
from multiprocessing import Process

class ImageDetailPrompt(object):
	def __init__(self):
		self.hookman = pyxhook.HookManager()
		self.hookman.KeyDown = self.keyDownEvent #Bind keydown and keyup events
		self.hookman.KeyUp = self.keyUpEvent
		self.hookman.HookKeyboard()
		self.hookman.start()


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
		self.hookman.cancel() #Close listener when done
		gtk.main_quit()

	def start(self):
		gtk.main()

	def keyUpEvent(self, event):
		print(event.Key)

	def keyDownEvent(self, event):
		print(event.Key)
		if self.title.has_focus():
			self.title.insert_text(event.Key, len(self.title.get_text()))

def gui_target():
	prompt = ImageDetailPrompt()
	prompt.start()

if __name__ == "__main__":
	gui_process = Process(target=gui_target)