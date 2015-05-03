#!/usr/bin/env python

# example images.py

import pygtk
pygtk.require('2.0')
import gtk
# import Twitter_API
import SNS_Platform

class sns_selection(object):
    def __init__(self, filename):
        self.filename=filename
        # create the main window, and attach delete_event signal to terminating
        # the application
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.connect("delete_event", self.close_application)
        window.set_border_width(10)
        window.show()

        # a horizontal box to hold the buttons
        self.hbox = gtk.HBox()
        self.hbox.show()
        window.add(self.hbox)

        self.button('twitter.png', "twitter")
        self.button('dropbox.png',"dropbox")
        self.button("imgur.jpg","imgur")
        self.button("qr.png","qr")

    def button(self,file_name, data):
        desired_width = 150
        desired_height = 150
        pixbuf = gtk.gdk.pixbuf_new_from_file(file_name)
        pixbuf = pixbuf.scale_simple(desired_width, desired_height, gtk.gdk.INTERP_BILINEAR)
        image = gtk.image_new_from_pixbuf(pixbuf)
        image.show()
        # a button to contain the image widget
        button = gtk.Button()
        button.add(image)
        button.show()
        self.hbox.pack_start(button)
        if data=="twitter":
            button.connect("clicked", self.button_clicked, "twitter")
        elif data=="dropbox":
            button.connect("clicked", self.button_clicked, "dropbox")
        elif data=="imgur":
            button.connect("clicked", self.button_clicked, "imgur")
        elif data=="qr":
            button.connect("clicked", self.button_clicked, "qr")





    # when invoked (via signal delete_event), terminates the application.
    def close_application(self, widget, event, data=None):
        gtk.main_quit()
        return False

    # is invoked when the button is clicked.  It just prints a message.
    def button_clicked(self, widget, data=None):
        SNS_Platform.Statusbar_Running(data,self.filename)
        print "button %s clicked" % data
        gtk.main_quit()




def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    filename="test.jpg"
    sns_selection(filename)
    main()