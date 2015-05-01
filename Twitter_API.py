# import tweetpony
# import Status_Bar
# import pygtk
# pygtk.require('2.0')
# import gtk


# def tweeter_call():
# 	consumer_key='ilsxfHf2M9WVFod3I0hOPlqlJ'
# 	consumer_secret= 'PD4gKHDVujDaDiMVkK678BVHoAXtYf4bXpEdZoM9dyLAIZ9xVB'
# 	# access_token = '269345705-EfvXGlPaHtY2foygiGZnay938uvECzsGlGlpVdIA', access_token_secret = 'JZaJyGfa5OCq2VOrW6f6JQPnQKh5e1Un2zFDRpAqPO3a4'
# 	api = tweetpony.API(consumer_key = consumer_key, consumer_secret = consumer_secret)
# 	auth_url = api.get_auth_url()
# 	print "Open this link to obtain your authentication code: %s" % auth_url
# 	code = raw_input("Please enter your authentication code: ")
# 	api.authenticate(code)
# 	print api.access_token
# 	print api.access_token_secret

# 	access_token=api.access_token
# 	access_token_secret=api.access_token_secret
# 	# access_token = '269345705-EfvXGlPaHtY2foygiGZnay938uvECzsGlGlpVdIA'
# 	# access_token_secret = 'JZaJyGfa5OCq2VOrW6f6JQPnQKh5e1Un2zFDRpAqPO3a4'

# 	api = tweetpony.API(consumer_key = consumer_key, consumer_secret = consumer_secret, access_token = access_token, access_token_secret = access_token_secret)
# 	user = api.user
# 	print "Hello, @%s!" % user.screen_name

#     # self.context_id=self.status_bar.get_context_id("Statusbar example")

# 	# Status_Bar.StatusbarExample.push_item(self.context_id, text)

# 	text = raw_input("What would you like to tweet? ")
# 	# text="test"
# 	screenshot=open("screenshot.png", "r")
# 	try:
# 	    api.update_status_with_media(status = text, media = [screenshot])
# 	except tweetpony.APIError as err:
# 	    print "Oops, something went wrong! Twitter returned error #%i and said: %s" % (err.code, err.description)
# 	else:
# 	    print "Yay! Your tweet has been sent!"
# if __name__=="__main__":
# 	tweeter_call()


import tweetpony


consumer_key='ilsxfHf2M9WVFod3I0hOPlqlJ'
consumer_secret= 'PD4gKHDVujDaDiMVkK678BVHoAXtYf4bXpEdZoM9dyLAIZ9xVB'
# access_token = '269345705-8IUSiwW1BVOh1cIp2kFEKoLCDKIybFjxtXO3jN3B'
# access_token_secret = 'QiSfoTftKRUGOHgF8zHmGuo52dgdpicIZLQGGU8gOvxrG'



api = tweetpony.API(consumer_key = consumer_key, consumer_secret = consumer_secret)
auth_url = api.get_auth_url()
# print "Open this link to obtain your authentication code: %s" % auth_url
print auth_url


code='0849298'
# code = raw_input("Please enter your authentication code: ")
api.authenticate(code)


access_token=api.access_token
access_token_secret=api.access_token_secret

api = tweetpony.API(consumer_key = consumer_key, consumer_secret = consumer_secret, access_token = access_token, access_token_secret = access_token_secret)
user = api.user
# print "Hello, @%s!" % user.screen_name
# text = raw_input("What would you like to tweet? ")
text = "test3"
# screenshot=open("screenshot.png", "r")
try:
    # api.update_status_with_media(status = text, media = [screenshot])
        api.update_status(status = text)
except tweetpony.APIError as err:
    print "Oops, something went wrong! Twitter returned error #%i and said: %s" % (err.code, err.description)
else:
    print "Yay! Your tweet has been sent!"