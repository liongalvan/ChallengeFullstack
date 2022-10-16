from json import dumps
from decouple import config
import json
import requests


def userData():
    url = (config('URL_INFO'))
    Api_Key = (config('API_KEY'))
    response = requests.get(url, params={
        'key': '4ee2d8d468cd4c05ac81046b90a4ab8d',
    }, headers={
        'X-API-Key': Api_Key
    })
    if response.status_code == 201:
        return response.json()
