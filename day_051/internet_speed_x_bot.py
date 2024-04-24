import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(2)
        self.driver.find_element(By.ID, "onetrust-reject-all-handler").click()

        start_button = self.driver.find_element(By.CSS_SELECTOR, "div.start-button > a")
        start_button.click()

    def tweet_at_provider(self):
            pass
