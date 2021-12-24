# coding=utf-8
import requests
import json

# This example uses Requests HTTP Library
stationIds = ['F1405', 'F8022']

with open('config.json') as json_data_file:
    config = json.load(json_data_file)

API = config['API']['baseUrl']


def observations(headers):
    url = API + '/stations?state=CA&limit=10'

    # Make get request to API with headers
    response = requests.get(url, headers=headers)
    return response.text


def stations(headers):
    stations = []

    for stationID in stationIds:
        url = API + '/stations/' + stationID + '/observations/latest?require_qc=false'
        response = requests.get(url, headers=headers)
        stationDict = json.loads(response.text)
        stations.append(stationDict)
        # temperature = respDictionary["properties"]["temperature"]["value"]

    return stations
