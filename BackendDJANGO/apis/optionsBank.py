import json
from json import dumps
import requests


API_KEY = ('OWXFSUJiu4DQ8C7uzvLfkBEuYJGBzXikXFoVgAOZ3Y9ocRTef5FRM57OMi7QOAuH')


respuesta = requests.get('https://banking.sandbox.prometeoapi.com/provider/',  headers={
    'X-API-Key': 'OWXFSUJiu4DQ8C7uzvLfkBEuYJGBzXikXFoVgAOZ3Y9ocRTef5FRM57OMi7QOAuH',
}, )


json_response = json.loads(respuesta.text)

providers = json_response["providers"]

for elem in providers:
    for k, v in elem.items():
        if (k == "country" and v == "AR"):
            print(elem.get("name"))
