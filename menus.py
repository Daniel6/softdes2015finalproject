from xml.etree import ElementTree
from xml.dom import minidom
import sys
import os
sys.path.insert(1, './lib')
import asynchronous_file_reader
import gtk
import time
import Queue
import subprocess
import dropbox
import tweetpony

class MainMenu(object):
	def __init__(self):
		"""Define sub-menus and set up window and buttons"""
		self.destinationsMenu = DestinationsMenu()

		self.init_Window()
		self.init_Buttons()

	def init_Buttons(self):
		"""Set up all buttons on main menu"""
		self.settings_button = gtk.Button(label='Settings')
		self.destination_button = gtk.Button(label='Destinations')
		self.man_capture_button = gtk.Button(label='Capture')
		self.man_edit_button = gtk.Button(label='Edit Image')

		self.settings_button.connect('button-press-event', self.openSettings)
		self.destination_button.connect('button-press-event', self.openDestinations)
		self.man_capture_button.connect('button-press-event', self.manCapture)
		self.man_edit_button.connect('button-press-event', self.manEdit)

		self.vbox.pack_start(self.settings_button, False, False, 1)
		self.vbox.pack_start(self.destination_button, False, False, 1)
		self.hbox = gtk.HBox(False, 0)
		self.hbox.pack_start(self.man_capture_button, True, True, 0)
		self.hbox.pack_start(self.man_edit_button, True, True, 0)
		self.vbox.pack_start(self.hbox)

		self.settings_button.show()
		self.destination_button.show()
		self.man_capture_button.show()
		self.man_edit_button.show()
		self.hbox.show()

	def openSettings(self, widget, event):
		"""Open the settings menu"""
		self.settingsMenu.start()

	def openDestinations(self, widget, event):
		"""Open the destinations menu"""
		self.destinationsMenu.start()

	def manCapture(self, widget, event):
		"""Manually call the capture script"""
		subprocess.call(["/usr/bin/python2.7", "./capture.py"])

	def manEdit(self, widget, event):
		"""Manually call the edit script"""
		pass

	def init_Window(self):
		"""Set up window"""
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_title('Main Menu')
		self.window.set_position(gtk.WIN_POS_CENTER)
		self.window.set_size_request(300, 200)
		self.window.connect("delete_event", self.delete_event) #When user presses orange X, quit out of gtk main loop
		self.vbox = gtk.VBox(False, 0)
		self.window.add(self.vbox)

		self.vbox.show()

	def start(self):
		"""Display window and start processes"""
		self.window.show()
		self.startListener()
		gtk.main()

	def startListener(self):
		"""Start pyxhook listener in another process and catch all output from that process"""
		#Open listener in new process
		print("Started Listener")
		self.listener_process = subprocess.Popen(["/usr/bin/python2.7", "./listener.py"], stdout = subprocess.PIPE, stderr = subprocess.STDOUT, bufsize=1)
		self.stdout_queue = Queue.Queue()
		self.stdout_reader = asynchronous_file_reader.AsynchronousFileReader(self.listener_process.stdout, self.stdout_queue)
		self.stdout_reader.start()
		self.settingsMenu = SettingsMenu(self.stdout_reader, self.stdout_queue)

	def delete_event(self, widget, event):
		"""Kill listener process and stop gtk.main() loop"""
		print("Listener Stopped")
		os.system("pkill python -15")
		gtk.main_quit()

