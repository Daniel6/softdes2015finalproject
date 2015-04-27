# Include the Dropbox SDK
import dropbox

# Get your app key and secret from the Dropbox developer website
app_key = 'q68gcs8kg63lq3y'
app_secret = 'wuus2lvqb0xnot4'


def upload(file_name):
	flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

	print '1. Go to: ' + flow.start() # Prints the authentication url
	print '2. Click "Allow" (you might have to log in first)'
	print '3. Copy the authorization code.'
	code = raw_input("Enter the authorization code here: ").strip()

	access_token, user_id = flow.finish(code) # Creates an access token
	client = dropbox.client.DropboxClient(access_token)
	print 'linked account: ', client.account_info()

	folder_metadata = client.metadata('/')
	print "metadata:", folder_metadata

	f = open(file_name, 'rb')
	response = client.put_file('/UploadX/' + file_name, f)
	print "uploaded:", response

if __name__ == "__main__":
	upload('test.jpg')
