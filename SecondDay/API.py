# API
"""
API  - application programming interface

"""

import requests
from pprint import pprint
url = 'https://cats-paradise-f994f218e0ee.herokuapp.com/api/v1/cats'

response = requests.get(url)
data = response.json()

for cat in data:
    print(cat['name'])

'''
CRUD: 
CREATE
READ
UPDATE
DELETE
'''
