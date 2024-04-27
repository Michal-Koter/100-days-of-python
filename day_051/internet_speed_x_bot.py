import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class InternetSpeedTwitterBot:
    def __init__(self, promised_down, promised_up):
        self.promised_down = promised_down
        self.promised_up = promised_up

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(2)
        self.driver.find_element(By.ID, "onetrust-reject-all-handler").click()

        start_button = self.driver.find_element(By.CSS_SELECTOR, "div.start-button > a")
        start_button.click()
        time.sleep(60)

        self.down = float(self.driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
        self.up = float(self.driver.find_element(By.XPATH,
                                           '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)

        print(f"Down: {self.down}")
        print(f"Up: {self.up}")

    def tweet_at_provider(self, email, password):
        if self.down >= self.promised_down and self.up >= self.promised_up:
            pass

        message = f"Hey my ISP, why is my internet speed {self.down}down/{self.up}up when I pay for {self.promised_down}down/{self.promised_up}up?"

        self.driver.get("https://twitter.com/i/flow/login")

        time.sleep(2)
        self.driver \
            .find_element(By.XPATH,
                          '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input') \
            .send_keys(email, Keys.ENTER)

        time.sleep(30)
        self.driver \
            .find_element(By.XPATH,
                          '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input') \
            .send_keys(password, Keys.ENTER)

        time.sleep(5)

        self.driver \
            .find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div') \
            .send_keys(message)

        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]').click()