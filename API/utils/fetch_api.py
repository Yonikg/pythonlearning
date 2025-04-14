import requests 


# GET, POST, PUT/PATCH , DELETE: 
'''
HTTP status code
404: Not found
200: Succes
201: Created 
401: Denied

'''
from pprint import pprint
def fetch_data(url):
    response = requests.get(url)
    data = response.json() 
    return data

    