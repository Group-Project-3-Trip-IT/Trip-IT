# import dependencies
import requests
import pandas as pd
from datetime import datetime
from config import apiKey, openWeatherAPI
import json

# import pprint 

# dictionary of cities and locations
citiesLocations={
    "New York City":{"Lat":40.7128, "Lon":-74.0060, "Station":"72502"},
    "Washington DC":{"Lat":38.9072, "Lon":-77.0369, "Station":"72405"},
    "Los Angeles":{"Lat":34.0522, "Lon":-118.2437, "Station":"72295"},
    "Boston":{"Lat":42.3601, "Lon":-71.0589, "Station":"72509"},
}

# function to convert celcius to farenheit
def C_to_F(temp):
    if temp is None:
        return ""
    if type(temp)==str:
        if "-" in temp:
            split=temp.split("-")
            t=-float(split[1])
        else:
            t=float(temp)
    else:
        t=temp
    F=(t * 9/5) + 32
    return round(F,2)

currentYear = datetime.now().year
Year = currentYear-1
fromMonth = "01"
toMonth ="12"

fromDate = f'{Year}-{fromMonth}'
toDate = f'{Year}-{toMonth}'

# function to get weather info
def weather():
    weatheYearCity={}

    # function to get yearly data from meteostat API
    for key,value in citiesLocations.items():
        url = f'https://api.meteostat.net/v1/history/monthly?station={value["Station"]}&start={fromDate}&end={toDate}&key={apiKey}'
        response = requests.get(url).json()
        data=response["data"]
        monthCity={}
        for row in data:
            month=row['month']
            temperature_mean=C_to_F(row['temperature_mean'])
            temperature_min=C_to_F(row['temperature_min'])
            temperature_max=C_to_F(row['temperature_max'])
            precipitation=row['precipitation']
            raindays=row['raindays']
            pressure=row['pressure']
            sunshine=row['sunshine']
            monthStats={
                "Mean Temperature":f"{temperature_mean}",
                "Min Temperature":f"{temperature_min}",
                "Max Temperature":f"{temperature_max}",
                "Precipitation":f"{round(precipitation/25.4,2)}",
                "Rainy Days":raindays,
                "Pressure":f"{pressure}",
                "Sunshine Duration":f"{sunshine}"}

            monthCity[month]=monthStats
        
        weatheYearCity[key]=monthCity

    units='imperial'

    # function to get today's data from open weather map API
    for key,value in citiesLocations.items():
        url = f'http://api.openweathermap.org/data/2.5/weather?lat={value["Lat"]}&lon={value["Lon"]}&appid={openWeatherAPI}&units={units}'

        response = requests.get(url).json()
        temp = response['main']['temp']
        feelsLike = response['main']['feels_like']
        tempMin = response['main']['temp_min']
        tempMax = response['main']['temp_max']
        pressure = response['main']['pressure']
        humidity = response['main']['humidity']
        windSpeed=response['wind']['speed']
        sunrise= int(response['sys']['sunrise'])- 14400
        sunset = int(response['sys']['sunset']) - 14400
        shortDescription = response['weather'][0]['main']
        description = response['weather'][0]['description']

        todayWeather = {
            "City":key,
            "Temp (F)":f"{temp}",
            "Feels Like (F)":f"{feelsLike}",
            "Min Temp (F)":f"{tempMin}",
            "Max Temp (F)":f"{tempMax}",
            # "Pressure":f"{pressure}",
            "Humidity (%)":f"{humidity}",
            "Wind Speed (mph)":f"{windSpeed}",
            "Sunrise (EST)":datetime.utcfromtimestamp(sunrise).strftime('%H:%M'),
            "Sunset (EST)":datetime.utcfromtimestamp(sunset).strftime('%H:%M'),
            # "Short Description":shortDescription,
            "Overall Weather":description
        }

        weatheYearCity[key]["Today"]=todayWeather

    now = datetime.now()
    weatheYearCity["timestamp"]=now.strftime("%m/%d/%Y-%H:%M")


    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(weatheYearCity)

    return weatheYearCity

# weather()
