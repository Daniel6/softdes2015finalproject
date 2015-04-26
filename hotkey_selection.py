#!/usr/bin/env python

# example table.py

import pygtk
pygtk.require('2.0')
import gtk
import main1


class Table:
    # Our callback.
    # The data passed to this method is printed to stdout
    # def callback(self, widget, data=None):
    #     print "Hello again - %s was pressed" % data

    # This callback quits the program
    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def __init__(self):
        # Create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

        # Set the window title
        self.window.set_title("Hotkey Selection")

        # Set a handler for delete_event that immediately
        # exits GTK.
        self.window.connect("delete_event", self.delete_event)
        # Sets the border width of the window.
        self.window.set_border_width(20)
        table = gtk.Table(4, 4, True)
        button = gtk.Button("OK")
        button.connect_object("clicked", self.button_press_event, "OK")
        table.attach(button, 3, 4, 4, 5)

#section1-----------------------------------------------
    
        entry = gtk.Entry()
        entry.connect("activate", self.enter_callback, "screenshot_run")
        # Put the table in the main window
        self.window.add(table)
        label = gtk.Label('sreenshot')
        table.attach(label, 0, 1, 0, 1)
        table.attach(entry, 1, 2, 0, 1)
        entry.show()


# #section2-----------------------------------------------



        entry = gtk.Entry()
        entry.connect("activate", self.enter_callback, "screenshot_prep1")
        # Put the table in the main window
        self.window.add(table)
        label = gtk.Label('function2')
        table.attach(label, 2, 3, 0, 1)
        table.attach(entry, 3, 4, 0, 1)
        entry.show()

# #section3-----------------------------------------------
        entry = gtk.Entry()
        entry.connect("activate", self.enter_callback, "screenshot_prep2")
        # Put the table in the main window
        self.window.add(table)
        label = gtk.Label('function3')
        table.attach(label, 0, 1, 1, 2)
        table.attach(entry, 1, 2, 1, 2)
        entry.show()

# #section4-----------------------------------------------
        entry = gtk.Entry()
        entry.connect("activate", self.enter_callback, "stop")
        # Put the table in the main window
        self.window.add(table)
        label = gtk.Label('function4')
        table.attach(label, 2, 3, 1, 2)
        table.attach(entry, 3, 4, 1, 2)
        entry.show()

# #section5-----------------------------------------------
        entry = gtk.Entry()
        entry.connect("activate", self.enter_callback, entry)
        # Put the table in the main window
        self.window.add(table)
        label = gtk.Label('function4')
        table.attach(label, 0, 1, 2, 3)
        table.attach(entry, 1, 2, 2, 3)
        entry.show()

# #section6-----------------------------------------------
        entry = gtk.Entry()
        entry.connect("activate", self.enter_callback, entry)
        # Put the table in the main window
        self.window.add(table)
        label = gtk.Label('function5')
        table.attach(label, 2, 3, 2, 3)
        table.attach(entry, 3, 4, 2, 3)
        entry.show()
        self.window.show_all()

# #section7-----------------------------------------------
        entry = gtk.Entry()
        entry.connect("activate", self.enter_callback, entry)
        # Put the table in the main window
        self.window.add(table)
        label = gtk.Label('function6')
        table.attach(label, 0, 1, 3, 4)
        table.attach(entry, 1, 2, 3, 4)
        entry.show()

# #section8-----------------------------------------------
        entry = gtk.Entry()
        entry.connect("activate", self.enter_callback, entry)
        # Put the table in the main window
        self.window.add(table)
        label = gtk.Label('function6')
        table.attach(label, 2, 3, 3, 4)
        table.attach(entry, 3, 4, 3, 4)
        entry.show()
        self.window.show_all()




#         # Create "Quit" button
#         button = gtk.Button("Quit")
#         # When the button is clicked, we call the main_quit function
#         # and the program exits
#         button.connect("clicked", lambda w: gtk.main_quit())
#         # Insert the quit button into the both lower quadrants of the table
#         table.attach(button, 1, 2, 1, 2)
    def enter_callback(self, entry, mytext):
        print mytext
        entry_text = entry.get_text()
        if mytext=="screenshot_run":
            self.A=entry_text
        if mytext=="screenshot_prep1":
            self.B=entry_text
        if mytext=="screenshot_prep2":
            self.C=entry_text
        if mytext=="stop":
            self.D=entry_text
        print "Entry contents: %s\n" % entry_text
    

    def button_press_event(self, widget, data=None):
        Hotkey=main1.hotkey(self.A, self.B, self.C, self.D)

def main():
    gtk.main()
    return 0       

def hotkey_selection():
    Table()
    main()
if __name__ == "__main__":
    # Table()
    # main()
    hotkey_selection()



    # #Initializing Model, View, Controlller
    # hotkey_model = model()
    # hotkey_view = view(hotkey_model)
    # hotkey_controller = controller(hotkey_model)

    # #Main Loop:
    # while true:
    #     if hotkey_controller.get_user_input():
    #         break
    #     else:
    #         hotkey_view.display()

