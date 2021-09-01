# - - - - - - - - - - IMPORT MODULES - - - - - - - - - - #
import requests as req
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# - - - - - - - - - - SETUP VARIABLES - - - - - - - - - - #
SHEETY_ENDPOINT = "https://api.sheety.co/460f379ce0b4e690d10bdc36715fcddf/flightDeals/prices"

TEQUILA_API_KEY = os.environ.get("TEQUILA_API_KEY")
TEQUILA_SEARCH_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
TEQUILA_LOCATIONS_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
LOCATIONS_PARAMS = {
    "term": "Paris",
    "locale": "en-US",
    "location_types": "airport",
    "limit": 1
}
LOCATIONS_HEADER = {
    "apikey": TEQUILA_API_KEY,
}
# - - - - - - - - - - FUNCTIONS - - - - - - - - - - #
def iata_codes():
    cities = []
    sheety_res = req.get(SHEETY_ENDPOINT)
    for city in sheety_res.json()["prices"]:
        cities.append(city["city"])
    for city in cities:
        LOCATIONS_PARAMS["term"] = city
        locations_res = req.get(TEQUILA_LOCATIONS_ENDPOINT, params=LOCATIONS_PARAMS, headers=LOCATIONS_HEADER)
        print(locations_res.json()["locations"][0]["code"])

iata_codes()