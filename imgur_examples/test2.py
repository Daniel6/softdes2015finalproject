from auth import authenticate
from datetime import datetime
import json

album = 'qAIoQ' # You can also enter an album ID here
image_path = 'Kitten.jpg'

def upload(client):

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
	print()

	return image


# If you want to run this as a standalone script
if __name__ == "__main__":
	client = authenticate()
	image = upload(client)

	print("Image was posted! Go check your images you sexy beast!")
	print("You can find it here: {0}".format(image['link']))