# coding=utf-8
import requests
import json

# This example uses Requests HTTP Library

with open('config.json') as json_data_file:
    config = json.load(json_data_file)

API = config['API']['baseUrl']


def stations(headers):

    url = API + '/stations/F1405/observations/latest?require_qc=false'

    # Make get request to API with headers
    response = requests.get(url, headers=headers)
    return response.text
