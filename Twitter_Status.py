import tweetpony
import pygtk
pygtk.require('2.0')
import gtk
import Queue
import threading


q=Queue.Queue()
q_text=Queue.Queue()
text=""
def tweeter_call():
    consumer_key='ilsxfHf2M9WVFod3I0hOPlqlJ'
    consumer_secret= 'PD4gKHDVujDaDiMVkK678BVHoAXtYf4bXpEdZoM9dyLAIZ9xVB'
    access_token = '269345705-8IUSiwW1BVOh1cIp2kFEKoLCDKIybFjxtXO3jN3B'
    access_token_secret = 'QiSfoTftKRUGOHgF8zHmGuo52dgdpicIZLQGGU8gOvxrG'


    api = tweetpony.API(consumer_key = consumer_key, consumer_secret = consumer_secret, access_token = access_token, access_token_secret = access_token_secret)
    user = api.user
    print "Hello, @%s!" % user.screen_name
    # text = raw_input("What would you like to tweet? ")
    try:
        reply=q_text.get()
    except:
        pass
    try:
        api.update_status(status = reply)
    except tweetpony.APIError as err:
        print "Oops, something went wrong! Twitter returned error #%i and said: %s" % (err.code, err.description)
    else:
        print "Yay! Your tweet has been sent!"
    if text=="":
        text="what do you want to Twitter?"
        q.put(text)

# def tweeter_call():
#     try:
#         text = "before"   
#         consumer_key='ilsxfHf2M9WVFod3I0hOPlqlJ'
#         consumer_secret= 'PD4gKHDVujDaDiMVkK678BVHoAXtYf4bXpEdZoM9dyLAIZ9xVB'
#         # access_token = '269345705-8IUSiwW1BVOh1cIp2kFEKoLCDKIybFjxtXO3jN3B'
#         # access_token_secret = 'QiSfoTftKRUGOHgF8zHmGuo52dgdpicIZLQGGU8gOvxrG'

#         api = tweetpony.API(consumer_key = consumer_key, consumer_secret = consumer_secret)
#         auth_url = api.get_auth_url()
#         # print "Open this link to obtain your authentication code: %s" % auth_url
#         # Statusbar()
#         text=auth_url
       


#         # status_bar = gtk.Statusbar()
#         # context_id=status_bar.get_context_id("Statusbar example")
#         # print Statusbar.push_item(context_id, text)
#         code=q_text.get()
#         # code = raw_input("Please enter your authentication code: ")
#         api.authenticate(code)
#         print api.access_token
#         print api.access_token_secret

#         access_token=api.access_token
#         access_token_secret=api.access_token_secret

#         api = tweetpony.API(consumer_key = consumer_key, consumer_secret = consumer_secret, access_token = access_token, access_token_secret = access_token_secret)
#         user = api.user
#         print "Hello, @%s!" % user.screen_name
#     except:
#         pass
#         # text = raw_input("What would you like to tweet? ")
#     text = "testt"
#         # screenshot=open("screenshot.png", "r")
#     try:

#         api.update_status(status = text)
#         # api.update_status_with_media(status = text)
#         # , media = [screenshot]
#     # except tweetpony.APIError as err:
#     #     print "Oops, something went wrong! Twitter returned error #%i and said: %s" % (err.code, err.description)
#     # else:
#     #     print "Yay! Your tweet has been sent!"     # except tweetpony.APIError as err:
#     #     print "Oops, something went wrong! Twitter returned error #%i and said: %s" % (err.code, err.description)
#     # else:
#     #     print "Yay! Your tweet has been sent!"   # except tweetpony.APIError as err:
#     #     print "Oops, something went wrong! Twitter returned error #%i and said: %s" % (err.code, err.description)
#     # else:
#     #     print "Yay! Your tweet has been sent!"   # except tweetpony.APIError as err:
#     #     print "Oops, something went wrong! Twitter returned error #%i and said: %s" % (err.code, err.description)
#     # else:
#     #     print "Yay! Your tweet has been sent!" # except tweetpony.APIError as err:
#     #     print "Oops, something went wrong! Twitter returned error #%i and said: %s" % (err.code, err.description)
#     # else:
#     #     print "Yay! Your tweet has been sent!"
#     except:
#         print "wrong"
#     q.put(text)



class Statusbar(object):
    
    def push_item(self, context_id, text):
        self.status_bar.push(self.context_id, text)
        entry_text = self.entry.get_text()
        print entry_text


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
        self.status_bar.show()
        vbox.pack_start(self.status_bar, True, True, 0)
        self.context_id=self.status_bar.get_context_id("Statusbar example")
        
        self.entry = gtk.Entry()
        text="Title"
        self.push_item(self.context_id, text)
        text="Description"
        self.entry.connect("activate", self.push_item,text)
        vbox.pack_start(self.entry, True, True, 0)
        self.entry.show()
        window.show()

def main():
    gtk.main()
    return 0


def Statusbar_Running():
    Statusbar()
    main()    

if __name__=="__main__":
    Statusbar_Running()
    # threading.Thread(target=Statusbar_Running).start()        

    # threading.Thread(target=tweeter_call).start()        

    # tweeter_call()
    # # Statusbar()
    # main()
