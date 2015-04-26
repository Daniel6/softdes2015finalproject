# # # import urllib2
# # # from BeautifulSoup import BeautifulSoup
# # # # or if you're using BeautifulSoup4:
# # # # from bs4 import BeautifulSoup

# # # soup = BeautifulSoup(urllib2.urlopen('https://api.twitter.com/oauth/authenticate?oauth_token=TkDcIa4REffSNaRHk7M8QGGIW0f9oT3Y').read())
# # # print soup

# # # from webscraping import download, xpath
# # # D = download.Download()

# # # html = D.get('https://api.twitter.com/oauth/authenticate?oauth_token=TkDcIa4REffSNaRHk7M8QGGIW0f9oT3Y')

# # import requests
# # from bs4 import BeautifulSoup

# # url = "https://api.twitter.com/oauth/authenticate?oauth_token=TkDcIa4REffSNaRHk7M8QGGIW0f9oT3Y"
# # page  = requests.get(url).text
# # soup_expatistan = BeautifulSoup(page)
# # print soup_expatistan

# import requests
# response = requests.get('http://pyvideo.org/category/50/pycon-us-2014')
# print response.text

from lxml import html
import requests
page = requests.get("https://api.twitter.com/oauth/authenticate?oauth_token=TkDcIa4REffSNaRHk7M8QGGIW0f9oT3Y")
# tree = html.fromstring(page.text)
# print tree
print page.text