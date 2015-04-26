

from TwitterAPI import TwitterAPI


TWEET_TEXT = "Ce n'est pas un tweet tweet."

APP_KEY = 'ilsxfHf2M9WVFod3I0hOPlqlJ'
APP_SECRET ='PD4gKHDVujDaDiMVkK678BVHoAXtYf4bXpEdZoM9dyLAIZ9xVB'
access_token_key="269345705-8IUSiwW1BVOh1cIp2kFEKoLCDKIybFjxtXO3jN3B"
access_token_secret="QiSfoTftKRUGOHgF8zHmGuo52dgdpicIZLQGGU8gOvxrG"


CONSUMER_KEY = APP_KEY
CONSUMER_SECRET = APP_SECRET
ACCESS_TOKEN_KEY = access_token_key
ACCESS_TOKEN_SECRET = access_token_secret


api = TwitterAPI(CONSUMER_KEY,
                 CONSUMER_SECRET,
                 ACCESS_TOKEN_KEY,
                 ACCESS_TOKEN_SECRET)

r = api.request('statuses/update', {'status': "hahaha"})

print('SUCCESS' if r.status_code == 200 else 'FAILURE')