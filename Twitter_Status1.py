import tweetpony
import pygtk
pygtk.require('2.0')
import gtk
# import Queue
# import threading


# q=Queue.Queue()
# q_text=Queue.Queue()
text=""
# def tweeter_call():
#     consumer_key='ilsxfHf2M9WVFod3I0hOPlqlJ'
#     consumer_secret= 'PD4gKHDVujDaDiMVkK678BVHoAXtYf4bXpEdZoM9dyLAIZ9xVB'
#     access_token = '269345705-8IUSiwW1BVOh1cIp2kFEKoLCDKIybFjxtXO3jN3B'
#     access_token_secret = 'QiSfoTftKRUGOHgF8zHmGuo52dgdpicIZLQGGU8gOvxrG'


#     api = tweetpony.API(consumer_key = consumer_key, consumer_secret = consumer_secret, access_token = access_token, access_token_secret = access_token_secret)
#     user = api.user
#     print "Hello, @%s!" % user.screen_name
#     # text = raw_input("What would you like to tweet? ")
#     try:
#         reply=q_text.get()
#     except:
#         pass
#     try:
#         api.update_status(status = reply)
#     except tweetpony.APIError as err:
#         print "Oops, something went wrong! Twitter returned error #%i and said: %s" % (err.code, err.description)
#     else:
#         print "Yay! Your tweet has been sent!"
#     if text=="":
#         text="what do you want to Twitter?"
#         q.put(text)

# # def tweeter_call():
# #     try:
# #         text = "before"   
# #         consumer_key='ilsxfHf2M9WVFod3I0hOPlqlJ'
# #         consumer_secret= 'PD4gKHDVujDaDiMVkK678BVHoAXtYf4bXpEdZoM9dyLAIZ9xVB'
# #         # access_token = '269345705-8IUSiwW1BVOh1cIp2kFEKoLCDKIybFjxtXO3jN3B'
# #         # access_token_secret = 'QiSfoTftKRUGOHgF8zHmGuo52dgdpicIZLQGGU8gOvxrG'

# #         api = tweetpony.API(consumer_key = consumer_key, consumer_secret = consumer_secret)
# #         auth_url = api.get_auth_url()
# #         # print "Open this link to obtain your authentication code: %s" % auth_url
# #         # Statusbar()
# #         text=auth_url
       


# #         # status_bar = gtk.Statusbar()
# #         # context_id=status_bar.get_context_id("Statusbar example")
# #         # print Statusbar.push_item(context_id, text)
# #         code=q_text.get()
# #         # code = raw_input("Please enter your authentication code: ")
# #         api.authenticate(code)
# #         print api.access_token
# #         print api.access_token_secret

# #         access_token=api.access_token
# #         access_token_secret=api.access_token_secret

# #         api = tweetpony.API(consumer_key = consumer_key, consumer_secret = consumer_secret, access_token = access_token, access_token_secret = access_token_secret)
# #         user = api.user
# #         print "Hello, @%s!" % user.screen_name
# #     except:
# #         pass
# #         # text = raw_input("What would you like to tweet? ")
# #     text = "testt"
# #         # screenshot=open("screenshot.png", "r")
# #     try:

# #         api.update_status(status = text)
# #         # api.update_status_with_media(status = text)
# #         # , media = [screenshot]
# #     # except tweetpony.APIError as err:
# #     #     print "Oops, something went wrong! Twitter returned error #%i and said: %s" % (err.code, err.description)
# #     # else:
# #     #     print "Yay! Your tweet has been sent!"     # except tweetpony.APIError as err:
# #     #     print "Oops, something went wrong! Twitter returned error #%i and said: %s" % (err.code, err.description)
# #     # else:
# #     #     print "Yay! Your tweet has been sent!"   # except tweetpony.APIError as err:
# #     #     print "Oops, something went wrong! Twitter returned error #%i and said: %s" % (err.code, err.description)
# #     # else:
# #     #     print "Yay! Your tweet has been sent!"   # except tweetpony.APIError as err:
# #     #     print "Oops, something went wrong! Twitter returned error #%i and said: %s" % (err.code, err.description)
# #     # else:
# #     #     print "Yay! Your tweet has been sent!" # except tweetpony.APIError as err:
# #     #     print "Oops, something went wrong! Twitter returned error #%i and said: %s" % (err.code, err.description)
# #     # else:
# #     #     print "Yay! Your tweet has been sent!"
# #     except:
# #         print "wrong"
# #     q.put(text)



class Statusbar(object):
    
    def authentication_code(self, context_id, text):
        self.status_bar.push(self.context_id, text)
        entry_text = self.entry1.get_text()
        self.authentication_code=entry_text
        self.entry1.set_text("")
        print "authentication:",entry_text

    def title(self, context_id, text):
        self.status_bar.push(self.context_id, text)
        entry_text = self.entry2.get_text()
        self.title=entry_text
        self.entry2.set_text("")
        print "title:",entry_text

    def description(self, context_id, text):
        self.status_bar.push(self.context_id, text)
        entry_text = self.entry3.get_text()
        self.description=entry_text
        self.entry3.set_text("")
        print "description:",entry_text

    def __init__(self):
        # create a new window
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_size_request(200, 100)
        window.set_title("PyGTK Statusbar Example")
        window.connect("delete_event", lambda w,e: gtk.main_quit())
        
        vbox = gtk.VBox(False, 1)
        window.add(vbox)
        vbox.show()

        self.status_bar = gtk.Statusbar()
        self.status_bar.show()
        vbox.pack_start(self.status_bar, True, True, 0)
        self.context_id=self.status_bar.get_context_id("Statusbar example")
    
        self.entry1 = gtk.Entry()
        text="https://api.twitter.com/oauth/authenticate?oauth_token=ezLLPQTjLaUiiCc8i73lIQoEkdBMTzHP"
        self.authentication_code(self.context_id, text)
        self.entry1.connect("activate", self.authentication_code,text)
        vbox.pack_start(self.entry1, True, True, 0)
        self.entry1.show()        


        self.entry2 = gtk.Entry()
        text="Description"
        self.description(self.context_id, text)
        self.entry2.connect("activate", self.description,text)
        vbox.pack_start(self.entry2, True, True, 0)
        self.entry2.show()   


        self.entry3 = gtk.Entry()
        text="title"
        self.title(self.context_id, text)
        self.entry3.connect("activate", self.title,text)
        vbox.pack_start(self.entry3, True, True, 0)
        self.entry3.show()           

        # always display the window as the last step so it all splashes on
        # the screen at once.
        window.show()

def main():
    gtk.main()
    return 0


def Statusbar_Running():
    Statusbar()
    main()    

if __name__=="__main__":
    Statusbar_Running()
