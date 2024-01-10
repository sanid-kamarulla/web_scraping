import requests
from bs4 import BeautifulSoup
import pandas as pd

result_df = pd.DataFrame()
for i in range(2, 12):
# i = 5
    url = "https://www.flipkart.com/search?q=mobiles+under+7000&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_14_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_14_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=mobiles+under+7000%7CMobiles&requestId=436a54d4-b8ce-4f30-bf61-2764d6ba2213&as-searchtext=mobiles+under+&page=" + str(i)
    r = requests.get(url)
    # print(r)

    soup = BeautifulSoup(r.text,"lxml")
    # print(soup)

    np_link = soup.find("a", class_ = "_1LKTO3").get("href")
    full_nplink = "https://www.flipkart.com" + np_link
    print(full_nplink)

