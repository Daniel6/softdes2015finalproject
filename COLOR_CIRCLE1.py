#!/usr/bin/env python

# example colorsel.py

import pygtk
pygtk.require('2.0')
import gtk
        
class ColorSelectionExample:
    def __init__(self):
        self.colorseldlg = None
        # Create toplevel window, set title and policies
        self. window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self. window.set_title("Click Here for Choosing Colors")
        self. window.set_resizable(True)

        # Attach to the "delete" and "destroy" events so we can exit
        self. window.connect("delete_event", self.destroy_window)
    # def draw():
        # Create drawingarea, set size and catch button events
        self.drawingarea = gtk.DrawingArea()

        self.color = self.drawingarea.get_colormap().alloc_color(0, 65535, 0)
        self.drawingarea.set_size_request(200, 200)
        self.drawingarea.set_events(gtk.gdk.BUTTON_PRESS_MASK)
        self.drawingarea.connect("event",  self.area_event)
        # Add drawingarea to window, then show them both
        self. window.add(self.drawingarea)
        # self.window.connect("key-press-event", self. keyEvent)
        self.drawingarea.show()
        self. window.show()

    # Color changed handler
    def color_changed_cb(self, widget):
        # Get drawingarea colormap
        colormap = self.drawingarea.get_colormap()

        # Get current color
        self.color = self.colorseldlg.colorsel.get_current_color()
        # global selected_color
        # selected_color=color

        # Set window background color
        self.drawingarea.modify_bg(gtk.STATE_NORMAL, self.color)

        

    # Drawingarea event handler
    def area_event(self, widget, event):
        handled = False

        # Check if we've received a button pressed event
        if event.type == gtk.gdk.BUTTON_PRESS:
            handled = True

            # Create color selection dialog
            if self.colorseldlg == None:
                self.colorseldlg = gtk.ColorSelectionDialog(
                    "Select background color")

            # Get the ColorSelection widget
            colorsel = self.colorseldlg.colorsel

            colorsel.set_previous_color(self.color)
            colorsel.set_current_color(self.color)
            colorsel.set_has_palette(True)

            # Connect to the "color_changed" signal
            colorsel.connect("color_changed", self.color_changed_cb)

            # Show the dialog
            response = self.colorseldlg.run()

            if response -- gtk.RESPONSE_OK:
                self.color = colorsel.get_current_color()

            else:
                self.drawingarea.modify_bg(gtk.STATE_NORMAL, self.color)
                
            self.colorseldlg.hide()
        return handled

    # Close down and exit handler
    def destroy_window(self, widget, event):
        gtk.main_quit()
        return False

# def keyEvent(widget, ev, data=None):
#     if ev.keyval == 65307:
#         print "QUITTING SCREENSHOT"
#         gtk.main_quit

        
def main():
    gtk.main()
    return 0

# def color_circle():
#     ColorSelectionExample()
#     ColorSelectionExample().selected_color()
#     main()
#     return selected_color
    
if __name__ == "__main__":
    ColorSelectionExample()
    # ColorSelectionExample().selected_color()
    main()