from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

s = Service("C:/Users/USER/Downloads/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.nike.com/in/w/mens-shoes-nik1zy7ok")

# take a screenshot
time.sleep(2)

while True:
    height = driver.execute_script("return document.body.scrollHeight")
    print(height)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    new_height = driver.execute_script("return document.body.scrollHeight")
    # print(new_height)
    if height == new_height:
        break
    # Introduce a delay (e.g., 10 seconds) before closing the browser
    time.sleep(10)  # Reduced sleep time to 10 seconds for a quicker example

time.sleep(60)  # Reduced sleep time to 10 seconds for a quicker example
