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


// Logo using anime.js
let titleMoving = anime({
    targets: '.navbar-brand',
    translateX: {
        value: 250,
        duration: 800
    },
    rotate: {
        value: 180,
        duration: 800,
    },
    easing: 'linear',
    direction: 'alternate',
    delay: 800,
    loop: true
});


var chartArea = d3.select("#bar")
var dropdown = d3.select("#measures")
var tbody = d3.select(".table");
tbody.classed("text-white", true)

// x-ticks for City Name
var Ticks = []
Object.keys(weather).forEach(function(key) {
    if (key != "timestamp") {
        Ticks.push(key)
    }
});

//Initiating the Today's Weather Chart
weatherBar()

// dropdown on change function to call the various plot functions
dropdown.on("change", chartForDropdown);


// Resizing the chart when the window size changes
d3.select(window).on("resize", chartForDropdown);



// Function for Today's weather comparison
function weatherBar() {
    var MinTemperature = []
    var MaxTemperature = []
    var FeelsLike = []
    tbody.html("")
    create_thead(weather["New York City"]["Today"])

    Object.entries(weather).forEach(function([key, value]) {
        if (key != "timestamp") {
            data_to_table(value["Today"])
            var min_temp = parseFloat(value['Today']['Min Temp (F)'])
            var max_temp = parseFloat(value['Today']['Max Temp (F)'])
            var feels_like = parseFloat(value['Today']['Feels Like (F)'])
            MinTemperature.push(min_temp)
            MaxTemperature.push(max_temp)
            FeelsLike.push(feels_like)

        }
    })

    trace_bar_min = {
        x: Ticks,
        y: MinTemperature,
        name: "Temperature - Low",
        type: 'bar',
        marker: {
            color: '#188ca1'
        }
    };

    trace_bar_max = {
        x: Ticks,
        y: MaxTemperature,
        name: "Temperature - High",
        type: 'bar',
    };
    trace_feels_like = {
        x: Ticks,
        y: FeelsLike,
        name: "Feels like",
        type: 'scatter',
        marker: {
            color: '#a1184a'
        }
    };

    var layout_bar = {
        xaxis: {
            color: 'white',
            tickfont:{
                size:16
            }
        },
        yaxis: {
            align: "left",
            color: 'white'
        },
        legend: {
            font: {
                color: 'white'
            },
            x:0,
            y:-0.15,
            orientation: "h"
        },
        plot_bgcolor: "black",
        paper_bgcolor: "black",
        margin: {
            l: 60,
            r: 30,
            b: 0,
            t: 50,
            pad: 4
        }
    };
    var bar_chart = [trace_bar_min, trace_bar_max, trace_feels_like];
    Plotly.newPlot('bar', bar_chart, layout_bar);

    d3.select('#chartTitle').text("Today's Weather (F)")

}

// Function for Public transprtation comparison 
function transpScoreBar() {

    transp_rank = []
    tbody.html("")

    create_thead(transpScore["New York City"])

    Object.entries(transpScore).forEach(function([key, value]) {
        transp_rank.push(value['Total Score'])
        data_to_table(value)
    })

    trace_bar = {
        x: Ticks,
        y: transp_rank,
        type: 'bar',
        text: transp_rank.map(value=>"<b>"+value+"</b>"),
        textposition: 'auto',
        textfont: {
            color: 'black'
          },
        hoverinfo: 'none',
        marker: { color: ['#99ddff', '#4dc3ff', '#cceeff', '#0088cc'] },
        name: "Score",
        width: 0.5
    };

    var layout_bar = {
        // title: { text: `Public Transportation Rating (100 US Major Cities)`, font: { color: "white" } },
        xaxis: {
            color: 'white',
            tickfont:{
                size:16
            }
        },
        yaxis: {
            align: "left",
            color: 'black'
        },
        plot_bgcolor: "black",
        paper_bgcolor: "black",
        margin: {
            l: 10,
            r: 10,
            b: 60,
            t: 50,
            pad: 4
        }
    };
    var bar_chart = [trace_bar];
    Plotly.newPlot('bar', bar_chart, layout_bar);

    d3.select('#chartTitle').text('Public Transportation Total Score (100 US Major Cities)')
}

