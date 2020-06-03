# Import Dependencies
import http.client, urllib.request, urllib.parse, urllib.error, base64
import requests
import json
import pandas as pd
from config import wkey
from pprint import pprint

def findtrains():
#Washington DC API for Station Location
    headers = {'api_key': wkey}

    try:
        response = requests.get("https://api.wmata.com/Rail.svc/json/jStations",headers=headers).json()
        # print(response)
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    # Create arrays to store data
    DC_station_name = []
    DC_station_lat = []
    DC_station_lon = []

    # response = requests.get(data_washington)
    train_station = response
    city_name_stations=train_station["Stations"]
    for station in city_name_stations:
        name = DC_station_name.append(station["Name"])
        latitude = DC_station_lat.append(station["Lat"])
        longitude = DC_station_lon.append(station["Lon"])

    #Create and array for DC_train and store staion name, lat and long
    DC_train ={}
    train_station = response
    city_name_stations=train_station["Stations"]
    for station in city_name_stations:
        name = (station["Name"])
        latitude = (station["Lat"])
        longitude = (station["Lon"])
        DC_train[name] = {'lat':latitude,'lng':longitude}

    #Boston

    #Read CSV
    Boston_data = "Support/Boston_Stations.csv"
    Boston_df = pd.read_csv(Boston_data, encoding="ISO-8859-1")

    Boston_station_name = Boston_df["STATION"].tolist()
    Boston_station_lat = Boston_df["Lat"].tolist()
    Boston_station_lon = Boston_df["Lon"].tolist()
    Boston_train = {z[0]:{'lat':z[1],'lng':z[2]} for z in zip(Boston_station_name, Boston_station_lat, Boston_station_lon)}


    #NYC
    NYC_data = "Support/NYC_Stations.csv"
    NYC_df = pd.read_csv(NYC_data, encoding="ISO-8859-1")

    NYC_station_name = NYC_df["NAME"].tolist()
    NYC_station_lat = NYC_df["Lat"].tolist()
    NYC_station_lon = NYC_df["Lon"].tolist()
    NYC_train = {z[0]:{'lat':z[1],'lng':z[2]} for z in zip(NYC_station_name, NYC_station_lat, NYC_station_lon)}

    #LA
    LA_data = "Support/LA_Stations.csv"
    LA_df = pd.read_csv(LA_data, encoding="ISO-8859-1")

    LA_station_name = LA_df["stop_name"].tolist()
    LA_station_lat = LA_df["stop_lat"].tolist()
    LA_station_lon = LA_df["stop_lon"].tolist()
    LA_train = {z[0]:{'lat':z[1],'lng':z[2]} for z in zip(LA_station_name, LA_station_lat, LA_station_lon)}

    #Combine all dictionaries
    Train_All = dict([('New York City',NYC_train), ('Washington DC', DC_train),('Los Angeles', LA_train), ('Boston', Boston_train)])

    # pprint(Train_All)

    return Train_All

# findtrains()