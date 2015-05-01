import tweetpony
import pygtk
pygtk.require('2.0')
import gtk
import Queue
import threading


q=Queue.Queue()
def tweeter_call():
    consumer_key='ilsxfHf2M9WVFod3I0hOPlqlJ'
    consumer_secret= 'PD4gKHDVujDaDiMVkK678BVHoAXtYf4bXpEdZoM9dyLAIZ9xVB'
    access_token = '269345705-8IUSiwW1BVOh1cIp2kFEKoLCDKIybFjxtXO3jN3B'
    access_token_secret = 'QiSfoTftKRUGOHgF8zHmGuo52dgdpicIZLQGGU8gOvxrG'


    api = tweetpony.API(consumer_key = consumer_key, consumer_secret = consumer_secret, access_token = access_token, access_token_secret = access_token_secret)
    user = api.user
    print "Hello, @%s!" % user.screen_name
    # text = raw_input("What would you like to tweet? ")
    text="test"

    try:
        api.update_status(status = text)
    except tweetpony.APIError as err:
        print "Oops, something went wrong! Twitter returned error #%i and said: %s" % (err.code, err.description)
    else:
        print "Yay! Your tweet has been sent!"
    q.put(text)

tweeter_call()