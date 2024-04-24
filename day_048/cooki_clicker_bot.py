from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")

store_items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in store_items]

timeout = time.time() + 5
five_min = time.time() + 60*5

continue_game = True
while continue_game:
    cookie.click()

    if time.time() > timeout:
        all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
        item_prices = []

        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = element_text.split("-")[1]
                cost = cost.strip()
                cost = cost.replace(",", "")
                item_prices.append(int(cost))

        upgrades = {}
        for n in range(len(item_prices)):
            upgrades[item_prices[n]] = item_ids[n]

        money_element = driver.find_element(by=By.ID, value="money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        my_cookies = int(money_element)

        affordable_upgrades = {}
        for cost, idx in upgrades.items():
            if my_cookies > cost:
                affordable_upgrades[cost] = idx

        try:
            highest_price_affordable_upgrade = max(affordable_upgrades)
        except ValueError:
            pass
        else:
            to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
            driver.find_element(by=By.ID, value=to_purchase_id).click()

        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break
