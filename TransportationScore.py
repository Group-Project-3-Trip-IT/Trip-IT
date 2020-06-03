# import dependencies
import pandas as pd
from pprint import pprint

cities = ["New York City","Washington DC","Los Angeles","Boston"]

cities_order = [2,1,3,0]

# function to real excel for Transportation facts and return dictionary
def transportationScore():
    
    transport_df = pd.read_excel('Support/TransportationFacts.xlsx')
    transport_df = transport_df.loc[(transport_df['City']=="Boston")|(transport_df['City']=="Washington")|(transport_df['City']=="New York")|(transport_df['City']=="Los Angeles"),:]
    transport_score=transport_df.to_dict("records")
  

    transport_rank={}
        
    for index,city in enumerate(cities):
        position = cities_order[index]
        transport_rank[city]=transport_score[position]
        
    # pprint(transport_rank)
    
    return transport_rank

# transportationScore()