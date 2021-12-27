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

    responseStr = """
    <table class="table">
  <thead>
    <tr>
      <th scope="col">Station</th>
      <th scope="col">Temperature</th>
      <th scope="col">Dewpoint</th>
      <th scope="col">barometric Pressure</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">1</th>
      <td>Mark</td>
      <td>Otto</td>
      <td>@mdo</td>
    </tr>
    """

    for station in stations:
        print(station)
        temperature = station["properties"]["temperature"]["value"]
        stationLink = station["properties"]["station"]
        fahrenheit = (temperature * 9/5) + 32
        responseStr += "<h1>Station " + stationLink + "  Temperature " + str(fahrenheit) + " </h1>"

    responseStr += """  </tbody>
</table>
"""
    return responseStr
    

