from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class FormsBot:
    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.url = url

    def send_form(self, address, price, link):
        self.driver.get(self.url)
        sleep(2)

        address_input = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_input = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link_input = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        submit = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div')

        address_input.send_keys(address)
        price_input.send_keys(price)
        link_input.send_keys(link)
        submit.click()