import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

url = "https://www.webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")
prod_name = soup.find_all("a",class_ = "title")
prod_names = [name.string for name in prod_name]
# print(len(prod_names))
prod_price = soup.find_all("h4",class_ = "float-end price card-title pull-right")
prod_prices = [price.string for price in prod_price]
# print(prod_prices)
prod_desc = soup.find_all("p",class_ = "description card-text")
prod_descs = [desc.string for desc in prod_desc]
# print(prod_descs)
prod_rev = soup.find_all("p",class_ = "float-end review-count")
prod_revs = [rev.string for rev in prod_rev]
# print(prod_revs)
df = pd.DataFrame({"Name":prod_names,"Price":prod_prices,"Description":prod_descs,"No_of_Reviews":prod_revs})
# print(df)

df.to_csv("C:/Users/USER/Desktop/product list.csv")