from prometeo import Client
from json import dumps
import requests
from decouple import config
import json


r = requests.get('https://www.python.org')

Api_Key = (config('API_KEY'))
url = (config('URL_API_LOGIN'))

client = Client(Api_Key, environment="sandbox")

credentials = {
    'provider': 'test',
    'username': '12345',
    'password': 'gfdsa',
}

response = requests.post(url, data=credentials, headers={
    'X-API-Key': Api_Key
})

session = client.banking.login(**credentials)
print(session._client)

try:
    # Datos del usuario
    responseClient = session._client.call_api("GET", "/info/", params={
        "key": session.get_session_key(),
    })
    # Datos de cuenta
    response = session._client.call_api("GET", "/account/", params={
        "key": session.get_session_key(),
    })
    print(dumps(responseClient))
    print(dumps(response, indent=4))

finally:
    session.logout()
