# from xml.etree import ElementTree
# def check_authentication():
#     flag=0
#     settings = ElementTree.parse('settings.xml').getroot()
#     subsettings = settings.find('authentication').find("twitter")
#     try:
#         key=subsettings.find("access_token")
#         print "key:",key.text
#         secret=subsettings.find("access_token_secret")
#         print "secret:",secret.text
#         if key and secret:
#             flag=1
#         return (flag,key,secret)

#     except:
#         pass



# print check_authentication()
key: "269345705-8IUSiwW1BVOh1cIp2kFEKoLCDKIybFjxtXO3jN3B"
secret: "QiSfoTftKRUGOHgF8zHmGuo52dgdpicIZLQGGU8gOvxrG"

if ord(key.text) and ord(secret.text):
    flag=1