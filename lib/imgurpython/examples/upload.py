#!/usr/bin/env python3

'''
	Here's how you upload an image. For this example, put the cutest picture
	of a kitten you can find in this script's folder and name it 'Kitten.jpg'

	For more details about images and the API see here:
		https://api.imgur.com/endpoints/image
'''

# Pull authentication from the auth example
from auth import authenticate
from datetime import datetime

def upload(image_path):
	client = authenticate()

	album = None # You can also enter an album ID here
	# Here's the metadata for the upload. All of these are optional, including
	# this config dict itself.
	config = {
		'album': album,
		'name':  'Catastrophe!',
		'title': 'Catastrophe!',
		'description': 'Cute kitten being cute on {0}'.format(datetime.now())
	}

	print("Uploading image... ")
	image = client.upload_from_path(image_path, config=config, anon=False)
	print("Done")

	print("Image was posted!")
	print("You can find it here: {0}".format(image['link']))

# If you want to run this as a standalone script
if __name__ == "__main__":
	upload("Kitten.jpg")