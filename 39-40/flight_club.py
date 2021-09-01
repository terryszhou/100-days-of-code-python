# - - - - - - - - - - IMPORT MODULES - - - - - - - - - - #
import requests as req
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# - - - - - - - - - - SETUP VARIABLES - - - - - - - - - - #
SHEETY_ENDPOINT = "https://api.sheety.co/460f379ce0b4e690d10bdc36715fcddf/flightDeals/prices"

# - - - - - - - - - - FUNCTIONS - - - - - - - - - - #
res = req.get(SHEETY_ENDPOINT)
print(res.text)