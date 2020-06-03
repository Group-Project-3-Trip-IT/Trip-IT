# import dependecies
import requests
import json
from pprint import pprint
from config import api_key

# find tourist attractions from Google places API call
def findPlaces():
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
    # cities = ["NewYorkCity","Washington D.C.","LosAngeles","Boston"]
    cities = ["New York City","Washington DC","Los Angeles","Boston"]
    POI_dict = {}
    for city in cities:
        query = "tourist_attractions"
        response = requests.get(url + 'query=' + query + '+' + city +
                            '&key=' + api_key)
        results_json = response.json()
        results = results_json['results']
        POI_info = {}
        for i in range(len(results)):
            POI_name = results[i]['name']
            lat = results[i]['geometry']['location']['lat']
            lng = results[i]['geometry']['location']['lng']
            try:
                popularity=results[i]['user_ratings_total']
            except:
                popularity=0
            try:
                business_status = results[i]['business_status']
            except:
                business_status =""
            try:
                formatted_address = results[i]['formatted_address']
            except:
                formatted_address = ""
            POI_info[POI_name] = {
                'city':city,
                'POI_name':POI_name,
                'lat':lat,
                'lng':lng,
                'business_status':business_status,
                'formatted_address':formatted_address,
                'popularity':popularity
                }
        POI_dict[city] = POI_info
    return POI_dict

    
# list = findPlaces()
# pprint(list)



