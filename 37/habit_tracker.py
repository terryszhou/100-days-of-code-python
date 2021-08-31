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

pixel_endpoint = f"{graph_endpoint}/{graph_params['id']}"
pixel_params = {
    "date": "20210830",
    "quantity": "100",
    "optionalData": "{\"rep/set max\":\"25\"}"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# - - - - - - - - - - FUNCTIONS - - - - - - - - - - #
def create_pixela_acct():
    response = requests.post(pixela_endpoint, json=user_params)
    print(response.text)

# create_pixela_acct()

def create_pixela_graph():
    response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
    print(response.text)

# create_pixela_graph()

def post_pixel():
    response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
    print(response.text)

post_pixel()

