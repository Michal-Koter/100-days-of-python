import requests
from twilio.rest import Client
import os

ACCOUNT_SID = os.environ.get("TWILIO_SID")
AUTH_TOKEN = os.environ.get("TWILIO_AUTH")
PHONE_NUMBER_FROM = "twilio_phone"
PHONE_NUMBER_TO = "my_phone"

weather_param = {
    "lat": 54.352024,
    "lon": 18.646639,
    "appid": os.environ.get("OWM_API_KEY"),
    "cnt": 4
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=weather_param)
response.raise_for_status()

weather_data = response.json()
# print(weather_data)
will_rain = False
for data in weather_data["list"]:
    condition_code = data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        break

if will_rain:
    twilio_client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = twilio_client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella",
        from_="twilio_phone",
        to=""
    )

    print(message.sid)