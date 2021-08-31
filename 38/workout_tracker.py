# - - - - - - - - - - IMPORT MODULES - - - - - - - - - - #
import requests
import os
from datetime import datetime
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())

# - - - - - - - - - - SETUP VARIABLES - - - - - - - - - - #
API_ID = os.environ.get("NUTRITIONIX_ID")
API_KEY = os.environ.get("NUTRITIONIX_API_KEY")

# - - - - - - - - - - FUNCTIONS - - - - - - - - - - #


