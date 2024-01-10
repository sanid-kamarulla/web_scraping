import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time

result_df = pd.DataFrame()
for i in range(1, 11):

    url = "https://www.flipkart.com/search?q=mobiles+under+7000&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_14_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_14_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=mobiles+under+7000%7CMobiles&requestId=436a54d4-b8ce-4f30-bf61-2764d6ba2213&as-searchtext=mobiles+under+&page=" + str(i)
    print(url)
    print(i)
    r = requests.get(url)
    # print(r)

    soup = BeautifulSoup(r.text,"lxml")
    print(len(soup))

    headers = ['Current timestamp','Name', 'Price', 'Offer', 'Rating', 'Number of Rating', 'Number of Reviews', 'Description']
    df = pd.DataFrame(columns=headers)
    box = soup.find_all("div", class_ = "_3pLy-c row")
    print(len(box))
    for l in range(len(box)):
        current_timestamp = time.time()
        if box[l].find("div", class_ = "_4rR01T") is not None:
            Name = box[l].find("div", class_ = "_4rR01T").text
        else:
            Name = 'NULL'
        if box[l].find("div", class_ = "_30jeq3 _1_WHN1") is not None:
            Price = box[l].find("div", class_="_30jeq3 _1_WHN1").text
        else:
            Price = 'NULL'
        if box[l].find("div", class_ = "_3Ay6Sb") is not None:
            offer = box[l].find("div", class_ = "_3Ay6Sb").text
        else:
            offer = 'NULL'
        if box[l].find("div", class_ = "_3LWZlK") is not None:
            Rating = box[l].find("div", class_ = "_3LWZlK").text
        else:
            Rating = 'NULL'
        if box[l].find("span", class_ = "_2_R_DZ") is not None:
            No_Ratings = box[l].find("span", class_ = "_2_R_DZ").text.split(' ')[0]
        else:
            No_Ratings = 'NULL'
        if box[l].find("span", class_ = "_2_R_DZ") is not None:
            No_Reviews = re.findall(r'\d[\d,]*', box[l].find("span", class_ = "_2_R_DZ").text)[-1]
        else:
            No_Reviews = 'NULL'
        if box[l].find("div", class_ = "fMghEO") is not None:
            Description = box[l].find("div", class_ = "fMghEO").text
        else:
            Description = 'NULL'
        each_row = [current_timestamp, Name, Price, offer, Rating, No_Ratings, No_Reviews, Description]
        df.loc[l] = each_row
    result_df = result_df._append(df, ignore_index=True)
print(result_df)

result_df.to_excel("C:/Users/USER/Desktop/Phone under 7000.xlsx", index=False)
