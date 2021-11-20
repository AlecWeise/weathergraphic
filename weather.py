from flask import Flask
from flask import render_template
import os
import get_requests
import json
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('main.html', name="Alec")

@app.route("/san-anselmo")
def sananselmo():
    HEADERS = {
    'User-Agent': "(myweatherapp.com, contact@myweatherapp.com)",
    'accept': "application/geo+json",
}

    # Returns all accounts from owner
    jsonStr = get_requests.stations(HEADERS)
    respDictionary = json.loads(jsonStr)

    temperature = respDictionary["properties"]["temperature"]["value"]
    return "<h1>Temperature " + str(temperature) + " </h1>"    
    

