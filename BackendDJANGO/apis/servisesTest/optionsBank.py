import json
from json import dumps
import requests
from decouple import config


Api_Key = (config('API_KEY'))
url = (config('URL_API_PROVIDER'))

respuesta = requests.get(url,  headers={
    'X-API-Key': Api_Key,
}, )


json_response = json.loads(respuesta.text)

providers = json_response["providers"]

for elem in providers:
    for k, v in elem.items():
        if (k == "code" and v == "test"):
            print(elem.get("name"))
