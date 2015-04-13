import base64
import json
import requests

from base64 import b64encode

response = requests.post(
    "https://api.imgur.com/3/upload.json", 
    headers={"Authorization": "Client-ID a21509ca229e76a"},
    data={'image': b64encode(open('screenshot.png', 'rb').read()),
        'type': 'base64',
        'name': 'screenshot.png',
        'title': 'Picture no. 1'
    }
)
x = json.loads(response.text)
print(x)
print(x['data']['link'])