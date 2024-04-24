import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")

titles = soup.select("h3")

title_list = [title.getText() for title in titles]
title_list = title_list[::-1]

with open("movies.txt", "w") as file:
    for t in title_list:
        file.write(f"{t}\n")
