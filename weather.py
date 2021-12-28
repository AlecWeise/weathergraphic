from flask import Flask
from flask import render_template
import os
import get_requests
import json
from viewmodel import StationObservation
from viewmodel import Station

app = Flask(__name__)

HEADERS = {
    'User-Agent': "(myweatherapp.com, contact@myweatherapp.com)",
    'accept': "application/geo+json",
}

floatFormat = "{:10.2f}"

stations = [
    Station('F1405', 'FW1405 San Anselmo'),
    Station('F8022', 'FW8022 Pacifica')
]


@app.route("/")
def main():
    jsonStr = get_requests.observations(HEADERS)
    respDictionary = json.loads(jsonStr)

    stations = respDictionary["observationStations"]
    return render_template('base.html', stations=stations)


@app.route("/observations")
def observations():
    return render_template('table_temperature.html', observations=get_observations(), current='observations', table='temperature' )


@app.route("/observations/wind")
def wind():
    return render_template('table_wind.html', observations=get_observations(), current='observations', table='wind')

@app.route("/observations/other")
def other():
    return render_template('table_other.html', observations=get_observations(), current='observations', table='other')

@app.route("/map")
def map():
    return render_template('map.html', current='map', )


def get_observations():
    obs = []
    for station in stations:
        station_obs = get_requests.station_observation(HEADERS, station)
        temp = station_obs["properties"]["temperature"]["value"]
        fahrenheit = (temp * 9 / 5) + 32
        obs.append(StationObservation(
            station=station,
            temperature=floatFormat.format(fahrenheit),
            humidity=floatFormat.format(station_obs["properties"]["relativeHumidity"]["value"]),
            dewpoint=station_obs["properties"]["dewpoint"]["value"],
            wind_direction=station_obs["properties"]["windDirection"]["value"],
            wind_speed=station_obs["properties"]["windSpeed"]["value"],
            wind_gust=station_obs["properties"]["windGust"]["value"],
            barometric_pressure=station_obs["properties"]["barometricPressure"]["value"],
            sealevel_pressure=station_obs["properties"]["seaLevelPressure"]["value"],
            precipitation_last3hours=station_obs["properties"]["precipitationLast3Hours"]["value"],
            wind_chill=station_obs["properties"]["windChill"]["value"],
            max_temperature_last24hours=station_obs["properties"]["maxTemperatureLast24Hours"]["value"],
            min_temperature_last24hours=station_obs["properties"]["minTemperatureLast24Hours"]["value"],
            visibility=station_obs["properties"]["visibility"]["value"],
            heat_index=station_obs["properties"]["heatIndex"]["value"],
        ))
    return obs
