from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import Weather, Restaurants, appBikeStation, Hotels,Train_Stations_final,POI_4_cities, TransportationScore
import json

app = Flask(__name__,static_url_path="/static")

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/Trip_IT"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")

# main route for Trip-IT Home page
@app.route("/")
def index():
    weather = mongo.db.weather
    restaurants = mongo.db.restaurants
    bikes = mongo.db.bikes
    hotels = mongo.db.hotels
    trains = mongo.db.trains
    poi = mongo.db.poi
    transportationScore=mongo.db.transportationScore

# This code block needs to run first time , for the database load/updates. After which needs to be commented.

    # weather_data = Weather.weather()
    # restaurants_data = Restaurants.collectRestaurants()
    # bikes_data = appBikeStation.bikeStation()
    # hotels_data = Hotels.findHotelsInfo()
    # trains_data = Train_Stations_final.findtrains()
    # poi_data = POI_4_cities.findPlaces()
    # transpScore_data = TransportationScore.transportationScore()
    
    
    # weather.update({}, weather_data, upsert=True)
    # restaurants.update({}, restaurants_data, upsert=True)
    # bikes.update({}, bikes_data, upsert=True)
    # hotels.update({}, hotels_data, upsert=True)
    # trains.update({}, trains_data, upsert=True)
    # poi.update({}, poi_data, upsert=True)
    # transportationScore.update({}, transpScore_data, upsert=True)
    

    weather = mongo.db.weather.find_one()
    restaurants = mongo.db.restaurants.find_one()
    bikes = mongo.db.bikes.find_one()
    hotels = mongo.db.hotels.find_one()
    trains = mongo.db.trains.find_one()
    poi = mongo.db.poi.find_one()
    transportationScore = mongo.db.transportationScore.find_one()

    weather.pop('_id') 
    restaurants.pop('_id') 
    bikes.pop('_id') 
    hotels.pop('_id') 
    trains.pop('_id') 
    poi.pop('_id')
    transportationScore.pop('_id')
    

    return render_template("index.html", 
    weather=json.dumps(weather), 
    restaurants=json.dumps(restaurants),
    bikes=json.dumps(bikes),
    hotels=json.dumps(hotels),
    trains = json.dumps(trains),
    poi =json.dumps(poi),
    transportationScore=json.dumps(transportationScore))

# Route for New York City page
@app.route("/NewYorkCity")
def NewYorkCity():
    
    weather = mongo.db.weather
    restaurants = mongo.db.restaurants
    bikes = mongo.db.bikes
    hotels = mongo.db.hotels
    trains = mongo.db.trains
    poi = mongo.db.poi
    transportationScore=mongo.db.transportationScore

    weather = mongo.db.weather.find_one()
    restaurants = mongo.db.restaurants.find_one()
    bikes = mongo.db.bikes.find_one()
    hotels = mongo.db.hotels.find_one()
    trains = mongo.db.trains.find_one()
    poi = mongo.db.poi.find_one()
    transportationScore = mongo.db.transportationScore.find_one()

    weather.pop('_id') 
    restaurants.pop('_id') 
    bikes.pop('_id') 
    hotels.pop('_id') 
    trains.pop('_id') 
    poi.pop('_id')
    transportationScore.pop('_id')

    return render_template("NewYorkCity.html", 
    weather=json.dumps(weather), 
    restaurants=json.dumps(restaurants),
    bikes=json.dumps(bikes),
    hotels=json.dumps(hotels),
    trains = json.dumps(trains),
    poi =json.dumps(poi),
    transportationScore=json.dumps(transportationScore))


@app.route("/WashingtonDC")
def WashingtonDC():
    
    weather = mongo.db.weather
    restaurants = mongo.db.restaurants
    bikes = mongo.db.bikes
    hotels = mongo.db.hotels
    trains = mongo.db.trains
    poi = mongo.db.poi
    transportationScore=mongo.db.transportationScore

    weather = mongo.db.weather.find_one()
    restaurants = mongo.db.restaurants.find_one()
    bikes = mongo.db.bikes.find_one()
    hotels = mongo.db.hotels.find_one()
    trains = mongo.db.trains.find_one()
    poi = mongo.db.poi.find_one()
    transportationScore = mongo.db.transportationScore.find_one()

    weather.pop('_id') 
    restaurants.pop('_id') 
    bikes.pop('_id') 
    hotels.pop('_id') 
    trains.pop('_id') 
    poi.pop('_id')
    transportationScore.pop('_id')

    return render_template("WashingtonDC.html", 
    weather=json.dumps(weather), 
    restaurants=json.dumps(restaurants),
    bikes=json.dumps(bikes),
    hotels=json.dumps(hotels),
    trains = json.dumps(trains),
    poi =json.dumps(poi),
    transportationScore=json.dumps(transportationScore))


@app.route("/LosAngeles")
def LosAngeles():
    
    weather = mongo.db.weather
    restaurants = mongo.db.restaurants
    bikes = mongo.db.bikes
    hotels = mongo.db.hotels
    trains = mongo.db.trains
    poi = mongo.db.poi
    transportationScore=mongo.db.transportationScore

    weather = mongo.db.weather.find_one()
    restaurants = mongo.db.restaurants.find_one()
    bikes = mongo.db.bikes.find_one()
    hotels = mongo.db.hotels.find_one()
    trains = mongo.db.trains.find_one()
    poi = mongo.db.poi.find_one()
    transportationScore = mongo.db.transportationScore.find_one()

    weather.pop('_id') 
    restaurants.pop('_id') 
    bikes.pop('_id') 
    hotels.pop('_id') 
    trains.pop('_id') 
    poi.pop('_id')
    transportationScore.pop('_id')

    return render_template("LosAngeles.html", 
    weather=json.dumps(weather), 
    restaurants=json.dumps(restaurants),
    bikes=json.dumps(bikes),
    hotels=json.dumps(hotels),
    trains = json.dumps(trains),
    poi =json.dumps(poi),
    transportationScore=json.dumps(transportationScore))

@app.route("/Boston")
def Boston():
    
    weather = mongo.db.weather
    restaurants = mongo.db.restaurants
    bikes = mongo.db.bikes
    hotels = mongo.db.hotels
    trains = mongo.db.trains
    poi = mongo.db.poi
    transportationScore=mongo.db.transportationScore

    weather = mongo.db.weather.find_one()
    restaurants = mongo.db.restaurants.find_one()
    bikes = mongo.db.bikes.find_one()
    hotels = mongo.db.hotels.find_one()
    trains = mongo.db.trains.find_one()
    poi = mongo.db.poi.find_one()
    transportationScore = mongo.db.transportationScore.find_one()

    weather.pop('_id') 
    restaurants.pop('_id') 
    bikes.pop('_id') 
    hotels.pop('_id') 
    trains.pop('_id') 
    poi.pop('_id')
    transportationScore.pop('_id')

    return render_template("Boston.html", 
    weather=json.dumps(weather), 
    restaurants=json.dumps(restaurants),
    bikes=json.dumps(bikes),
    hotels=json.dumps(hotels),
    trains = json.dumps(trains),
    poi =json.dumps(poi),
    transportationScore=json.dumps(transportationScore))



if __name__ == "__main__":
    app.run(debug=True)