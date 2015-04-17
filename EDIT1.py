import gtk
from COLOR_CIRCLE1 import *
# Backing pixmap for drawing area
pixmap = None
x1 = None
y1 = None
# Create a new backing pixmap of the appropriate size



class ScaleImage(object):
    def __init__(self):
        self.pixmap=pixmap
        self.temp_height = 0
        self.temp_width = 0

        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_resizable(False)
        # window.connect("key-press-event", self.keyEvent)
        window.connect("delete_event", self.delete_event)
        image = gtk.Image()
        image.set_from_file('screenshot.png')
        self.pixbuf = image.get_pixbuf()
        image.connect('expose-event', self.on_image_resize, window)  
        window.set_size_request(self.pixbuf.get_width(), self.pixbuf.get_height())
        window.set_keep_above(True)
        self.color_selected_object=ColorSelectionExample()

#-------------------------------------------------------------------------------------------------------    


      # Create the drawing areadrawing_area
        drawing_area = gtk.DrawingArea()
        drawing_area.set_size_request(self.pixbuf.get_width(), self.pixbuf.get_height())
        window.add(drawing_area)
        drawing_area.show()

        # Signals used to handle backing pixmap
        drawing_area.connect("expose_event", self.expose_event)
        drawing_area.connect("configure_event", self.configure_event)

        # Event signals
        drawing_area.connect("motion_notify_event", self.motion_notify_event)
        drawing_area.connect("button_press_event", self.button_press_event) 
        drawing_area.set_events(gtk.gdk.EXPOSURE_MASK
                                | gtk.gdk.LEAVE_NOTIFY_MASK
                                | gtk.gdk.BUTTON_PRESS_MASK
                                | gtk.gdk.POINTER_MOTION_MASK
                                | gtk.gdk.POINTER_MOTION_HINT_MASK)



#---------------------------------------------------------------------------------------------------------
        window.show_all()        

    def on_image_resize(self, widget, event, window):
        allocation = widget.get_allocation()
        if self.temp_height != allocation.height or self.temp_width != allocation.width:
            self.temp_height = allocation.height
            self.temp_width = allocation.width
            pixbuf = self.pixbuf.scale_simple(allocation.width, allocation.height, gtk.gdk.INTERP_BILINEAR)
            widget.set_from_pixbuf(pixbuf)

    def close_application(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def configure_event(self,widget, event):
        global pixmap

        x, y, width, height = widget.get_allocation()
        self.pixmap = gtk.gdk.Pixmap(widget.window, width, height)
        self.pixmap.draw_rectangle(widget.get_style().white_gc,
                              True, 0, 0, width, height)
        pixbuf = gtk.gdk.pixbuf_new_from_file("screenshot.png") #one way to load a pixbuf
        self.pixmap.draw_pixbuf(None, pixbuf, 0, 0, x, y, -1, -1, gtk.gdk.RGB_DITHER_NONE, 0, 0)
       
        return True

    # Redraw the screen from the backing pixmap
    def expose_event(self, widget, event):
        x , y, width, height = event.area
        widget.window.draw_drawable(widget.get_style().fg_gc[gtk.STATE_NORMAL], self.pixmap, x, y, x, y, width, height)
        return False

    #Draw a rectangle on the screen
    def draw_brush(self, widget, x, y):
        global x1
        global y1
        x = int(x)
        y = int(y)
        gc = widget.get_style().black_gc
        # color=gtk.gdk.Color(red=65535, green=0, blue=0)
        gc.set_rgb_fg_color(self.selected_color)

        if x1 != None and y1 != None:
            self.pixmap.draw_lines(gc,((x1, y1), (x, y)))
            gc.set_line_attributes(10,gtk.gdk.LINE_SOLID,gtk.gdk.CAP_ROUND,gtk.gdk.JOIN_ROUND)

            widget.queue_draw_area(0, 0, widget.allocation.width, widget.allocation.height)
        x1 = x
        y1 = y

        # self.save_image(widget)
        # pixbuf1 = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, has_alpha=False, bits_per_sample=8, width=widget.allocation.width, height=widget.allocation.height)
        # pixbuf1.get_from_drawable(self.pixmap, self.pixmap.get_colormap(), 0, 0, 0, 0, widget.allocation.width, widget.allocation.height)
        # pixbuf1.save("SCREENSHOT", "jpeg", {"quality":"100"})


    def button_press_event(self, widget, event):
        
        self.selected_color=self.color_selected_object.color
        if event.button == 3:
            self.save_image(widget)
        elif event.button == 1 and self.pixmap != None:
            self.draw_brush(widget, event.x, event.y)
        return True

    def motion_notify_event(self, widget, event):
        if event.is_hint:
            x, y, state = event.window.get_pointer()
        else:
            x = event.x
            y = event.y
            state = event.state
        
        if state & gtk.gdk.BUTTON1_MASK and self.pixmap != None:
            self.selected_color=self.color_selected_object.color
            self.draw_brush(widget, x, y)
                    
        return True

    def save_image(self, widget):
        # widget=self.widget
        print("Save Image")
        pixbuf1 = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, has_alpha=False, bits_per_sample=8, width=widget.allocation.width, height=widget.allocation.height)
        pixbuf1.get_from_drawable(self.pixmap, self.pixmap.get_colormap(), 0, 0, 0, 0, widget.allocation.width, widget.allocation.height)
        pixbuf1.save("SCREENSHOT", "jpeg", {"quality":"100"})

    # def keyEvent(widget, ev, data=None):
    #     if ev.keyval == 65307:
    #         print "QUITTING SCREENSHOT"
    #         gtk.main_quit()
    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False


def edit():
    ScaleImage()
    gtk.main()

if __name__ == "__main__":
    ScaleImage()
    gtk.main()