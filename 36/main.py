# - - - - - - - - - - IMPORT MODULES - - - - - - - - - - #
import os
from dotenv import load_dotenv, find_dotenv
import requests
load_dotenv(find_dotenv())

# - - - - - - - - - - SETUP VARIABLES - - - - - - - - - - #
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_URL = "https://www.alphavantage.co/query?"
API_PARAMS = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

# - - - - - - - - - - STOCK FUNCTION - - - - - - - - - - #
def stock_checker():
    res = requests.get(API_URL, params=API_PARAMS).json()
    last_two_days = list(res["Time Series (Daily)"].items())[:2]
    l2d_closing = []
    for day in last_two_days:
        close_price = float(day[1]["4. close"])
        l2d_closing.append(close_price)
    difference = abs(l2d_closing[0] - l2d_closing[1])
    percent_change = difference / l2d_closing[1]
    if percent_change > .05:
        print("Get News")
    

stock_checker()

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

