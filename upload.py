import json
import requests
import sys
sys.path.insert(1, './lib')
import dropbox
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

def dropbox_Upload(access_token, file_name, title):
	app_key = 'uehmy7qwfyhnd34'
	app_secret = 'h1tmocr962j6xfa'
	flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
	"""Upload file to dropbox"""
	client = dropbox.client.DropboxClient(access_token)
	folder_metadata = client.metadata('/')

	f = open(file_name, 'rb')
	response = client.put_file('/UploadX/' + title, f)
	return client.media(response['path'])['url']

if __name__ == "__main__":
	print(dropbox_Upload("8PI1wJknXpkAAAAAAAAB2oxw70Bgr7mavYF0iu4LCkZxUjKGyaZXPASZFKTAFUvh", "screenshot.png", "test_daniel.png"))