from datetime import datetime

import requests

USERNAME = "my_name"
TOKEN = "my_token"
GRAPH_ID = "graph1"


pixela_endpoint = "https://pixe.la/v1/users"

user_data = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_data)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_data = {
    "id": GRAPH_ID,
    "name": "book",
    "unit": "page",
    "type": "int",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(graph_endpoint, json=graph_data, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# today = datetime.now()
today = datetime(year=2021, month=1, day=1)

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many pages did you read today?: "),
}

# response = requests.post(pixel_endpoint, json=pixel_data, headers=headers)
# print(response.text)

date_to_update = datetime(year=2024, month=3, day=25)
pixel_update_endpoint = f"{pixel_endpoint}/{date_to_update.strftime('%Y%m%d')}"

pixel_update_data = {
    "quantity": "25"
}

# response = requests.put(pixel_update_endpoint, json=pixel_update_data, headers=headers)
# print(response.text)

# delete_endpoint = f"{pixel_endpoint}/{date_to_update.strftime('%Y%m%d')}"
# response = requests.delete(delete_endpoint, headers=headers)
# print(response.text)