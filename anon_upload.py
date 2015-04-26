import base64
import json
import requests
import gtk

from base64 import b64encode

def anonymous_Upload(image):
	response = requests.post(
		"https://api.imgur.com/3/upload.json", 
		headers={"Authorization": "Client-ID a21509ca229e76a"},
		data={'image': b64encode(open(image, 'rb').read()),
			'type': 'base64',
			'name': image,
			'title': 'Picture no. 1'
		}
	)
	x = json.loads(response.text)
	clipboard = gtk.clipboard_get()
	clipboard.set_text(x['data']['link'])
	clipboard.store()

if __name__ == "__main__":
	anonymous_Upload("SCREENSHOT")