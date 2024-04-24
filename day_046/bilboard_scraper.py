import re
from datetime import datetime

import requests
from bs4 import BeautifulSoup


class BillboardScraper:
    def __init__(self):
        self.URL = "https://www.billboard.com/charts/hot-100"

    def get_hot_songs(self, date):
        match = re.search(r"^\d{4}-\d{2}-\d{2}$", date)

        if match is None:
            raise ValueError("Invalid date format")

        if datetime.strptime(date, "%Y-%m-%d") > datetime.now():
            raise ValueError("Invalid date, date must be in the past")

        response = requests.get(f"{self.URL}/{date}")
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        content = soup.find("div", class_="pmc-paywall")
        songs_spans = content.select("li ul li h3")
        return [song.getText().strip() for song in songs_spans]
