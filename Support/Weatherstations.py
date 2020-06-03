import requests

citiesLocations={
    'New York City':[40.7128,-74.0060],
    'Boston':[42.3601,-71.0589],
    'Washington DC':[38.9072,-77.0369],
    'Los Angeles':[34.0522,-118.2437]
}

apiKey = 'jseaiEFl'

cityWeatherStations={}

for key,value in citiesLocations.items():
    url = f'https://api.meteostat.net/v1/stations/nearby?lat={value[0]}&lon={value[1]}&limit=5&key={apiKey}'

    response = requests.get(url).json()
    stationID = response['data'][0]['id']
    stationName = response['data'][0]['name']

    station = {'Statio ID':stationID,'Station Name':stationName}

    cityWeatherStations[key] = station

print(cityWeatherStations)