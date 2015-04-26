from twython import Twython, TwythonError


APP_KEY = 'ilsxfHf2M9WVFod3I0hOPlqlJ'
APP_SECRET ='PD4gKHDVujDaDiMVkK678BVHoAXtYf4bXpEdZoM9dyLAIZ9xVB'

twitter = Twython(APP_KEY, APP_SECRET)

auth = twitter.get_authentication_tokens()
# callback_url='https://api.twitter.com/oauth/authenticate?oauth_token=TkDcIa4REffSNaRHk7M8QGGIW0f9oT3Y'
OAUTH_TOKEN = auth['oauth_token']
OAUTH_TOKEN_SECRET = auth['oauth_token_secret']

oauth_verifier = auth.GET['oauth_verifier']


# twitter = Twython(APP_KEY, APP_SECRET,
#                   OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# final_step = twitter.get_authorized_tokens(oauth_verifier)
# OAUTH_TOKEN = final_step['oauth_token']
# OAUTH_TOKEN_SECRET = final_step['oauth_token_secret']