import json
import requests
import sys
sys.path.insert(1, './lib')
import dropbox
import tweetpony
from base64 import b64encode

def imgur_Upload(image):
	"""Upload an image to imgur anonymously and publicly"""
	response = requests.post(
		"https://api.imgur.com/3/upload.json", 
		headers={"Authorization": "Client-ID a21509ca229e76a"},
		data={'image': b64encode(open('screenshot.png', 'rb').read()),
			'type': 'base64',
			'name': 'screenshot.png',
			'title': 'Picture no. 1',
			'description': 'Description'
		}
	)
	x = json.loads(response.text)
	return x['data']['link']

def dropbox_Upload(file_name, title):
	"""Given a file and title, upload the file to your dropboxwith the title specified"""

	settings = ElementTree.parse('settings.xml').getroot()
	auth = settings.find('authentication')
	dropbox_auth = auth.find('dropbox')

	app_key = 'uehmy7qwfyhnd34'
	app_secret = 'h1tmocr962j6xfa'
	access_token = dropbox_auth.find('access_token').text

	flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
	"""Upload file to dropbox"""
	client = dropbox.client.DropboxClient(access_token)
	folder_metadata = client.metadata('/')

	f = open(file_name, 'rb')
	response = client.put_file('/UploadX/' + title, f)
	return client.media(response['path'])['url']

def twitter_Upload(file_name, message):
	"""Upload an image with a message to your Twitter account"""

	settings = ElementTree.parse('settings.xml').getroot()
	auth = settings.find('authentication')
	twitter_auth = auth.find('twitter')

	consumer_key='ilsxfHf2M9WVFod3I0hOPlqlJ'
	consumer_secret= 'PD4gKHDVujDaDiMVkK678BVHoAXtYf4bXpEdZoM9dyLAIZ9xVB'
	access_token = twitter_auth.find('access_token').text
	access_token_secret = twitter_auth.find('access_token_secret').text


	api = tweetpony.API(consumer_key = consumer_key, consumer_secret = consumer_secret, access_token = access_token, access_token_secret = access_token_secret)
	user = api.user
	print "Hello, @%s!" % user.screen_name
	text = message
	# text = "test"
	picture=open(file_name, "r")
	api.update_status_with_media(status = text, media = [picture])
	return ""

if __name__ == "__main__":
	twitter_Upload("screenshot.png", "hoorah")