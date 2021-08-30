# - - - - - - - - - - IMPORT MODULES - - - - - - - - - - #
import os
from dotenv import load_dotenv, find_dotenv
import requests
from twilio.rest import Client

load_dotenv(find_dotenv())

# - - - - - - - - - - SETUP VARIABLES - - - - - - - - - - #
COMPANY_NAME = "Tesla Inc"
STOCK = "TSLA"
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
STOCK_URL = "https://www.alphavantage.co/query?"
STOCK_PARAMS = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

ACCT_SID = os.environ.get("TWILIO_ACCT_SID")
AUTH_TOKEN = os.environ.get("TWILIO_ACCT_TOKEN")
PHONE_NUM = "+15406251609"

# - - - - - - - - - - STOCK FUNCTION - - - - - - - - - - #
def stock_checker():
    res = requests.get(STOCK_URL, params=STOCK_PARAMS).json()
    last_two_days = list(res["Time Series (Daily)"].items())[:2]
    l2d_closing = []
    for day in last_two_days:
        close_price = float(day[1]["4. close"])
        l2d_closing.append(close_price)
    difference = abs(l2d_closing[0] - l2d_closing[1])
    percent_change = difference / l2d_closing[1]
    if percent_change > .05:
        print("Get News")
        news_res = requests.get(f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&from={last_two_days[1][0]}&sortBy=publishedAt&apiKey={NEWS_API_KEY}").json()
        news_articles = news_res["articles"][:3]
        news_dict = {}
        for article in news_articles:
            news_dict[article["title"]] = article["description"]
        message_body = ""
        for key, value in news_dict.items():
            message_body += f"\n\n{key}: {value}"
        client = Client(ACCT_SID, AUTH_TOKEN)
        message = client.messages \
            .create(
                body=f"{COMPANY_NAME} Percent Change: {round(percent_change, 2)}\n{message_body}",
                from_=PHONE_NUM,
                to='+19253843787'
            )
        print(message.status)

stock_checker()