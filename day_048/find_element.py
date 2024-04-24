from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.python.org/")

events = driver.find_elements(By.XPATH, "/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li")

event_dict = {
    idx: {
        "time": e.find_element(By.TAG_NAME, "time").text,
        "name": e.find_element(By.TAG_NAME, "a").text,
    } for idx, e in enumerate(events)
}
print(event_dict)

driver.close()