# - - - - - - - - - - IMPORT MODULES - - - - - - - - - - #
import requests
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# - - - - - - - - - - SETUP VARIABLES - - - - - - - - - - #
pixela_endpoint = "https://pixe.la/v1/users"
token = os.environ.get("PIXELA_ACCT_TOKEN")
user_params = {
    "token": token,
    "username": "terryszhou",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# - - - - - - - - - - FUNCTION - - - - - - - - - - #
def habit_tracker():
    response = requests.post(pixela_endpoint, json=user_params)
    print(response.text)

habit_tracker()