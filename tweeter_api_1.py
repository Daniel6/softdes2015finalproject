# from twython import Twython

# twitter = Twython(
#     twitter_token = 'HbV8NVJlcttlgntRgQg3n9VVp',
#     twitter_secret = 'VBlpcDJxDlusVfgL6qI27AONHpMKfU4e5aA8pjaha9YykqffFl',
#     oauth_token = '269345705-9NZuJoqJA6QnhWU1FniXLdp1qxc9o778e1jDANZC',
#     oauth_token_secret = 'JgVqJYieblEzUXUQhPmbhM7s23CnCkj4dCXrQWTRHQ5GW')

# twitter.updateStatusWithMedia(status='post from twitter api')


from twython import Twython, TwythonError

APP_KEY= 'HbV8NVJlcttlgntRgQg3n9VVp'
APP_SECRET= 'VBlpcDJxDlusVfgL6qI27AONHpMKfU4e5aA8pjaha9YykqffFl'
OAUTH_TOKEN= '269345705-9NZuJoqJA6QnhWU1FniXLdp1qxc9o778e1jDANZC'
OAUTH_TOKEN_SECRET= 'JgVqJYieblEzUXUQhPmbhM7s23CnCkj4dCXrQWTRHQ5GW'


# Requires Authentication as of Twitter API v1.1
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

try:
    twitter.update_status(status='See how easy this was?')
except TwythonError as e:
    print e