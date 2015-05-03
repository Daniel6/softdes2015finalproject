#!/usr/bin/env python

# example images.py
import sys
import pygtk
pygtk.require('2.0')
import gtk
# import Queue


class format_selection(object):
    def __init__(self):
        self.choose_format=None
        # self.q=Queue.Queue()
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
        self.button('jpeg_icon.png', "jpeg")
        self.button('png_icon.png',"png")
        # print "3"
        # format=self.q.get()
        # print format
        # print 4
        # return format

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
        if data=="jpeg":
            button.connect("clicked", self.button_clicked, "jpeg")
        elif data=="png":
            button.connect("clicked", self.button_clicked, "png")
        # return format


    # when invoked (via signal delete_event), terminates the application.
    def close_application(self, widget, event, data=None):
        gtk.main_quit()
        return False

    # is invoked when the button is clicked.  It just prints a message.
    def button_clicked(self, widget, data=None):
        if data=="jpeg":
            self.choose_format= "jpeg"
        elif data=="png":
            self.choose_format= "png"
        if self.choose_format=="jpeg" or "png":
            gtk.main_quit()
        # self.q.put(self.choose_format)
        # return self.choose_format


def format_selection_running():
    selection=format_selection()
    # if selection=="jpeg" or "png":
    #     sys.exit()
    main()
    return selection.choose_format

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    print format_selection_running()