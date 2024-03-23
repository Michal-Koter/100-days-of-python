import requests
from twilio.rest import Client
import os

account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_AUTH")


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
    twilio_client = Client(account_sid, auth_token)
    message = twilio_client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella",
        from_="+16502414415",
        to="+420733702820"
    )

    print(message.sid)