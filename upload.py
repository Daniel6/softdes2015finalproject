import json
import requests
# import dropbox
from base64 import b64encode

def imgur_Upload(image):
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

def dropbox_Upload(file_name,code,title,flow):
	app_key = 'uehmy7qwfyhnd34'
	app_secret = 'h1tmocr962j6xfa'

	access_token, user_id = flow.finish(code) # Creates an access token
	client = dropbox.client.DropboxClient(access_token)
	print 'linked account: ', client.account_info()

	folder_metadata = client.metadata('/')
	print "metadata:", folder_metadata

	f = open(file_name, 'rb')
	response = client.put_file('/UploadX/' + title, f)
	print "uploaded:", response

if __name__ == "__main__":
	dropbox_Upload("screenshot.png")