from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from prometeo import Client
from json import dumps
import requests
from decouple import config
from django.views.generic import ListView
import json
from django.http import HttpResponse
from django.template import Template, Context

Api_Key = (config('API_KEY'))
url_login = (config('URL_API_LOGIN'))
url_providers = (config('URL_API_PROVIDER'))

client = Client(Api_Key, environment="sandbox")


def bank(request):
    nombre = []
    respuesta = requests.get(url_providers,  headers={
        'X-API-Key': Api_Key})

    respuesta = respuesta.text
    json_response = json.loads(respuesta)
    providersB = json_response["providers"]
    for elem in providersB:
        nombre.append(elem.get("name"))

    return render(request, 'optionBank.html', {"bancos": nombre})


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
        response = requests.post(url_login, data=credentials, headers={
            'X-API-Key': Api_Key
        })

        try:
            # Login del usuario
            session = client.banking.login(**credentials)

            # Datos del usuario
            responseClient = session._client.call_api("GET", "/info/", params={
                "key": session.get_session_key(),
            })
            # Datos de cuenta
            response = session._client.call_api("GET", "/account/", params={
                "key": session.get_session_key(),
            })
            return render(request, 'userData.html', {'data': responseClient, 'cuentas': response})

        except KeyError:
            return render(request, 'signin.html', {'error': "Usuario o contraseña incorrecta", 'form': AuthenticationForm})


def data(request):
    return render(request, 'userData.html')
