import os
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


URL = "https://www.instagram.com"
SIMILAR_ACCOUNT = "crumblcookies"
USERNAME = os.environ.get("INST_USER")
PASSWORD = os.environ.get("INST_PASSWORD")


class InstagramBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(chrome_options)

    def login(self):
        self.driver.get(URL)
        sleep(5)

        self.driver.find_element(By.XPATH,
                                 '/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]').click()

        sleep(2)

        self.driver \
            .find_element(By.XPATH,
                          '/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input') \
            .send_keys(USERNAME)

        self.driver \
            .find_element(By.NAME, "password").send_keys(PASSWORD, Keys.ENTER)
        sleep(5)

    def fallow(self):
        container = self.driver.find_element(By.XPATH,
                                             "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]")
        buttons = container.find_elements(By.TAG_NAME, "button")
        for button in buttons:
            try:
                button.click()
                sleep(2)
            except ElementClickInterceptedException:
                self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Anuluj')]").click()
                sleep(2)
                button.click()
                sleep(2)

        print(len(buttons))


if __name__ == '__main__':
    bot = InstagramBot()
    bot.login()
    bot.fallow()
