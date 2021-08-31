# - - - - - - - - - - IMPORT MODULES - - - - - - - - - - #
import requests
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# - - - - - - - - - - SETUP VARIABLES - - - - - - - - - - #
TOKEN = os.environ.get("PIXELA_ACCT_TOKEN")
USERNAME = "terryszhou"
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id": "graph1",
    "name": "Pullups Graph",
    "unit": "reps",
    "type": "int",
    "color": "shibafu"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# - - - - - - - - - - FUNCTION - - - - - - - - - - #
def create_pixela_acct():
    response = requests.post(pixela_endpoint, json=user_params)
    print(response.text)

# create_pixela_acct()

def habit_tracker():
    response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
    print(response.text)

habit_tracker()