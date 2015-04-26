#!/usr/bin/env python

# example table.py
from testing import*
from EDIT1 import*
import pygtk
pygtk.require('2.0')
import gtk
from hotkey_selection import hotkey_selection
import filechooser


class Table:
    # Our callback.
    # The data passed to this method is printed to stdout
    def Setting(self, widget, data=None):
        hotkey_selection()

    def show(self, widget, data=None):
        edit()

    # This callback quits the program
    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False
  
    def screenshot(self, widget, event, data=None): 
        screenshot() 
        edit()
        
    def filechooser(self, widget, data=None):
        filechooser.filechooser()

    def keyEvent(self, widget, ev, data=None):
        if ev.keyval == 65307:
            print "QUITTING SCREENSHOT"
            gtk.main_quit()

    def __init__(self):
        # Create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

        # Set the window title
        self.window.set_title("UploadX")
        

        # Set a handler for delete_event that immediately
        # exits GTK.
        self.window.connect("delete_event", self.delete_event)
        self.window.connect("key-press-event", self.keyEvent)

        # Sets the border width of the window.
        self.window.set_border_width(20)

        # Create a 2x2 table
        table = gtk.Table(2, 2, True)

        # Put the table in the main window
        self.window.add(table)

        # Create first button
        button = gtk.Button("Screenshot")

        # When the button is clicked, we call the "callback" method
        # with a pointer to "button 1" as its argument
        button.connect("clicked", self.screenshot, "Screenshot")


        # Insert button 1 into the upper left quadrant of the table
        table.attach(button, 0, 1, 0, 1)

        button.show()

        # Create second button

        button = gtk.Button("Edit")

        # When the button is clicked, we call the "callback" method
        # with a pointer to "button 2" as its argument
        button.connect("clicked", self.show, "Edit")
        # Insert button 2 into the upper right quadrant of the table
        table.attach(button, 1, 2, 0, 1)

        button.show()


        button = gtk.Button("Hotkey Setting")

        button.connect("clicked", self.Setting)
        table.attach(button, 0, 2, 1, 2)
        button.show()


        button = gtk.Button("Local Image")
        # When the button is clicked, we call the "callback" method
        # with a pointer to "button 2" as its argument
        button.connect("clicked", self.filechooser)
        # Insert button 2 into the upper right quadrant of the table
        table.attach(button, 0, 2, 2, 3)

        button.show()

        # Create "Quit" button
        button = gtk.Button("Quit")

        # When the button is clicked, we call the main_quit function
        # and the program exits
        button.connect("clicked", lambda w: gtk.main_quit())
        # Insert the quit button into the both lower quadrants of the table
        table.attach(button, 0, 2, 3, 4)

        button.show()

        table.show()
        self.window.show()

def main():
    gtk.main()
    return 0       

def front_gui():
    Table()
    main()

if __name__ == "__main__":
    # Table()
    # main()
    front_gui()
