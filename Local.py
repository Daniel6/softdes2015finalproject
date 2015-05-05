#!/usr/bin/env python

# example filechooser.py

import pygtk
pygtk.require('2.0')
import edit_image
import gtk
from xml.etree import ElementTree
from upload import imgur_Upload, dropbox_Upload, twitter_Upload

def filechooser():
  # Check for new pygtk: this is new class in PyGtk 2.4
  if gtk.pygtk_version < (2,3,90):
     print "PyGtk 2.3.90 or later required for this example"
     raise SystemExit

  dialog = gtk.FileChooserDialog("Open..",
                                 None,
                                 gtk.FILE_CHOOSER_ACTION_OPEN,
                                 (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                  gtk.STOCK_OPEN, gtk.RESPONSE_OK))
  dialog.set_default_response(gtk.RESPONSE_OK)

  filter = gtk.FileFilter()
  filter.set_name("All files")
  filter.add_pattern("*")
  dialog.add_filter(filter)

  filter = gtk.FileFilter()
  filter.set_name("Images")
  filter.add_mime_type("image/png")
  filter.add_mime_type("image/jpeg")
  filter.add_mime_type("image/gif")
  filter.add_pattern("*.png")
  filter.add_pattern("*.jpg")
  filter.add_pattern("*.gif")
  filter.add_pattern("*.tif")
  filter.add_pattern("*.xpm")
  dialog.add_filter(filter)

  response = dialog.run()
  if response == gtk.RESPONSE_OK:
    filename=dialog.get_filename()
    edit_image.edit(filename)
    print'selected:',filename
    destinations=get_destination()
    upload(destinations,filename)

  elif response == gtk.RESPONSE_CANCEL:
    print 'Closed, no files selected'    
  dialog.destroy()


def upload(destinations,filename):
  URL=""
  if "imgur" in destinations:
    URL = imgur_Upload(filename)
  if "dropbox" in destinations:
    URL = dropbox_Upload(filename, "Test")
  if "twitter" in destinations:
    URL = twitter_Upload(filename, "Test")

  clipboard = gtk.clipboard_get()
  clipboard.set_text(URL)
  clipboard.store()

def get_destination():
  settings = ElementTree.parse('settings.xml').getroot()
  subsettings = settings.find('workflows').find('workflow' + "1") #Find sub-branch of settings for this workflow

  try:
    destinations = settings.find('destinations').text.split(',') #Grab destinations from top level settings
  except:
    destinations = ""
  return destinations

