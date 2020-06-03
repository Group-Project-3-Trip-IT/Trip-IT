# Dependencies
import requests
import json
from pprint import pprint


city_url = {"New York City" : "https://gbfs.citibikenyc.com/gbfs/en/station_information.json",
            "Washington DC":"https://gbfs.capitalbikeshare.com/gbfs/en/station_information.json",
           "Los Angeles":"https://gbfs.bcycle.com/bcycle_lametro/station_information.json",
            "Boston": "https://gbfs.bluebikes.com/gbfs/en/station_information.json"
            }
#function to return bike stations locations
def bikeStation():

    all_bike_stations = {}

    for city, url in city_url.items():

        response = requests.get(url)
        bikeplaces = response.json()
        bike_stations=bikeplaces["data"]["stations"]
        
        station_bike ={}

        for station in bike_stations:

            station_name = (station["name"])
            latitude = (station["lat"])
            longitude = (station["lon"])
            station_bike[station_name] = {'lat':latitude,'lng':longitude}

        city_name = city
        all_bike_stations[city_name] = station_bike 

    # pprint(all_bike_stations)

    return all_bike_stations


# bikeStation()