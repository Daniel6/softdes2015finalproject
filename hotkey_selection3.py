#!/usr/bin/env python

# example entry.py

import gtk

import sys
sys.path.insert(0, './lib/pyxhook')
import pygtk

import time
import pyxhook
import Queue
# from gi.repository import gtk

# global i
# i=0

q=Queue.Queue()


class Table:
    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def __init__(self):

        hookman = pyxhook.HookManager()
        hookman.KeyDown = self.keyDownEvent #Bind keydown and keyup events
        hookman.HookKeyboard() 
        # hookman.HookMouse()
        hookman.start()


        # Create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

        # Set the window title
        self.window.set_title("Hotkey Selection")

        # Set a handler for delete_event that immediately
        # exits gtk.
        self.window.connect("delete_event", self.delete_event)
        # Sets the border width of the window.
        self.window.set_border_width(20)
        table = gtk.Table(4, 4, True)
        
        entry = gtk.Entry()
        entry.connect("activate", enter_callback,entry)
        self.window.add(table)
        label = gtk.Label('sreenshot')
        table.attach(label, 0, 1, 0, 1)
        table.attach(entry, 1, 2, 0, 1)
        entry.show()

        self.check = gtk.CheckButton("Editable")
        self.check.connect("toggled", self.signal)
        self.check.show()
        table.attach(self.check, 0,1,4,5)

        self.window.add(table)
        self.window.show_all()

    def signal(self, checkbutton):
        print self.check.get_active()
        # time.sleep(0.1)

    def keyDownEvent(self, event):
        # print self.check.get_active()
        if self.check.get_active()=="True":
            q.put(event)
        # time.sleep(0.1)

def enter_callback(entry, event):
    entry_text=q.get()
    print "Entry contents: %s\n" % entry_text
    time.sleep(0.1)

def main():
    gtk.main()
    # time.sleep(0.1)
    return 0       

def hotkey_selection():
    Table()
    main()


if __name__ == "__main__":

    hotkey_selection()



