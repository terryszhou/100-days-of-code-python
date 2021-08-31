# - - - - - - - - - - IMPORT MODULES - - - - - - - - - - #
import requests
import os
from datetime import datetime
from dotenv import load_dotenv, find_dotenv
from requests.api import head
load_dotenv(find_dotenv())

# - - - - - - - - - - SETUP VARIABLES - - - - - - - - - - #
TOKEN = os.environ.get("PIXELA_ACCT_TOKEN")
USERNAME = "terryszhou"
TODAY = datetime.now().strftime("%Y%m%d")

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
    "date": TODAY,
    "quantity": "100",
    "optionalData": "{\"rep/set max\":\"25\"}"
}

put_params = {
    "quantity": "50"
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

# post_pixel()

def put_pixel():
    response=requests.put(f"{pixel_endpoint}/{TODAY}", json=put_params, headers=headers)
    print(response.text)

# put_pixel()

def delete_pixel():
    response=requests.delete(f"{pixel_endpoint}/{TODAY}", headers=headers)
    print(response.text)

# delete_pixel()



