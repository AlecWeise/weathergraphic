from flask import Flask
from flask import render_template
import os
import get_requests
import json
app = Flask(__name__)

HEADERS = {
    'User-Agent': "(myweatherapp.com, contact@myweatherapp.com)",
    'accept': "application/geo+json",
}


@app.route("/")
def main():
    jsonStr = get_requests.observations(HEADERS)
    respDictionary = json.loads(jsonStr)

    stations = respDictionary["observationStations"]
    return render_template('main.html', stations=stations)

@app.route("/observations")
def observations():

    stations = get_requests.stations(HEADERS)

    responseStr = ""

    for station in stations:
        print(station)
        temperature = station["properties"]["temperature"]["value"]
        responseStr += "<h1>Temperature " + str(temperature) + " </h1>"

    return responseStr
    

