import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")
boxes = soup.find_all("div", class_ = "col-md-4 col-xl-4 col-lg-4")
# print(len(boxes))

# box = soup.find_all("div", class_ = "col-md-4 col-xl-4 col-lg-4")[2]
# print(box)
names = []
prices = []
descs = []
revs = []
rats = []
for i in range(len(boxes)):
    name = boxes[i].find("a", class_="title").string
    price = boxes[i].find("h4", class_="float-end price card-title pull-right").string
    desc = boxes[i].find("p", class_="description card-text").string
    rev = boxes[i].find("p", class_="float-end review-count").string
    rat = len(boxes[i].find_all("span", class_="ws-icon ws-icon-star"))
    names.append(name)
    prices.append(price)
    descs.append(desc)
    revs.append(rev)
    rats.append(rat)
df = pd.DataFrame({"Name":names,"Price":prices,"Description":descs,"No_of_Reviews":revs,"Rating":rats})
# print(df)

#extact data inside the nested html
sidebar = soup.find_all("ul", class_ = "nav flex-column",id = "side-menu")
# print(sidebar[0])
lists = sidebar[0].find_all("li", class_ = "nav-item")
print(lists[0])
values = lists[0].find_all("a", class_ = "nav-link")
print(values[0].string)




