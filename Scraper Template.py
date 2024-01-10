import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time

class FlipkartScraper:
    def __init__(self):
        self.result_df = pd.DataFrame()
        self.headers = ['Current timestamp', 'Name', 'Price', 'Offer', 'Rating', 'Number of Rating', 'Number of Reviews', 'Description']

    def scrape_page(self, page_number):
        url = f"https://www.flipkart.com/search?q=mobiles+under+7000&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_14_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_14_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=mobiles+under+7000%7CMobiles&requestId=436a54d4-b8ce-4f30-bf61-2764d6ba2213&as-searchtext=mobiles+under+&page={page_number}"
        print(url)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml")
        self.extract_data(soup)

    def extract_data(self, soup):
        df = pd.DataFrame(columns=self.headers)
        box = soup.find_all("div", class_="_3pLy-c row")

        for l in range(len(box)):
            current_timestamp = time.time()
            Name = self.get_text(box[l], "_4rR01T")
            Price = self.get_text(box[l], "_30jeq3 _1_WHN1")
            offer = self.get_text(box[l], "_3Ay6Sb")
            Rating = self.get_text(box[l], "_3LWZlK")
            No_Ratings = self.get_text(box[l], "_2_R_DZ", split=True)
            No_Reviews = self.get_reviews(box[l])
            Description = self.get_text(box[l], "fMghEO")

            each_row = [current_timestamp, Name, Price, offer, Rating, No_Ratings, No_Reviews, Description]
            df.loc[l] = each_row

        self.result_df = self.result_df._append(df, ignore_index=True)

    def get_text(self, element, class_name, split=False):
        found_element = element.find("div", class_=class_name)
        if found_element is not None:
            text = found_element.text
            return text.split(' ')[0] if split else text
        else:
            return 'NULL'

    def get_reviews(self, element):
        found_element = element.find("span", class_="_2_R_DZ")
        if found_element is not None:
            return re.findall(r'\d[\d,]*', found_element.text)[-1]
        else:
            return 'NULL'

if __name__ == "__main__":
    flipkart_scraper = FlipkartScraper()

    for i in range(1, 11):
        flipkart_scraper.scrape_page(i)

    print(flipkart_scraper.result_df)