class SettingsMenu(object):
	def __init__(self, stdout_reader, stdout_queue):
		"""Initialize all input fields and get reference to listener process"""
		self.init_listener(stdout_reader, stdout_queue)
		self.init_Window()
		self.init_HotkeySettings()
		self.init_AfterCaptureSettings()
		self.init_AfterUploadSettings()
		self.init_SaveButton()

	def init_listener(self, stdout_reader, stdout_queue):
		"""Hook into listener process output"""
		self.stdout_reader = stdout_reader
		self.stdout_queue = stdout_queue
		self.count = 0

	def init_Window(self):
		"""Set up window properties"""
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_title('Workflow Settings')
		self.window.set_position(gtk.WIN_POS_CENTER)
		self.window.set_size_request(400, 300)
		self.window.connect("delete_event", self.delete_event) #When user presses orange X, quit out of gtk main loop
		self.vbox = gtk.VBox(False, 0)
		self.window.add(self.vbox)

		self.vbox.show()

	def init_HotkeySettings(self):
		"""Initialize hotkey input field"""
		self.hotkey_label = gtk.Label(str='Set Hotkey')
		self.vbox.pack_start(self.hotkey_label, False, False, 2)

		self.hbox = gtk.HBox(False, 0)
		self.hotkey = gtk.Entry(max=0)
		self.hotkey.connect('focus-in-event', self.startListening)
		self.hotkey.set_editable(False)
		self.hbox.pack_start(self.hotkey, False, False, 5)
		self.vbox.pack_start(self.hbox, False, False, 0)

		self.hbox.show()
		self.hotkey_label.show()
		self.hotkey.show()

	def init_AfterCaptureSettings(self):
		"""Initialize After Capture input field"""
		self.after_capture_box = gtk.HBox(False, 0)
		self.after_capture_label = gtk.Label(str='What to do after capturing image')
		self.vbox.pack_start(self.after_capture_label, False, False, 2)

		self.upload_option = gtk.ToggleButton(label='Upload')
		self.edit_option = gtk.ToggleButton(label='Edit')
		self.after_capture_box.pack_start(self.upload_option, False, False, 0)
		self.after_capture_box.pack_start(self.edit_option, False, False, 0)
		self.vbox.pack_start(self.after_capture_box, False, False, 0)
		
		self.after_capture_label.show()
		self.upload_option.show()
		self.edit_option.show()
		self.after_capture_box.show()

	def init_AfterUploadSettings(self):
		"""Initialize After Upload input field"""
		self.after_upload_box = gtk.HBox(False, 0)
		self.after_upload_label = gtk.Label(str='What to do after uploading image')
		self.vbox.pack_start(self.after_upload_label, False, False, 2)

		self.copy_link_option = gtk.ToggleButton(label='Copy link to clipboard')
		self.generate_code_option = gtk.ToggleButton(label='Generate QR Code')
		self.after_upload_box.pack_start(self.copy_link_option, False, False, 0)
		self.after_upload_box.pack_start(self.generate_code_option, False, False, 0)
		self.vbox.pack_start(self.after_upload_box, False, False, 0)

		self.after_upload_label.show()
		self.copy_link_option.show()
		self.generate_code_option.show()
		self.after_upload_box.show()

	def init_SaveButton(self):
		"""Create save button"""
		self.save_button = gtk.Button(label='Save')
		self.save_button.connect('button-press-event', self.save_button_pressed)
		self.vbox.pack_end(self.save_button, False, False, 2)
		self.save_button.show()

	def startListening(self, widget, event):
		"""Begin listening to key presses, 
		   the first time this is run ignore the first 3 outputs from
		   the listener process """
		self.hotkey.set_text("")
		self.save_xml()
		running = True
		while not self.stdout_reader.eof():

			while not self.stdout_queue.empty():
				self.count += 1
				out = (self.stdout_queue.get())
				if out == "Return\n":
					running = False
					break
				if self.count > 3: #Ignore first three messages
					print(out.rstrip())
					self.hotkey.set_text(self.hotkey.get_text() + out.rstrip() + "+")
				
			if not running:
				break
			time.sleep(.02)

		self.count = 3 #Reset to 3 instead of 0 so that we don't ignore the first three outputs next time

	def save_button_pressed(self, widget, event):
		"""When save button is pressed, save settings to xml"""
		self.save_xml()

	def delete_event(self, widget, event):
		"""When user exits window, hide the window instead of destroying it"""
		self.window.hide()
		return True

	def start(self):
		"""Unhide the window and resume gtk.main() loop"""
		self.window.show()
		gtk.main()

	def save_xml(self):
		"""Load current settings.xml, make edits, save as new xml"""
		root = ElementTree.parse('settings.xml').getroot()
		root.find('workflows').find('workflow1').find('after_capture').text = self.get_after_capture_functions()
		root.find('workflows').find('workflow1').find('after_upload').text = self.get_after_upload_functions()
		root.find('workflows').find('workflow1').find('hotkeys').text = self.get_hotkey()
		f = open("settings.xml", "w")
		f.write(ElementTree.tostring(root))
		f.close()

	def get_after_capture_functions(self):
		"""Get desired functions from the buttons that are currently pressed on the menu"""
		function = ""
		if self.edit_option.get_active():
			function = "edit,"
		if self.upload_option.get_active():
			function = function + "upload,"
		return function[:-1]

	def get_after_upload_functions(self):
		"""Get desired functions from the buttons that are currently pressed on the menu"""
		function = ""
		if self.copy_link_option.get_active():
			function = function + "copy_link_to_clipboard,"
		if self.generate_code_option.get_active():
			function = function + "generate_qr_code,"
		return function[:-1]

	def get_hotkey(self):
		"""Read the hotkey field and trim the last character"""
		return self.hotkey.get_text()[:-1]

