# Python program to get a set of 
# restaurants in city using Google Places API 

# importing required modules 
import requests, json 
from pprint import pprint
from config import GOOGLE_APIKEY
import statistics

restaurant_APIKEY = GOOGLE_APIKEY

# function to return restaurants within 4000 radius
def collectRestaurants():

    restaurants_dict = {}

    cities = [{"city":"New York City","lat":40.7128, "lng": -74.0060},
    {"city":"Washington DC","lat":38.9072,"lng": -77.0369},
    {"city":"Los Angeles", "lat":34.0522,"lng": -118.2437},
    {"city":"Boston","lat":42.3601,"lng": -71.0589}]

       
    def findPlaces(citi,lat,lng,radius=4000, pagetoken = None):
        type = "restaurant"
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius={radius}&type={type}&key={restaurant_APIKEY}{pagetoken}".format(lat = lat, lng = lng, radius = radius, type = type,restaurant_APIKEY = restaurant_APIKEY, pagetoken = "&pagetoken="+pagetoken if pagetoken else "")
    
        response = requests.get(url)
        res = json.loads(response.text)

        restaurant_info = {}
        for result in res["results"]:
            
            try:
                price_level= int(result['price_level'])
            except:
                price_level=0
            try:
                rating = float(result['rating'])
            except:
                rating =0

            rest_name = result["name"]
            lat = result['geometry']['location']['lat']
            lng= result['geometry']['location']['lng']

            restaurant_info[rest_name] = {
                'city':citi,
                'rest_name':rest_name,
                'lat':lat,
                'lng':lng,
                'price_level':price_level,
                'rating':rating}

        restaurants_dict[citi] = restaurant_info
        pagetoken = res.get("next_page_token",None)
        return pagetoken


    for city in cities:
        citi=city["city"]
        lat=city["lat"]
        lng=city["lng"]

        pagetoken = None
        while True:
            pagetoken = findPlaces(citi,lat,lng,pagetoken=pagetoken)
            import time
            time.sleep(2)

            if not pagetoken:
                break
                
    city_avg ={}
    for city in cities:
        city_name = city["city"]
        city_data = restaurants_dict[city_name]

        ratings = []
        prices = []
        for data in city_data:
            ratings.append(city_data[data]["rating"])
            prices.append(city_data[data]["price_level"])
        
        rating_avg = round(statistics.mean(ratings),2)
        price_avg = round(statistics.mean(prices),2)
        city_avg[city_name] = {"rating":rating_avg,
                                "price":price_avg}
           
    restaurants_dict["AverageRating"] = city_avg
    
    return restaurants_dict

# pprint(collectRestaurants())

