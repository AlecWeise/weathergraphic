class Station:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class StationObservation:
    def __init__(self,
                 station,
                 temperature=None,
                 max_temperature_last24hours=None,
                 min_temperature_last24hours=None,
                 humidity=None,
                 wind_chill=None,
                 heat_index=None,
                 dewpoint=None,
                 precipitation_last3hours=None,
                 wind_direction=None,
                 wind_speed=None,
                 wind_gust=None,
                 sealevel_pressure=None,
                 barometric_pressure=None,
                 visibility=None,
                 ):
        self.station = station
        self.temperature = temperature
        self.max_temperature_last24hours = max_temperature_last24hours,
        self.min_temperature_last24hours = min_temperature_last24hours,
        self.humidity = humidity
        self.wind_chill = wind_chill
        self.heat_index = heat_index
        self.dewpoint = dewpoint
        self.precipitation_last3hours = precipitation_last3hours
        self.wind_direction = wind_direction
        self.wind_speed = wind_speed
        self.wind_gust = wind_gust
        self.sealevel_pressure = sealevel_pressure
        self.barometric_pressure = barometric_pressure
        self.visibility = visibility
