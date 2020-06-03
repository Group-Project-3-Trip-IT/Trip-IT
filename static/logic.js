// Cities Location to center the map on load
citiesLocations = {
    "New York City": { "Lat": 40.7128, "Lon": -74.0060 },
    "Washington DC": { "Lat": 38.9072, "Lon": -77.0369 },
    "Los Angeles": { "Lat": 34.0522, "Lon": -118.2437 },
    "Boston": { "Lat": 42.3601, "Lon": -71.0589 },
}

// capture City name
var city = d3.select("#City").text()


// variables to hold data for each data points that feeds into the Trip-IT application
var weather = JSON.parse(d3.select(".weather").text())
var poi = JSON.parse(d3.select(".poi").text())
var trains = JSON.parse(d3.select(".trains").text())
var bikes = JSON.parse(d3.select(".bikes").text())
var restaurants = JSON.parse(d3.select(".restaurants").text())
var hotels = JSON.parse(d3.select(".hotels").text())
var transpScore = JSON.parse(d3.select(".transportationScore").text())



// remove divs created to capture data rendered from python flask server
d3.select(".weather").remove();
d3.select(".poi").remove();
d3.select(".trains").remove();
d3.select(".bikes").remove();
d3.select(".restaurants").remove();
d3.select(".hotels").remove();
d3.select(".transportationScore").remove();

// icons dictionary to hold marker icons to show in maps
var icons = {
    Restaurants: L.ExtraMarkers.icon({
        icon: "ion-coffee",
        iconColor: "white",
        markerColor: "red",
        shape: "circle"
    }),
    Bikes: L.ExtraMarkers.icon({
        icon: "ion-android-bicycle",
        iconColor: "white",
        markerColor: "green-light",
        shape: "circle"
    }),
    POIs: L.ExtraMarkers.icon({
        icon: "ion-flag",
        iconColor: "white",
        markerColor: "blue-dark",
        shape: "circle"
    }),
    Trains: L.ExtraMarkers.icon({
        icon: "ion-android-train",
        iconColor: "white",
        markerColor: "orange",
        shape: "circle"
    })
}

// Function for creating all markers in map
function createMarkers() {

    var poi_Markers = [];
    var rest_markers = [];
    var train_markers = [];
    var bike_markers = [];

    // Creating markers for POIs
    Object.entries(poi[city]).forEach(function([key, value]) {
        var marker_name = key

        var marker_details = L.marker(value, {
                icon: icons['POIs']
            })
            .bindPopup("<p>" + marker_name + "</p>");

        poi_Markers.push(marker_details);

    })

    // Creating markers for Restaurants
    Object.entries(restaurants[city]).forEach(function([key, value]) {
        var marker_name = key

        var marker_details = L.marker(value, {
                icon: icons['Restaurants']
            })
            .bindPopup("<p><strong>" + marker_name + "</strong></p>" + "<hr>" + "<p> Rating:" + value["rating"] + " | Price Level:" + value["price_level"] + "</p>");

        rest_markers.push(marker_details);

    })

    // Creating markers for trains
    Object.entries(trains[city]).forEach(function([key, value]) {
        var marker_name = key

        var marker_details = L.marker(value, {
                icon: icons['Trains']
            })
            .bindPopup("<p>" + marker_name + "</p>");

        train_markers.push(marker_details);

    })

    // Creating markers for bikes
    Object.entries(bikes[city]).forEach(function([key, value]) {
        var marker_name = key

        var marker_details = L.marker(value, {
                icon: icons['Bikes']
            })
            .bindPopup("<p>" + marker_name + "</p>");

        bike_markers.push(marker_details);

    })

    // Create layer groups 
    var poi_details = L.layerGroup(poi_Markers);
    var rest_details = L.layerGroup(rest_markers);
    var train_details = L.layerGroup(train_markers);
    var bike_details = L.layerGroup(bike_markers);

    // Create the tile layer that will be the background of our map

    var streetmap = L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
        attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
        maxZoom: 18,
        id: 'mapbox/streets-v11',
        tileSize: 512,
        zoomOffset: -1,
        accessToken: API_KEY
    })

    // Create a baseMaps object to hold the streetmap layer
    var baseMaps = {
        "Street Map": streetmap
    };

    // Create overlayMaps object to hold the different layers
    var overlayMaps = {
        "Points Of Interest": poi_details,
        "Restaurants": rest_details,
        "Trains": train_details,
        "Bike Stations": bike_details
    };

    // Create the map object
    var map = L.map("map", {
        center: [citiesLocations[city]['Lat'], citiesLocations[city]['Lon']],
        zoom: 12,
        layers: [streetmap, poi_details]
    });

    // Create a layer control
    L.control.layers(baseMaps, overlayMaps, {
        collapsed: true
    }).addTo(map);


}

createMarkers()

// Function for Previous Year weather plot
function YearlyWeather() {
    var Months = ["Jan 2019", "Feb 2019", "Mar 2019", "Apr 2019", "May 2019",
        "June 2019", "July 2019", "Aug 2019", "Sep 2019", "Oct 2019", "Nov 2019", "Dec 2019"
    ]
    var Temp = []
    var RainyDays = []

    Object.entries(weather[city]).forEach(function([key, value]) {
        // Months.push(key)
        Temp.push(parseFloat(value["Mean Temperature"]))
        RainyDays.push(parseInt(value["Rainy Days"]))
    })

    var temp = {
        x: Months,
        y: Temp,
        name: "Avg Temperature",
        type: 'bar',
        marker: {
            color: '#34ebe5'
        }
    };

    var Rain = {
        x: Months,
        y: RainyDays,
        name: "Number of Rainy Days",
        type: 'scatter'
    };

    var layout = {
        height: 500,
        title: { text: `${city} Weather (Previous Year)`, font: { color: "white", size: 25 } },
        xaxis: {
            tickangle: -30,
            color: 'white'
        },

        yaxis: {
            align: "left",
            color: 'white'
        },
        legend: {
            font: {
                color: 'white'
            },
            x: 1,
            xanchor: 'right',
            y: 1
        },
        plot_bgcolor: "black",
        paper_bgcolor: "black",
        margin: {
            l: 50,
            r: 50,
            b: 80,
            t: 80,
            pad: 10
        }
    };
    var line_bar_chart = [temp, Rain];
    Plotly.newPlot('weatherMap', line_bar_chart, layout);
}

YearlyWeather()

// Sorting POI by user ratings to list tourist attractions
var sortPOI = []
Object.entries(poi[city]).forEach(function([key, value]) {
    var popularity = value['popularity']
    sortPOI.push([key, popularity])
})
sortPOI.sort(function(a, b) {
    return b[1] - a[1];
});

var top10POI = sortPOI.slice(0, 10)

var resultcontent = '';
for (i = 0; i < top10POI.length; i++) {
    resultcontent += '<li class="poi_details">' + top10POI[i][0] + '</li>'
}
$('#content').append(resultcontent);

d3.select(window).on("resize", YearlyWeather);