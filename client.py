# coding=utf-8
import os
import get_requests
import json

HEADERS = {
    'User-Agent': "(myweatherapp.com, contact@myweatherapp.com)",
    'accept': "application/geo+json",
}

# Returns all accounts from owner
response = get_requests.stationIds(HEADERS)

# print(response)

responsePython = json.loads(response)

print(responsePython["@context"])



