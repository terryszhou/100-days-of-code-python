# - - - - - - - - - - IMPORT MODULES - - - - - - - - - - #
import requests as req
import os
from datetime import datetime
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())

# - - - - - - - - - - SETUP VARIABLES - - - - - - - - - - #
APP_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
APP_ID = os.environ.get("NUTRITIONIX_ID")
APP_KEY = os.environ.get("NUTRITIONIX_API_KEY")
req_body = {
    "query": "",
    "gender": "male",
    "weight_kg": 79.4,
    "height_cm": 177.8,
    "age": 27
}
headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

# - - - - - - - - - - FUNCTIONS - - - - - - - - - - #
def workout_tracker():
    global req_body
    user_input = input("Tell me what exercises you did: ")
    req_body["query"] = user_input
    res = req.post(APP_ENDPOINT, req_body, headers=headers)
    print(res.json())

workout_tracker()

