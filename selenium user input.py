from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

s = Service("C:/Users/USER/Downloads/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.google.com/")

# take a screenshot
time.sleep(2)
driver.save_screenshot("C:/Users/USER/Desktop/Web Scraping/google landing page.png")
# screenshot of an element
driver.find_element("xpath", """/html/body/div[1]/div[2]/div/img""").screenshot("C:/Users/USER/Desktop/Web Scraping/google doodle.png")

# Introduce a delay (e.g., 10 seconds) before clicking the button
time.sleep(2)

# full x path
search = driver.find_element("xpath", """/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/div/textarea""")
search.send_keys("truedatainsights.com")
search.send_keys(Keys.ENTER)

# Introduce a delay (e.g., 10 seconds) before closing the browser
time.sleep(60)  # Reduced sleep time to 10 seconds for a quicker example

