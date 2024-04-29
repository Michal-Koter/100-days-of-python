from bs4 import BeautifulSoup
import requests


class ZillowScraper:
    def __init__(self, url):
        self.url = url
        self.header = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
        }

    def __get_soup(self, url, headers):
        response = requests.get(self.url, headers=headers)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')

    def get_properties_links(self):
        soup = self.__get_soup(self.url, self.header)
        link_elements = soup.select(".StyledPropertyCardDataWrapper a")

        return [link["href"] for link in link_elements]

    def get_prices(self):
        soup = self.__get_soup(self.url, self.header)
        price_elements = soup.select(".StyledPropertyCardDataWrapper span")

        return [element.get_text(strip=True)[:6] for element in price_elements]

    def get_addresses(self):
        soup = self.__get_soup(self.url, self.header)

        address_elements = soup.find_all("address")

        return [address.get_text(strip=True).replace(" | ", " ") for address in address_elements]
