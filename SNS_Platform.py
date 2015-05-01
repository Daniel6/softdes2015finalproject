import tweetpony
import pygtk
pygtk.require('2.0')
import gtk
import Twitter_API2
import tweetpony
import Dropbox_API
import dropbox
import Imgur_anon_upload
import qr_code

class Statusbar(object):
    def Initilize_Register(self,media):
        
        if self.media=="twitter":
        
            consumer_key='ilsxfHf2M9WVFod3I0hOPlqlJ'
            consumer_secret= 'PD4gKHDVujDaDiMVkK678BVHoAXtYf4bXpEdZoM9dyLAIZ9xVB'
            self.api = tweetpony.API(consumer_key = consumer_key, consumer_secret = consumer_secret)
            self.auth_url = self.api.get_auth_url()
            print self.auth_url
        
        elif self.media=="dropbox":
            app_key = 'uehmy7qwfyhnd34'
            app_secret = 'h1tmocr962j6xfa'        
            self.flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
            print self.flow.start() # Prints the authentication url
        
        elif self.media=="imgur":
            self.imgur_url=Imgur_anon_upload.anonymous_Upload(self.filename)
            print self.imgur_url

        elif self.media=="qr":
            self.imgur_url=Imgur_anon_upload.anonymous_Upload(self.filename)
            qr_code(self.imgur_url)
            gtk.main_quit()

    
    def authentication_callback(self, context_id, text):
        entry_text = self.entry1.get_text()
        self.status_bar.push(self.context_id, self.text)
        self.entry1.set_text("")
        self.authentication=entry_text
        print "authentication:",entry_text

    def title_callback(self, context_id, text):
        entry_text = self.entry2.get_text()
        self.status_bar.push(self.context_id, self.text)
        self.entry2.set_text("")
        self.title=entry_text
        print "title:",entry_text
    
    def description_callback(self, context_id, text):
        entry_text = self.entry3.get_text()
        self.status_bar.push(self.context_id, self.text)
        self.entry3.set_text("")
        self.description=entry_text
        print "description:",entry_text

    def create_button(self,text_name):
        self.button = gtk.Button(text_name)
        self.button.connect_object("clicked", self.button_press_event, text_name)
        self.button.show()
        self.vbox.pack_start(self.button, False,False, 0)
    
    def button_press_event(self, widget, data=None):
        
        if self.media=="twitter":
            print "authentication:",self.authentication
            print "title:",self.title
            print "description:",self.description
            Twitter_API2.Twitter_API_Running(self.filename,self.authentication,self.title,self.api)
            gtk.main_quit()
 
        if self.media=="dropbox":
            Dropbox_API.upload(self.filename,self.authentication,self.title,self.flow)
            gtk.main_quit()
        if self.media=="imugr":
            pass

    def set_clipboard(self, button):
        print self.imgur_url
        text = self.textbuffer.get_text(*self.textbuffer.get_bounds())
        if self.media=="twitter":
            self.clipboard.set_text(self.auth_url)
        if self.media=="dropbox":
            self.clipboard.set_text(self.flow.start())
        if self.media=="imugr":
            print self.imgur_url
            self.clipboard.set_text(self.imgur_url)
            gtk.main_quit()
        return
    
    def __init__(self, media, filename):
        self.media=media
        self.filename=filename
        
        self.Initilize_Register(media)
        # create a new window
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_size_request(300, 230)
        window.set_title("UploadX SNS Platform")
        window.connect("delete_event", lambda w,e: gtk.main_quit())
 
        self.vbox = gtk.VBox(False, 1)
        window.add(self.vbox)
        
        self.button1 = gtk.Button('Copy Authentication URL to Clipboard')
        self.button1.show()
        self.button1.connect('clicked', self.set_clipboard)
        self.clipboard = gtk.clipboard_get(gtk.gdk.SELECTION_CLIPBOARD)
        self.textview = gtk.TextView()
        self.textbuffer = self.textview.get_buffer()
        self.vbox.pack_start(self.button1, False,False, 0)


        self.status_bar = gtk.Statusbar()
        self.status_bar.show()
        self.vbox.pack_start(self.status_bar, False,False, 0)
        self.context_id=self.status_bar.get_context_id("Statusbar example")
        
        self.entry1 = gtk.Entry()
        self.text="Paste Authentication Code"
        # self.text="https://api.twitter.com/oauth/authenticate?oauth_token=n1QQ8LYDZS7XWibBaz18zdk13oYuF5jI"
        self.authentication_callback(self.context_id, self.text)
        self.entry1.connect("activate", self.authentication_callback,self.text)
        self.vbox.pack_start(self.entry1,  False,False, 0)
        self.entry1.show()


        self.status_bar = gtk.Statusbar()
        self.status_bar.show()
        self.vbox.pack_start(self.status_bar,  False,False, 0)
        self.context_id=self.status_bar.get_context_id("Statusbar example")

        self.entry2 = gtk.Entry()
        self.text="Title"
        self.title_callback(self.context_id, self.text)
        self.entry2.connect("activate", self.title_callback,self.text)
        self.vbox.pack_start(self.entry2,  False,False, 0)
        self.entry2.show()

        self.status_bar = gtk.Statusbar()
        self.status_bar.show()
        self.vbox.pack_start(self.status_bar,  False,False, 0)
        self.context_id=self.status_bar.get_context_id("Statusbar example")


        self.entry3 = gtk.Entry()
        self.text="Description"
        self.description_callback(self.context_id, self.text)
        self.entry3.connect("activate", self.description_callback,self.text)
        self.vbox.pack_start(self.entry3,  False,False, 0)
        self.entry3.show()

        self.create_button("ok")


        self.vbox.show()
        window.show_all()

def main():
    gtk.main()
    return 0


def Statusbar_Running(media,filename):
    Statusbar(media,filename)
    main()    

if __name__=="__main__":
    filename="test.jpg"
    Statusbar_Running("imgur",filename)
