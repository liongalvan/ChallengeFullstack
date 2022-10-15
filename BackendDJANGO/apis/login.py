from prometeo import Client
from json import dumps
import requests

r = requests.get('https://www.python.org')

API_KEY = ('OWXFSUJiu4DQ8C7uzvLfkBEuYJGBzXikXFoVgAOZ3Y9ocRTef5FRM57OMi7QOAuH')

respuesta = requests.post('https://banking.sandbox.prometeoapi.com/login/', data={
    'provider': 'Banco Nación',
    'username': '12345',
    'password': 'gfdsa',
}, headers={
    'X-API-Key': 'OWXFSUJiu4DQ8C7uzvLfkBEuYJGBzXikXFoVgAOZ3Y9ocRTef5FRM57OMi7QOAuH'
})
print(respuesta.json())
