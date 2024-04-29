from forms_bot import FormsBot
from zillow_scraper import ZillowScraper

ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSeSFW-8qznz_bApcYoIxDgJiH_mByvVmIpz0SFWAf3UFUTvjw/viewform?usp=sf_link"

if __name__ == "__main__":
    scraper = ZillowScraper(ZILLOW_URL)
    links = scraper.get_properties_links()
    print(f"There are {len(links)} links to individual listings in total: \n")
    print(links)

    prices = scraper.get_prices()
    print(f"\n After having been cleaned up, the {len(prices)} prices now look like this: \n")
    print(prices)

    addresses = scraper.get_addresses()
    print(f"\n After having been cleaned up, the {len(addresses)} addresses now look like this: \n")
    print(addresses)

    # data = [
    #     {
    #         "links": link,
    #         "prices": price,
    #         "address": address
    #     } for link, price, address in zip(links, prices, addresses)
    # ]

    bot = FormsBot(FORM_URL)
    for link, price, address in zip(links, prices, addresses):
        bot.send_form(address, price, link)
