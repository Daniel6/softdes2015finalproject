import requests
from requests_oauthlib import OAuth1
from urlparse import parse_qs
from TwitterAPI import TwitterAPI

APP_KEY = 'ilsxfHf2M9WVFod3I0hOPlqlJ'
APP_SECRET ='PD4gKHDVujDaDiMVkK678BVHoAXtYf4bXpEdZoM9dyLAIZ9xVB'
consumer_key = APP_KEY
consumer_secret = APP_SECRET


# obtain request token
oauth = OAuth1(consumer_key, consumer_secret)
r = requests.post(
    url='https://api.twitter.com/oauth/request_token',
    auth=oauth)
credentials = parse_qs(r.content)
request_key = credentials.get('oauth_token')[0]
request_secret = credentials.get('oauth_token_secret')[0]


# obtain authorization from resource owner
print(
    'Go here to authorize:\n  https://api.twitter.com/oauth/authorize?oauth_token=%s' %
    request_key)
verifier = raw_input('Enter your authorization code: ')


# obtain access token
oauth = OAuth1(consumer_key,
               consumer_secret,
               request_key,
               request_secret,
               verifier=verifier)
r = requests.post(url='https://api.twitter.com/oauth/access_token', auth=oauth)
credentials = parse_qs(r.content)
access_token_key = credentials.get('oauth_token')[0]
access_token_secret = credentials.get('oauth_token_secret')[0]
print "access_token_key", access_token_key
print "access_token_secret:", access_token_secret

# access resource
api = TwitterAPI(consumer_key,
                 consumer_secret,
                 access_token_key,
                 access_token_secret)

# file = open(IMAGE_PATH, 'rb')
# data = file.read()
# r = api.request('statuses/update_with_media',
#                 {'status': TWEET_TEXT},
#                 {'media[]': data})
r = api.request('statuses/update', {'status': "api testing"})

print('SUCCESS' if r.status_code == 200 else 'FAILURE')
