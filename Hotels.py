# importing dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import time
import pandas as pd
from datetime import datetime
from pprint import pprint

sleep_time=3

citiesURL={
    'New York City':'http://insideairbnb.com/new-york-city/',
    'Washington DC':'http://insideairbnb.com/washington-dc/',
    'Los Angeles':'http://insideairbnb.com/los-angeles/',
    'Boston':'http://insideairbnb.com/boston/'
}

# function to collect airbnb details
def findHotelsInfo():

    scrape_nightPrice={}

    for key,value in citiesURL.items():
        browser = init_browser()

        url= value
        browser.visit(url)
        time.sleep(sleep_time)

        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        price=soup.find("span", {"id": "summaryPrice"}).text
        totalListings=soup.find("span", {"id": "geoTotalListings"}).text
        entireHome=soup.find("span", {"id": "summaryEntireHomeMetricsNumber"}).text
        privateRoom=soup.find("span", {"id": "summaryPrivateRoomMetricsNumber"}).text
        sharedRoom=soup.find("span", {"id": "summarySharedRoomMetricsNumber"}).text
        availability=soup.find("span",class_="summaryHighAvailabilityListingsPercentage").text

        cityObject={
            'City':key,
            'Total Listings':totalListings,
            'Price Per Night ($)':price,
            'Availability (%)':availability,
            'Entire Homes':entireHome,
            'Private Rooms':privateRoom,
            'Shared Rooms':sharedRoom            
        }

        scrape_nightPrice[key]=cityObject

        browser.quit()

    now = datetime.now()
    scrape_nightPrice['timestamp']=now.strftime("%m/%d/%Y-%H:%M")

    # pp = pprint.PrettyPrinter(indent=4)
    # pprint(scrape_nightPrice)
    return scrape_nightPrice
    



def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

# findHotelsInfo()



