import requests
from decouple import config

url = (config('URL_LOGOUT'))
Api_Key = (config('API_KEY'))


headers = {
    "accept": "application/json",
    'X-API-Key': Api_Key
}

response = requests.get(url, headers=headers)

print(response.text)
