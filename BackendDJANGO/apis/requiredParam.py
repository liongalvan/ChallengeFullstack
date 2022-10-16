import requests
from decouple import config

Api_Key = (config('API_KEY'))

response = requests.get('https://banking.sandbox.prometeoapi.com/provider/test/', headers={
    'X-API-Key': Api_Key
})

print(response.text)
