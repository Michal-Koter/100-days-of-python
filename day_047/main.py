import os
import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

URL = "https://www.amazon.pl/LEGO-Icons-W%C5%81ADCA-PIER%C5%9ACIENI-minifigurkami/dp/B0BVMZ5NT5"
TARGET_PRICE = 1500
SMTP_SERVER = "smtp.gmail.com"
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("EMAIL_PASS")


headers = {
    "Accept-Language": "pl-PL,pl;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

response = requests.get(URL)
response.raise_for_status()

soup = BeautifulSoup(response.text, "lxml")
# print(soup.prettify())

title = soup.find(id="productTitle").get_text().strip()
# print(title)

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("zł")[0]
price_splited = price_without_currency.split("\xa0")
price_without_space = price_splited[0] + price_splited[1]
price_without_space = price_without_space.replace(",", ".")

price_as_float = float(price_without_space)
# print(price_as_float)

if price_as_float < TARGET_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(SMTP_SERVER) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon Price Alert! Buy now!\n\n{message}\n{URL}".encode("utf-8")
        )
