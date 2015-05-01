#!/usr/bin/env python

# example statusbar.py

import pygtk
pygtk.require('2.0')
import gtk

class StatusbarExample:
    
    def push_item(self, context_id, text):
        # buff = " Item %d" % self.count
        # self.count = self.count + 1
        # print type(context_id)
        self.status_bar.push(self.context_id, text)
        entry_text = self.entry.get_text()
        print entry_text
        return entry_text

    def pop_item(self, widget, data):
        self.status_bar.pop(data)
        return

    # def enter_callback(self, widget, data):
    #     buff=data
    #     entry_text = self.entry.get_text()
    #     print "Entry contents: %s\n" % entry_text
    #     self.entry.set_text("")
    #     context_id = self.status_bar.get_context_id("Statusbar example")
    #     self.status_bar.push(context_id, buff)

    def __init__(self):
        # self.count = 1
        # create a new window
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_size_request(200, 100)
        window.set_title("PyGTK Statusbar Example")
        window.connect("delete_event", lambda w,e: gtk.main_quit())
 
        vbox = gtk.VBox(False, 1)
        window.add(vbox)
        vbox.show()
          
        self.status_bar = gtk.Statusbar()

        vbox.pack_start(self.status_bar, True, True, 0)
        
        self.status_bar.show()

        # context_id = self.status_bar.get_context_id("Statusbar example")
        self.context_id=self.status_bar.get_context_id("Statusbar example")
        # self.status_bar.push(context_id, buff)

        # button = gtk.Button("push item")
        # button.connect("clicked", self.push_item, context_id)
        # vbox.pack_start(button, True, True, 2)
        # button.show()              

        # button = gtk.Button("pop last item")
        # button.connect("clicked", self.pop_item, context_id)
        # vbox.pack_start(button, True, True, 2)
        # button.show()              
        self.entry = gtk.Entry()
   
        text="Title"
        self.push_item(self.context_id, text)

        text="Description"
        

        self.entry.connect("activate", self.push_item,text)

        # self.entry.select_region(0, len(self.entry.get_text()))
        vbox.pack_start(self.entry, True, True, 0)
        self.entry.show()

        # self.enter_callback("Title")

        # always display the window as the last step so it all splashes on
        # the screen at once.
        window.show()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    StatusbarExample()
    main()