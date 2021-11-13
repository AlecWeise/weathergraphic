# coding=utf-8
import os
import get_requests
import json

HEADERS = {
    'User-Agent': "(myweatherapp.com, contact@myweatherapp.com)",
}

# Returns all accounts from owner
response = get_requests.stations(HEADERS)

print(response)
