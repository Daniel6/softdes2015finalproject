import gtk
import time
import sys
sys.path.insert(0, './lib/pyxhook')
import pyxhook
import Image
import Tkinter
from Xlib import display

class ZoneDesignator():
	def __init__(self, bkgrnd):
		self.dragging = False
		self.running = True
		self.bkgrnd = bkgrnd
		self.top_left = []
		self.bottom_right = []
		self.root_window = gtk.gdk.get_default_root_window()
		self.x, self.y, self.width, self.height, self.depth = self.root_window.get_geometry() #Get Geometry of desktop

		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_position(gtk.WIN_POS_CENTER_ON_PARENT)
		self.window.fullscreen()
		self.window.set_title("Test")
		self.window.set_keep_above(True)
		self.window.set_opacity(.2)
		self.window.connect("key-press-event", self.keyEvent)

		self.vbox = gtk.VBox(False, 0)
		self.window.add(self.vbox)
		self.vbox.show()

		self.drawingArea = gtk.DrawingArea()
		self.drawingArea.set_size_request(self.width, self.height)
		self.vbox.pack_start(self.drawingArea, True, True, 0)
		self.drawingArea.show()
		self.drawingArea.connect("configure_event", self.configureEvent)
		self.drawingArea.connect("expose_event", self.exposeEvent)
		self.drawingArea.connect("button_press_event", self.buttonDown)
		self.drawingArea.connect("button_release_event", self.buttonUp)
		self.drawingArea.connect("motion_notify_event", self.mouseMove)
		self.drawingArea.set_events(gtk.gdk.EXPOSURE_MASK
							| gtk.gdk.LEAVE_NOTIFY_MASK
							| gtk.gdk.BUTTON_PRESS_MASK
							| gtk.gdk.BUTTON_RELEASE_MASK
							| gtk.gdk.BUTTON_MOTION_MASK
							| gtk.gdk.POINTER_MOTION_MASK
							| gtk.gdk.POINTER_MOTION_HINT_MASK)

	def start(self):
		self.window.present()
		self.window.show_all()
		gtk.main()

	def exposeEvent(self, widget, ev):
		x , y, width, height = ev.area
		# widget.window.draw_pixbuf(widget.get_style().fg_gc[gtk.STATE_NORMAL], self.bkgrnd, 0, 0, 0, 0)
		widget.window.draw_drawable(widget.get_style().fg_gc[gtk.STATE_NORMAL],
			pixmap, x, y, x, y, width, height)
		if not self.running:
			gtk.main_quit()

	def configureEvent(self, widget, ev):
		global pixmap
		pixmap = gtk.gdk.Pixmap(widget.window, self.width, self.height)
		pixmap.draw_rectangle(widget.get_style().white_gc,
			True, 0, 0, self.width, self.height)

	def keyEvent(self, widget, ev, data=None):
		if ev.keyval == 65307: #Exit when user presses ESC
			gtk.main_quit()
			

	def buttonDown(self, widget, ev):
		if ev.button == 1:
			self.top_left = self.mousepos()
			self.dragging = True

	def mouseMove(self, widget, ev):
		if self.dragging:
			x, y = self.mousepos()
			width = x - self.top_left[0]
			height = y - self.top_left[1]
			rect = (int(self.top_left[0]), int(self.top_left[1]), int(width), int(height))
			pixmap.draw_rectangle(widget.get_style().white_gc, #Draw White background on everything
				True, 0, 0, self.width, self.height)
			pixmap.draw_rectangle(widget.get_style().black_gc, True, rect[0], rect[1], rect[2], rect[3]) #Draw Black Rectangle defined by user
			widget.queue_draw_area(0, 0, self.width, self.height)


	def buttonUp(self, widget, ev):
		if ev.button == 1:
			self.bottom_right = self.mousepos()
			self.dragging = False
			self.running = False
			widget.queue_draw_area(0, 0, self.width, self.height)
			

	def mousepos(self):
		pos = display.Display().screen().root.query_pointer()._data
		return pos["root_x"], pos["root_y"]

class Capturer(object):
	def __init__(self):
		self.root = Tkinter.Tk()
		self.screen_width = self.root.winfo_screenwidth()
		self.screen_height = self.root.winfo_screenheight()

		self.size = [self.screen_width, self.screen_height]

	def capture(self):
		self.pixbuf = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, False, 8, self.size[0], self.size[1])
		self.pixbuf = self.pixbuf.get_from_drawable(gtk.gdk.get_default_root_window(), gtk.gdk.colormap_get_system(), 0,0,0,0,self.size[0],self.size[1])

		self.zoneDesignator = ZoneDesignator(self.pixbuf)

		self.zoneDesignator.start()

		try:
			self.size = [self.zoneDesignator.bottom_right[0]-self.zoneDesignator.top_left[0], self.zoneDesignator.bottom_right[1]-self.zoneDesignator.top_left[1]]
		except IndexError:
			sys.exit()

		self.screenie = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, False, 8, self.size[0], self.size[1])
		self.pixbuf.copy_area(self.zoneDesignator.top_left[0], self.zoneDesignator.top_left[1], self.size[0], self.size[1], self.screenie, 0, 0)
		self.screenie.save("screenshot.png","png")

if __name__ == "__main__":
	myCapturer = Capturer()
	myCapturer.capture()