import logging

import azure.functions as func
import requests
import os

LIFX_TOKEN = os.getenv('lifx_token')

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    auth_token = f'Bearer {LIFX_TOKEN}'
    response = requests.post('https://api.lifx.com/v1/lights/all/effects/move', data={'period': '10', 'cycles': '1', 'direction': 'backward'}, headers= { 'Authorization': auth_token})

    return func.HttpResponse(response.text)