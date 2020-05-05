import requests
import os

class OpenWeatherInterface:

    def __init__(self, version="2.5"):
        self.version = version
        self.url_base = f"http://api.openweathermap.org/data/{self.version}/weather?"
        self.api_key = os.environ['OPENWEATHER_API_KEY']
        self.url_suffix = f"&appid={self.api_key}"

    def get_(self, url_full):
        return requests.get(url_full)

    def get_by_coordinates(self, lat, lon):
        url_full = self.url_base + f"lat={lat}" + "&" + f"lon={lon}" + self.url_suffix
        return self.get_(url_full)

    def get_by_zipcode(self, zipcode):
        url_full = self.url_base + f"zip={zipcode}" + self.url_suffix
        return self.get_(url_full)

    def get_by_city_name(self, city_name):
        pass

    def get_by_city_id(self, city_id):
        pass
