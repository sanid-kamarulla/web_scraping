import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.iplt20.com/auction/2022"
r = requests.get(url)

soup = BeautifulSoup(r.text,"lxml")
# print(r)

ipl_table = soup.find_all("table", class_ = "ih-td-tab auction-tbl")[0]
# print(ipl_table)
headers = [header.text for header in ipl_table.find_all("th")]
# print(headers)

df = pd.DataFrame(columns = headers)
# print(df)

rows = ipl_table.find_all("tr")
# print(rows)
# print(len(rows))
# for i in range(len(rows)-1):
#     # print([row.text for row in rows[i+1].find_all("td")])
#     each_row = [row.text for row in rows[i+1].find_all("td")]
#     l = len(df)
#     df.loc[l] = each_row
# df.iloc[:,0] = df.iloc[:,0].str.replace('\n','')

for i in rows[1:]:
    first_col = i.find_all("td")[0].text.replace('\n','')
    remaining_col = [row.text for row in i.find_all("td")[1:]]
    remaining_col.insert(0,first_col)
    l = len(df)
    df.loc[l] = remaining_col

# print(df)
df.to_excel("C:/Users/USER/Desktop/IPL Auction table.xlsx", index=False)