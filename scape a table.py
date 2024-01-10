import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.premierleague.com/tables"
r = requests.get(url)
# print(r)

soup = BeautifulSoup(r.text,"lxml")

pl_table = soup.find("table")
headers = pl_table.find_all("th")
all_headers = [header.text.split('\n')[1] if '\n' in header.text else header.text for header in headers]
# print(all_headers)
# print(len(all_headers))
df = pd.DataFrame(columns = all_headers)
# print(df)
# print(len(df))

rows = pl_table.find_all("tr")
# print(int((len(rows)-1)*0.5))
# each_row = rows[1].find_all("td")
for i in range(int((len(rows)-1)*0.5)):
    each_row = [row.text for row in rows[2*i+1].find_all("td")]
    # print(len(each_row))
    l = len(df)
    df.loc[l] = each_row


df.iloc[:,0] = df.iloc[:,0].str.split('\n').str[1]
df.iloc[:,1] = df.iloc[:,1].str.split('\n').str[8]
df.iloc[:,8] = df.iloc[:,8].str.split('\n').str[1]
df.iloc[:,10] = df.iloc[:,10].str.replace('\n','').str[0]
df.iloc[:,11] = df.iloc[:,11].str.split('\n').str[5]
df_pl = df.iloc[:,:12]
# print(df_pl)

df_pl.to_excel("C:/Users/USER/Desktop/PL table.xlsx", index=False)