from time import sleep
import os

from selenium import webdriver
from selenium.common import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

EMAIL = os.environ.get('EMAIL')
PASSWORD = os.environ.get('PASS')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://tinder.com/")
sleep(2)
driver.find_element(By.XPATH, '//*[@id="o515699397"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a').click()
sleep(2)


driver.find_element(By.XPATH, value='//*[@id="o-1212681679"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button').click()
sleep(2)
base_window = driver.window_handles[0]
fb_window = driver.window_handles[1]

driver.switch_to.window(fb_window)
sleep(2)
email = driver.find_element(By.XPATH, value='//*[@id="email"]')
password = driver.find_element(By.XPATH, value='//*[@id="pass"]')
email.send_keys(EMAIL)
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
sleep(2)
driver.find_element(By.XPATH, value='//*[@id="o-1212681679"]/main/div[1]/div/div/div[3]/button[1]').click()
sleep(2)
driver.find_element(By.XPATH, value='//*[@id="o-1212681679"]/main/div[1]/div/div/div[3]/button[2]').click()
sleep(2)
driver.find_element(By.XPATH, value='//*[@id="o515699397"]/div/div[2]/div/div/div[1]/div[2]/button').click()

for n in range(100):
    sleep(1)

    try:
        print("called")
        driver.find_element(By.XPATH, value='//*[@id="o515699397"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button').click()
    except ElementClickInterceptedException:
        try:
            driver.find_element(By.CSS_SELECTOR, value='//*[@id="o846070598"]/main/div/div[1]/div/div[4]/button').click()
        except NoSuchElementException:
            sleep(2)
driver.quit()