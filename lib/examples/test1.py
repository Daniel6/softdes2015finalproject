from imgurpython import ImgurClient
from auth import authenticate

client_id = '749bf61e825e475'
client_secret = '7d5ba26773fd8c9a7156d5625203e80c14d1799c'

client = ImgurClient(client_id, client_secret)

# Example request
# items = client.gallery()
# for item in items:
#     print(item.link)

def upload(client):
	img = client.upload_from_path('Kitten.jpg', config={}, anon=True)
	print('Finished')
	return img


if __name__ == "__main__":
	client = authenticate()
	image = upload(client)
	print("You can find your image here: {0}".format(image['link']))





# def sideLoad(imgURL):
# 	clientID = '749bf61e825e475'
#     img = urllib.quote_plus(imgURL)
#     req = urllib2.Request('https://api.imgur.com/3/image', 'image=' + image)
#     req.add_header('Authorization', 'Client-ID ' + clientID)
#     response = urllib2.urlopen(req)
#     response = json.loads(response.read())
#     return str(response[u'data'][u'link'])