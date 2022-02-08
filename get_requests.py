# coding=utf-8
import requests
import json

with open('config.json') as json_data_file:
    config = json.load(json_data_file)

API = config['API']['baseUrl']

HEADERS = {
    'User-Agent': "(myweatherapp.com, contact@myweatherapp.com)",
    'accept': "application/geo+json",
}


def station_observation(station):
    return get_to_json_response('/stations/' + station.id + '/observations/latest?require_qc=false')


def get_alerts(state):
    return get_to_json_response('/alerts/active?area=' + state)


def get_to_json_response(url):
    response = requests.get(API + url, headers=HEADERS)
    print(response.text)
    return json.loads(response.text)
