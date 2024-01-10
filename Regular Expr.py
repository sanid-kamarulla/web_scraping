import requests
from bs4 import BeautifulSoup
import re

url = "https://www.webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)

soup = BeautifulSoup(r.text,"lxml")

# print data inside multiple tags
data = soup.find_all(["h4", "p", "a"])
# print(data)

# search for a string
data = soup.find_all(string = "Galaxy Tab")
# print(data)

# use regular expressions
data = soup.find_all(string = re.compile("Galaxy"))
print(data)