// Function for restaurants rating/price level comparison 
function restaurantsBar() {
    var restaurantsRating = []
    var restaurantsPrice = []
    tbody.html("")

    Object.entries(restaurants['AverageRating']).forEach(function([key, value]) {
        var rating = parseFloat(value['rating'])
        restaurantsRating.push(rating)

        var price = parseFloat(value['price'])
        restaurantsPrice.push(price)

    });

    trace_rating = {
        x: Ticks,
        y: restaurantsRating,
        name: "Average Rating",
        type: 'bar',
        text: restaurantsRating.map(value=>"<b>"+value+"</b>"),
        textposition: 'auto',
        textfont: {
            color: 'black'
          },
        hoverinfo: 'none',
        marker: {
            color: '#188ca1'
        }
    };

    var trace_price_level = {
        x: Ticks,
        y: restaurantsPrice,
        name: "Average Price Level",
        type: 'bar',
        text: restaurantsPrice.map(value=>"<b>"+value+"</b>"),
        textposition: 'auto',
        textfont: {
            color: 'black'
          },
        hoverinfo: 'none',
    };

    var layout_bar = {
        // title: { text: `Average Restaurants Rating`, font: { color: "white" } },
        xaxis: {
            color: 'white',
            tickfont:{
                size:16
            }
        },
        yaxis: {
            align: "left",
            color: 'black'
        },
        legend: {
            font: {
                color: 'white'
            },
            x:0,
            y:-0.15,
            orientation: "h"
        },
        plot_bgcolor: "black",
        paper_bgcolor: "black",
        margin: {
            l: 30,
            r: 30,
            b: 0,
            t: 50,
            pad: 4
        },
        barmode: 'group'
    };
    var bar_chart = [trace_rating, trace_price_level];
    Plotly.newPlot('bar', bar_chart, layout_bar);

    d3.select('#chartTitle').text("Average Restaurants Rating")
}

// Function for Airbnb price per night and availability comparison 
function nightPriceBar() {
    var nightPrice = []
    var availability = []
    tbody.html("")

    create_thead(hotels["New York City"])
    Object.entries(hotels).forEach(function([key, value]) {
        if (key != "timestamp") {
            var price = parseFloat(value['Price Per Night ($)'])
            nightPrice.push(price)

            var available = parseFloat(value['Availability (%)'])
            availability.push(available)

            data_to_table(value)
        }

    });

    var trace_price = {
        x: Ticks,
        y: nightPrice,
        name: "Avg Price per Night ($)  ",
        text: nightPrice.map(value=>"<b>$"+value+"</b>"),
        textposition: 'auto',
        textfont: {
            color: 'black'
          },
        hoverinfo: 'none',
        type: 'bar',
        marker: { color: '#2eb8b8' },
        width: 0.5
    };

    var trace_availability = {
        x: Ticks,
        y: availability,
        mode: 'markers+text+lines',
        text: availability.map(value=>"<b>"+value+" %</b>"),
        textposition: 'bottom center',
        textfont: {
            color: 'black'
          },
        hoverinfo: 'none',
        name: "Avg Availability (%)",
        type: 'scatter'
    };

    var layout_bar = {
        // title: { text: `Average AirBnb Price per Night`, font: { color: "white" } },
        xaxis: {
            color: 'white',
            tickfont:{
                size:16
            }
        },
        yaxis: {
            align: "left",
            color: 'black'
        },
        legend: {
            font: {
                color: 'white'
            },
            x:0,
            y:-0.15,
            orientation: "h"
        },
        plot_bgcolor: "black",
        paper_bgcolor: "black",
        margin: {
            l: 10,
            r: 10,
            b: 0,
            t: 50,
            pad: 4
        }
    };
    var bar_chart = [trace_price, trace_availability];
    Plotly.newPlot('bar', bar_chart, layout_bar);

    d3.select('#chartTitle').text("Average AirBnb Price per Night and Availability")

}

// function for table head
function create_thead(object) {
    Object.keys(object).forEach(function(key) {
        tbody.append("th").text(key);
    })
}

// Function for table data
function data_to_table(object) {
    var row = tbody.append("tr");
    Object.values(object).forEach(function(value) {
        row.append("td").text(value)
    })
};

function chartForDropdown() {

    var dropdownValue = dropdown.property("value")

    if (dropdownValue == 'weather') {
        weatherBar()
    } else if (dropdownValue == 'transport') {
        transpScoreBar()
    } else if (dropdownValue == 'reataurants') {
        restaurantsBar()
    } else if (dropdownValue == 'accomodationPrice') {
        nightPriceBar()
    }
}