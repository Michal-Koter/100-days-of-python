from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://secure-retreat-92358.herokuapp.com/")

driver.find_element(By.CLASS_NAME, "top").send_keys("my_firstname")
driver.find_element(By.CLASS_NAME, "middle").send_keys("my_lastname")
driver.find_element(By.CLASS_NAME, "bottom").send_keys("my_email@gmail.com")

driver.find_element(By.TAG_NAME, "button").click()