class DestinationsMenu(object):
	def __init__(self):
		"""Initialize window and buttons"""
		self.init_Window()
		self.init_Buttons()
		self.dropboxAuth = AuthenticationMenu("dropbox")
		self.twitterAuth = AuthenticationMenu("twitter")

	def start(self):
		"""Show the window and resume the gtk.main() loop"""
		self.window.show()
		gtk.main()

	def init_Window(self):
		"""Initialize window properties"""
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.connect("delete_event", self.delete_event)
		self.window.set_title('Choose Destination')
		self.window.set_position(gtk.WIN_POS_CENTER)
		self.hbox = gtk.HBox()
		self.window.add(self.hbox)
		self.window.set_border_width(10)
		self.hbox.show()

	def init_Buttons(self):
		"""Initialize buttons representing destinations"""
		self.icon_width = 150
		self.icon_height = 150

		self.imgur_Button = self.makeButton(self.icon_width, self.icon_height, "./res/imgur.jpg")

		self.twitter_box = gtk.VBox()
		self.twitter_Button = self.makeButton(self.icon_width, self.icon_height, "./res/twitter.png")
		self.twitter_Reset = gtk.Button(label='Reset')
		self.twitter_Reset.connect('button-press-event', self.reset, "twitter")
		self.twitter_box.pack_start(self.twitter_Button, False, False, 1)
		self.twitter_box.pack_start(self.twitter_Reset, False, False, 1)

		self.dropbox_box = gtk.VBox()
		self.dropbox_Button = self.makeButton(self.icon_width, self.icon_height, "./res/dropbox.png")
		self.dropbox_Reset = gtk.Button(label='Reset')
		self.dropbox_Reset.connect('button-press-event', self.reset, "dropbox")
		self.dropbox_box.pack_start(self.dropbox_Button, False, False, 1)
		self.dropbox_box.pack_start(self.dropbox_Reset, False, False, 1)

		self.hbox.pack_start(self.imgur_Button, False, False, 1)
		self.hbox.pack_start(self.twitter_box, False, False, 1)
		self.hbox.pack_start(self.dropbox_box, False, False, 1)

		self.imgur_Button.connect("button-press-event", self.selectDest, "imgur")
		self.twitter_Button.connect("button-press-event", self.selectDest, "twitter")
		self.dropbox_Button.connect("button-press-event", self.selectDest, "dropbox")

		self.imgur_Button.show()
		self.twitter_box.show()
		self.twitter_Button.show()
		self.twitter_Reset.show()
		self.dropbox_box.show()
		self.dropbox_Button.show()
		self.dropbox_Reset.show()

	def makeButton(self, width, height, file_name):
		"""Given dimensions and an image, return a button with the icon of the given image"""
		desired_width = width
		desired_height = height
		pixbuf = gtk.gdk.pixbuf_new_from_file(file_name)
		pixbuf = pixbuf.scale_simple(desired_width, desired_height, gtk.gdk.INTERP_BILINEAR)
		icon = gtk.image_new_from_pixbuf(pixbuf)
		icon.show()
		button = gtk.ToggleButton()
		button.add(icon)

		return button

	def reset(self, widget, event, dest):
		"""Reset the auth info for a destination"""
		root = ElementTree.parse('settings.xml').getroot()
		subsettings = root.find('authentication')
		if dest == "twitter":
			section = subsettings.find('twitter')
			section.find('access_token').text = ""
			section.find('access_token_secret').text = ""
		elif dest == "dropbox":
			section = subsettings.find('dropbox')
			section.find('access_token').text = ""

		self.savexml(root)

	def savexml(self, root):
		f = open("settings.xml", "w")
		f.write(ElementTree.tostring(root))
		f.close()

	def selectDest(self, widget, event, dest):
		if dest=="dropbox":
			if not self.dropboxAuth.check_authentication()[0]:
				self.dropboxAuth.start()
		elif dest=="twitter":
			if not self.twitterAuth.check_authentication()[0]:
				self.twitterAuth.start()

	def saveDest(self):
		"""Set the destination field of settings.xml to the chosen value"""
		root = ElementTree.parse('settings.xml').getroot()
		dest = ""
		if self.imgur_Button.get_active():
			dest = dest + "imgur,"
		if self.twitter_Button.get_active():
			dest = dest + "twitter,"
		if self.dropbox_Button.get_active():
			dest = dest + "dropbox,"

		root.find('destinations').text = dest[:-1]
		self.savexml(root)

	def delete_event(self, widget, event):
		"""Hide the window instead of destroying it"""
		self.saveDest()
		self.window.hide()
		gtk.main_quit()
		return True

