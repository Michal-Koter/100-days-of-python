import os

import requests
from datetime import datetime, timedelta
from twilio.rest import Client

STOCK = "NVDA"
COMPANY_NAME = "NVIDIA Corporation"
ALPHAVANTAGE_API_KEY = os.environ.get("ALPHAVANTAGE_API_KEY")
ACCOUNT_SID_TWILIO = os.environ.get("TWILIO_SID")
AUTH_TOKEN_TWILIO = os.environ.get("TWILIO_AUTH")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
PHONE_NUMBER_FROM = "twilio_phone"
PHONE_NUMBER_TO = "my_phone"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
params_stock = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHAVANTAGE_API_KEY
}

response_stock = requests.get("https://www.alphavantage.co/query", params=params_stock)
response_stock.raise_for_status()
try:
    data_stock = response_stock.json()["Time Series (Daily)"]
except KeyError:
    print(response_stock.json())
    exit(1)

now = datetime.now()
yesterday = now - timedelta(days=1)
day_before = now - timedelta(days=2)

try:
    yesterday_data = data_stock[str(yesterday.date())]
    day_before_data = data_stock[str(day_before.date())]
except KeyError:
    print("The stock exchange was closed yesterday.")
    exit(1)

close_dict_key = "4. close"
change = float(yesterday_data[close_dict_key]) - float(day_before_data[close_dict_key])
change_percentage = abs(change) / float(yesterday_data[close_dict_key]) * 100

if change_percentage < 5:
    print("Share price change of less than 5%")
    exit(0)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

params_news = {
    "q": COMPANY_NAME,
    "pageSize": 3,
    "apiKey": NEWS_API_KEY
}

response_news = requests.get("https://newsapi.org/v2/everything", params=params_news)
response_news.raise_for_status()

data_news = response_news.json()["articles"]

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.

twilio_client = Client(ACCOUNT_SID_TWILIO, AUTH_TOKEN_TWILIO)
for news in data_news:
    emoji = "🔺" if change > 0 else "🔻"
    msg_text = (f"{STOCK}: {emoji}{change_percentage:.0f}\n"
                f"Headline: {news['title']})\n"
                f"Brief: {news['description']}")

    message = twilio_client.messages.create(
        body=msg_text,
        from_=PHONE_NUMBER_FROM,
        to=PHONE_NUMBER_TO
    )

    print(message.sid)
