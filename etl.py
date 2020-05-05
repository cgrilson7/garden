import requests
import os
from pymongo import MongoClient
from apis.openweather import OpenWeatherInterface

def etl():
    owi = OpenWeatherInterface()
    response = owi.get_by_coordinates(lat=42.45823, lon=-71.34119)
    if response.status_code == 200:
        client = MongoClient()
    #  [client].[db].[collection]
        client.garden.openweather.insert_one(response.json())
        
if __name__ == "__main__":
    etl()