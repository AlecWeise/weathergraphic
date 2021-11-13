from flask import Flask
import os
import get_requests
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/san-anselmo")
def sananselmo():
    HEADERS = {
    'User-Agent': "(myweatherapp.com, contact@myweatherapp.com)",
    'accept': "application/geo+json",
}

    # Returns all accounts from owner
    response = get_requests.stations(HEADERS)
    respObject = json.loads(response)

    temperature = respObject["properties"]["temperature"]["value"]
    return "<h1>Temperature " + str(temperature) + " </h1>"    