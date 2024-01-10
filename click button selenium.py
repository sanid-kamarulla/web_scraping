from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

s = Service("C:/Users/USER/Downloads/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.truedatainsights.com/")

# wait for an element
element = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/div/div[1]/section[10]/div[2]/div/div[1]/div/div/div/div/div/div/a/div/img")))

# full x path
driver.find_element("xpath", """/html/body/div[1]/div/div[2]/div[3]/div/div[1]/section[10]/div[2]/div/div[1]/div/div/div/div/div/div/a/div/img""").click()

time.sleep(2)
driver.find_element("xpath", """""").click()


# Introduce a delay (e.g., 10 seconds) before closing the browser
time.sleep(60)  # Reduced sleep time to 10 seconds for a quicker example
