# - - - - - - - - - - IMPORT MODULES - - - - - - - - - - #
import requests as req
import os
from twilio.rest import Client
from datetime import datetime, timedelta
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())

# - - - - - - - - - - SETUP VARIABLES - - - - - - - - - - #
TOMORROW = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
SIX_MONTHS_HENCE = (datetime.now() + timedelta(days=60)).strftime("%d/%m/%Y")

SHEETY_ENDPOINT = "https://api.sheety.co/460f379ce0b4e690d10bdc36715fcddf/flightDeals/prices"
SHEETY_HEADERS = {
    "Authorization" : "Basic dGVycnlzemhvdToxNFxsKytkbjM/NjkyMDY3"
}

TEQUILA_API_KEY = os.environ.get("TEQUILA_API_KEY")
TEQUILA_HEADER = {
    "apikey": TEQUILA_API_KEY,
}

TEQUILA_SEARCH_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
SEARCH_PARAMS = {
    "fly_from": "AUS",
    "fly_to": "MIA",
    "dateFrom": TOMORROW,
    "dateTo": SIX_MONTHS_HENCE
}


TEQUILA_LOCATIONS_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
LOCATIONS_PARAMS = {
    "term": "Paris",
    "locale": "en-US",
    "location_types": "airport",
    "limit": 1
}

ACCT_SID = os.environ.get("TWILIO_ACCT_SID")
AUTH_TOKEN = os.environ.get("TWILIO_ACCT_TOKEN")
PHONE_NUM = "+15406251609"

# - - - - - - - - - - FUNCTIONS - - - - - - - - - - #
def iata_codes():
    cities = []
    sheety_res = req.get(SHEETY_ENDPOINT)
    for city in sheety_res.json()["prices"]:
        cities.append({city["city"]: city["id"]})
    for city in cities:
        for key in city.keys():
            LOCATIONS_PARAMS["term"] = key
            locations_res = req.get(TEQUILA_LOCATIONS_ENDPOINT, params=LOCATIONS_PARAMS, headers=TEQUILA_HEADER)
            price_params = {
                "price": {
                    'iataCode': locations_res.json()["locations"][0]["code"],
                }
            }
            sheety_put_res = req.put(f"{SHEETY_ENDPOINT}/{city[key]}", json=price_params)
            print(sheety_put_res.text)

# iata_codes()

def flight_search():
    sheety_res = req.get(SHEETY_ENDPOINT)
    for city in sheety_res.json()["prices"]:
        SEARCH_PARAMS["fly_to"] = city["iataCode"]
        search_res = req.get(TEQUILA_SEARCH_ENDPOINT, params=SEARCH_PARAMS, headers=TEQUILA_HEADER)
        for flight in search_res.json()["data"]:
            if flight["price"] < city["lowestPrice"]:
                client = Client(ACCT_SID, AUTH_TOKEN)
                message = client.messages \
                    .create(
                        body=f"Low price alert! Only {flight['price']} to fly from {flight['cityFrom']}-{flight['flyFrom']} to {flight['cityTo']}-{flight['flyTo']}!",
                        from_=PHONE_NUM,
                        to='+19253843787'
                    )
                print(message.status)

flight_search()