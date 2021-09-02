# - - - - - - - - - - IMPORT MODULES - - - - - - - - - - #
import requests as req
import os
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())

# - - - - - - - - - - SETUP VARIABLES - - - - - - - - - - #
SHEETY_ENDPOINT = "https://api.sheety.co/460f379ce0b4e690d10bdc36715fcddf/flightDeals/prices"
SHEETY_HEADERS = {
    "Authorization" : "Basic dGVycnlzemhvdToxNFxsKytkbjM/NjkyMDY3"
}

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
        cities.append({city["city"]: city["id"]})
    for city in cities:
        for key in city.keys():
            LOCATIONS_PARAMS["term"] = key
            locations_res = req.get(TEQUILA_LOCATIONS_ENDPOINT, params=LOCATIONS_PARAMS, headers=LOCATIONS_HEADER)
            price_params = {
                "price": {
                    'iataCode': locations_res.json()["locations"][0]["code"],
                }
            }
            sheety_put_res = req.put(f"{SHEETY_ENDPOINT}/{city[key]}", json=price_params)
            print(sheety_put_res.text)

iata_codes()