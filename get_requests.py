# coding=utf-8
import requests
import json

with open('config.json') as json_data_file:
    config = json.load(json_data_file)

API = config['API']['baseUrl']


def station_observation(headers, station):
    url = API + '/stations/' + station.id + '/observations/latest?require_qc=false'
    response = requests.get(url, headers=headers)
    return json.loads(response.text)
