import requests
import time
from bs4 import BeautifulSoup
import urllib

# Set the URL you want to scrape from
URL = 'https://www.zara.com/ca/en/man-jackets-l640.html?v1=1445065'  # men jackets from Zara
#URL = 'https://www.zara.com/ca/en/woman-jeans-l1119.html?v1=1445721'  # men jackets from Zara


# Connect to the URL
page = requests.get(URL)

# Parse HTML and save to BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

#To download the whole data set,  do a for loop through all a tags
for i in range(len(soup.find_all('div', class_='product-info _product-info'))):  # 'a' tags are for items

        if URL.replace('https://www.zara.com/ca/en','').startswith("/woman") is True:
                product_gender = "Female"
        elif URL.replace('https://www.zara.com/ca/en','').startswith("/man") is True:
                product_gender = "Male"
        else: product_gender = "Unisex"

        product_name = soup.find_all('a', attrs={'class': 'name _item'})[i].text
        product_price_parse = soup.find_all("div", {"class": 'price _product-price'})[i].find_all("span", recursive=False)
        product_link = soup.find_all('a', attrs={'class': 'name _item'})[i]['href']

        j = 0
        visit_for_image = requests.get(product_link)
        soup2 = BeautifulSoup(visit_for_image.text, 'html.parser')
        product_img_link = soup2.find_all('meta', attrs={'property': 'og:image'})[j]['content']
        ++j

        print("\nproduct ID:") + str(i)
        print("product gender: ") + product_gender
        print ("product_name: ") + product_name
        print ("product_price_parse: ") + str(product_price_parse)

        print ("product_link: ") + product_link
        print ("product_img_link: https://") + (product_img_link.replace('//','')) #removes the first '//' from image link
    # time.sleep(1)  # pause the code for a sec, so we dont get blocked for spamming