class AuthenticationMenu(object):
	def __init__(self, media):
		self.media=media
		
		self.Initilize_Register()
		# create a new window
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_position(gtk.WIN_POS_CENTER)
		self.window.set_size_request(300, 230)
		self.window.set_title("UploadX SNS Platform")
		self.window.connect("delete_event", lambda w,e: gtk.main_quit())
 
		self.vbox = gtk.VBox(False, 1)
		self.window.add(self.vbox)
		
		self.button1 = gtk.Button('Copy Authentication URL to Clipboard')
		self.button1.show()
		self.button1.connect('clicked', self.set_clipboard)
		self.clipboard = gtk.clipboard_get(gtk.gdk.SELECTION_CLIPBOARD)
		self.textview = gtk.TextView()
		self.textbuffer = self.textview.get_buffer()
		self.vbox.pack_start(self.button1, False,False, 0)


		self.status_bar = gtk.Statusbar()
		self.vbox.pack_start(self.status_bar, False,False, 0)
		self.context_id=self.status_bar.get_context_id("Statusbar example")
		
		self.entry1 = gtk.Entry()
		self.text="Paste Authentication Code"
		# self.text="https://api.twitter.com/oauth/authenticate?oauth_token=n1QQ8LYDZS7XWibBaz18zdk13oYuF5jI"
		self.vbox.pack_start(self.entry1,  False,False, 0)

		self.create_button("ok")

	def start(self):
		self.window.show_all()
		gtk.main()

	def Initilize_Register(self):
		
		if self.media=="twitter":
		
			consumer_key='ilsxfHf2M9WVFod3I0hOPlqlJ'
			consumer_secret= 'PD4gKHDVujDaDiMVkK678BVHoAXtYf4bXpEdZoM9dyLAIZ9xVB'
			self.api = tweetpony.API(consumer_key = consumer_key, consumer_secret = consumer_secret)
			self.auth_url = self.api.get_auth_url()
		
		elif self.media=="dropbox":
			app_key = 'uehmy7qwfyhnd34'
			app_secret = 'h1tmocr962j6xfa'        
			self.flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

	def create_button(self,text_name):
		self.button = gtk.Button(text_name)
		self.button.connect_object("clicked", self.button_press_event, text_name)
		self.button.show()
		self.vbox.pack_start(self.button, False,False, 0)

	def check_authentication(self):
		flag=0
		settings = ElementTree.parse('settings.xml').getroot()
		subsettings = settings.find('authentication').find(self.media)
		key=subsettings.find("access_token")
		if self.media == "twitter":
			secret=subsettings.find("access_token_secret")
			if key.text and secret.text:
				flag = 1
			return (flag,key.text,secret.text)
		elif self.media == "dropbox":
			if key.text:
				flag = 1
			return (flag,key.text,None)

	def save_authentication(self, access_token, access_token_secret=None):
		root=ElementTree.parse('settings.xml').getroot()
		subsettings = root.find('authentication').find(self.media)

		atoken = subsettings.find('access_token')
		atoken.text = access_token

		if access_token_secret != None:
			asecret = subsettings.find('access_token_secret')
			asecret.text = access_token_secret
	
		self.savexml(root)

	def savexml(self, root):
		f = open("settings.xml", "w")
		f.write(ElementTree.tostring(root))
		f.close()
		
	def button_press_event(self, widget, data=None):
		
		if self.media=="twitter":
			storage=self.check_authentication()
			if not storage[0]:
				self.api.authenticate(self.entry1.get_text())
				access_token=self.api.access_token
				access_token_secret=self.api.access_token_secret
				self.save_authentication(access_token,access_token_secret)
			gtk.main_quit()

		elif self.media=="dropbox":
			print("dropbox chosen")
			storage=self.check_authentication()            
			if not storage[0]:
				access_token, user_id = self.flow.finish(self.entry1.get_text())
				self.save_authentication(access_token)
			gtk.main_quit()

	def set_clipboard(self, button):
		text = self.textbuffer.get_text(*self.textbuffer.get_bounds()) 
		if self.media=="twitter":
			self.clipboard.set_text(self.auth_url)
		elif self.media=="dropbox":
			self.clipboard.set_text(self.flow.start())

if __name__ == "__main__":
	menu = DestinationsMenu()
	menu.start()