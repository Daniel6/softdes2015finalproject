#!/usr/bin/env python

# example table.py

import pygtk
pygtk.require('2.0')
import gtk
import main1
import pyxhook
import Queue
import time
global i
i=0

q=Queue.Queue()

class Model(object):
    def __init__(self):

        self.controlller=Controlller()
        self.window=self.create_window("Hotkey Selection", 20)
        self.table = self.create_table(5,5)
        self.window.add(self.table)

        self.create_button("ok", 3, 4, 4, 5)
        self.create_text_entry('sreenshot', 0, 1, 0, 1)
        self.create_text_entry("prep1", 2, 3, 0, 1)
        self.create_text_entry("prep2", 0, 1, 1, 2)
        self.create_text_entry("stop", 2, 3, 1, 2)

        self.create_text_entry("func5", 0, 1, 2, 3)
        self.create_text_entry("func6", 2, 3, 2, 3)
        self.create_text_entry("func7", 0, 1, 3, 4)
        self.create_text_entry("func8", 2, 3, 3, 4)

        self.check = gtk.CheckButton("Editable")
        self.check.connect("toggled", self.signal)
        self.check.show()
        self.add_to_table(self.check, 0,1,4,5)

        self.window.show_all()

        hookman = pyxhook.HookManager()
        hookman.KeyDown = self.keyDownEvent #Bind keydown and keyup events
        hookman.HookKeyboard() 
        # hookman.HookMouse()
        # watch for all mouse events
        # hookman.MouseAllButtonsDown = mouse_event
        # hookman.MouseAllButtonsUp = mouse_event 
        hookman.start()
    # def keyDownEvent(event):
    #     print event.ScanCode 
    #     return event.ScanCode


    def signal(self, checkbutton):
        global i
        print self.check.get_active()
        if self.check.get_active()=="True":
            i=1
        else:
            i=0

    def create_window(self, title, border):
        # Create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        # Set the window title
        self.window.set_title(title)
        # Set a handler for delete_event that immediately
        # exits GTK.
        self.window.connect("delete_event", self.controlller.delete_event)
        # Sets the border width of the window.
        self.window.set_border_width(border)
        return self.window

    def create_table(self, w,h):
        self.table = gtk.Table(w, h, True)
        return self.table

    def add_to_table(self, element, a, b, c, d):
        self.table.attach(element, a, b, c, d)

    def create_button(self,text_name,a,b,c,d):
        self.button = gtk.Button(text_name)
        self.button.connect_object("clicked", self.controlller.button_press_event, text_name)
        self.add_to_table(self.button, a,b,c,d)

    def create_text_entry(self,text_name, a, b, c, d):
        
        self.entry = gtk.Entry()
        self.entry.connect("activate", self.controlller.enter_callback, text_name)
        # Put the table in the main window
        self.label = gtk.Label(text_name)
        self.add_to_table(self.label, a, b, c, d)
        self.add_to_table(self.entry, a+1, b+1, c, d)
        # sef.entry.connect
    def keyDownEvent(event):
        global i
        message=event.Key
        print "1:",message
        if i==1: 
            print "i:",i
            print "message:",message
            q.put(message)

# def mouse_event(event):
#     global i
#     if event=="mouse left down":
#         i+=1
#     if event=="mouse left up":
#         i+=1





class Controlller(object):
    """docstring for ClassName"""
    def __init__(self):
        # This callback quits the program
        self.A, self.B, self.C, self.D=1,2,3,4
    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False
    def enter_callback(self, entry, mytext):
        # if not q.empty():
        #     entry_text=q.get()
        # else:
        #     raise Exception("No Input meesage")
        #     raise SystemExit
        if not q.empty():
            # print ("No Input meesage")
            # time.sleep(1)
            entry_text=q.get()
        else: 
            entry_text=None

        # entry_text = entry.get_text()
        if mytext=="screenshot_run":
            self.A=entry_text
        if mytext=="screenshot_prep1":
            self.B=entry_text
        if mytext=="screenshot_prep2":
            self.C=entry_text
        if mytext=="stop":
            self.D=entry_text
        print"+++++++"
        print "Entry contents: %s\n" % entry_text
        print"---------"
        print mytext   

    def button_press_event(self, widget, data=None):
        Hotkey=main1.hotkey(self.A, self.B, self.C, self.D)
        

def main():
    gtk.main()
    return 0       

if __name__ == "__main__":

    #Initializing Model, View, Controlller
    hotkey_model = Model()
    main()
 