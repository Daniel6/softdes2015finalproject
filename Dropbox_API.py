# Include the Dropbox SDK
import dropbox

# Get your app key and secret from the Dropbox developer website
app_key = 'uehmy7qwfyhnd34'
app_secret = 'h1tmocr962j6xfa'


def upload(file_name,code,title,flow):
	# flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

	# print flow.start() # Prints the authentication url

	# code = raw_input("Enter the authorization code here: ").strip()

	access_token, user_id = flow.finish(code) # Creates an access token
	client = dropbox.client.DropboxClient(access_token)
	print 'linked account: ', client.account_info()

	folder_metadata = client.metadata('/')
	print "metadata:", folder_metadata

	f = open(file_name, 'rb')
	response = client.put_file('/UploadX/' + title, f)
	print "uploaded:", response

if __name__ == "__main__":
	upload('test.jpg')