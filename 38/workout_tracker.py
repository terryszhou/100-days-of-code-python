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
TODAY = datetime.now().strftime("%d/%m/%Y")
NOW = datetime.now().strftime("%H:%M:%S")
REQ_BODY = {
    "query": "",
    "gender": "male",
    "weight_kg": 79.4,
    "height_cm": 177.8,
    "age": 27
}

APP_HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

SHEETY_HEADERS = {
    "Authorization" : "Basic dGVycnlzemhvdToxNFxsKytkbjM/NjkyMDY3"
}

SHEETY_ENDPOINT = "https://api.sheety.co/460f379ce0b4e690d10bdc36715fcddf/myWorkouts/workouts"

# - - - - - - - - - - FUNCTIONS - - - - - - - - - - #
def workout_tracker():
    global REQ_BODY
    user_input = input("Tell me what exercises you did: ")
    REQ_BODY["query"] = user_input
    workout_res = req.post(APP_ENDPOINT, REQ_BODY, headers=APP_HEADERS)
    workout_req_body = {
        "workout": {
            'date': TODAY,
            'time': NOW,
            'exercise': workout_res.json()["exercises"][0]["user_input"].capitalize(),
            'duration': workout_res.json()["exercises"][0]["duration_min"],
            'calories': workout_res.json()["exercises"][0]["nf_calories"],
        }
    }
    sheety_res = req.post(SHEETY_ENDPOINT, json=workout_req_body, headers=SHEETY_HEADERS)
    print(sheety_res.text)

workout_tracker()

# - - - - - - - - - - SAMPLE JSON DATA FORMATS - - - - - - - - - - #
{
    'exercises': [{
        'tag_id': 825,
        'user_input': 'pullups',
        'duration_min': 8.33,
        'met': 3.8,
        'nf_calories': 41.89,
        'photo': {'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/825_highres.jpg',
        'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/825_thumb.jpg',
        'is_user_uploaded': False},
        'compendium_code': 2022,
        'name': 'pull-up',
        'description': None,
        'benefits': None
    }]
}

{
    'workouts': {
        'date': '21/07/2020',
        'time': '15:00:00',
        'exercise': 'Running',
        'duration': 22,
        'calories': 130,
    }
}