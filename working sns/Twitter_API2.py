import tweetpony


def Twitter_API_Running(filename,access_token,access_token_secret,message):
	consumer_key='ilsxfHf2M9WVFod3I0hOPlqlJ'
	consumer_secret= 'PD4gKHDVujDaDiMVkK678BVHoAXtYf4bXpEdZoM9dyLAIZ9xVB'

	# api = tweetpony.API(consumer_key = consumer_key, consumer_secret = consumer_secret)
	# auth_url = api.get_auth_url()
	# print "Open this link to obtain your authentication code: %s" % auth_url
	
	# api.authenticate(code)
	# access_token=api.access_token
	# access_token_secret=api.access_token_secret


#-----------------------------------------------------------------------------------------------------------------------------



	api = tweetpony.API(consumer_key = consumer_key, consumer_secret = consumer_secret, access_token = access_token, access_token_secret = access_token_secret)
	user = api.user
	print "Hello, @%s!" % user.screen_name
	text = message
	# text = "test"
	picture=open(filename, "r")
	try:
	    api.update_status_with_media(status = text, media = [picture])
	    # api.update_status(status = text)
	except tweetpony.APIError as err:
	    print "Oops, something went wrong! Twitter returned error #%i and said: %s" % (err.code, err.description)
	else:
	    print "Yay! Your tweet has been sent!"

if __name__=="__main__":
	Twitter_API_Running("8024341","testing")