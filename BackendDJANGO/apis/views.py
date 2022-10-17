from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from prometeo import Client
from json import dumps
import requests
from decouple import config


Api_Key = (config('API_KEY'))
url = (config('URL_API_LOGIN'))

client = Client(Api_Key, environment="sandbox")


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        credentials = {
            'provider': 'test',
            'username': request.POST['username'],
            'password': request.POST['password'],
        }
        response = requests.post(url, data=credentials, headers={
            'X-API-Key': Api_Key
        })
        session = client.banking.login(**credentials)

        if session is None:
            return render(request, 'signin.html',)
        else:
            try:
                # Datos del usuario
                responseClient = session._client.call_api("GET", "/info/", params={
                    "key": session.get_session_key(),
                })
                # Datos de cuenta
                response = session._client.call_api("GET", "/account/", params={
                    "key": session.get_session_key(),
                })
                return render(request, 'userData.html', {'data': responseClient, 'cuentas': response})

            except ValueError:
                return render(request, 'signin.html',)


def data(request):

    return render(request, 'userData.html', responseClient)
