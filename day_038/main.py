import os
from datetime import datetime

import requests

NUTRITIONIX_APP_ID = os.environ["NT_APP_ID"]
NUTRITIONIX_API_KEY = os.environ["NT_API_KEY"]

AGE = 21
HEIGHT = 175
WEIGHT = 80

nutritionix_headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutritionix_body = {
    "query": input("Tell me which exercise you did: "),
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

nutritionix_response = requests.post(nutritionix_endpoint, json=nutritionix_body, headers=nutritionix_headers)
nutritionix_response.raise_for_status()
exercises = nutritionix_response.json()["exercises"]
print(nutritionix_response.json())


sheety_endpoint = os.environ["SHEET_ENDPOINT"]

sheety_headers = {
    "Authorization": f"Basic {os.environ['TOKEN']}"
}

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
for row in exercises:
    sheety_body = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": row["name"],
            "duration": row["duration_min"],
            "calories": row["nf_calories"]
        }
    }

    sheety_response = requests.post(sheety_endpoint, json=sheety_body, headers=sheety_headers)
    sheety_response.raise_for_status()
    print(sheety_response.json())
