import gtk.gdk
from Xlib import display

def mousepos():
	pos = display.Display().screen().root.query_pointer()._data
	return pos["root_x"], pos["root_y"]

w = gtk.gdk.get_default_root_window()

top_left = [100, 100]
bottom_right = mousepos()
size = [bottom_right[0]-top_left[0], bottom_right[1]-top_left[1]]

print "The size of the window is %d x %d" % (size[0], size[1])
pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, False, 8, size[0], size[1])
pb = pb.get_from_drawable(w,w.get_colormap(),top_left[0],top_left[1],0,0,size[0],size[1])
if (pb != None):
    pb.save("screenshot.png","png")
    print "Screenshot saved to screenshot.png."
else:
    print "Unable to get the screenshot."