import requests
import time
from bs4 import BeautifulSoup
import re
import urllib

# Set the URL you want to scrape from
URL = 'https://www.zara.com/ca/en/man-shirts-l737.html?v1=1445099'  # men shirts from Zara

proxies = {
    "http": 'http://"58.84.164.230:53281'
}

# Connect to the URL
try:
    page = requests.get(URL, proxies=proxies)
except:
    print("Connnection error")

# Parse HTML and save to BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

# To download the whole data set,  do a for loop through all a tags
for i in range(len(soup.find_all('div', class_='product-info _product-info'))):  # 'a' tags are for items

    if URL.replace('https://www.zara.com/ca/en', '').startswith("/woman") is True:
        product_gender = "Female"
    elif URL.replace('https://www.zara.com/ca/en', '').startswith("/man") is True:
        product_gender = "Male"
    else:
        product_gender = "Unisex"

    product_name = soup.find_all('a', attrs={'class': 'name _item'})[i].text
    product_price_parse = soup.find_all("div", {"class": 'price _product-price'})[i].find_all("span", recursive=False)

    if str(product_price_parse).find("sale") != -1:
        marked_down = ("YES")

        product_price_text = str(
            soup.find_all("div", {"class": 'price _product-price'})[i].find_next().find_next("span", recursive=False))
        product_price = re.sub("[^0123456789\.]", "", product_price_text).strip()

    else:
        marked_down = ("NO")

        product_price_text = str(
            (soup.find_all("div", {"class": 'price _product-price'})[i].find_all("span", recursive=False)))
        product_price = re.sub("[^0123456789\.]", "", product_price_text).strip()

    product_link = soup.find_all('a', attrs={'class': 'name _item'})[i]['href']

    j = 0
    visit_for_image = requests.get(product_link)
    soup2 = BeautifulSoup(visit_for_image.text, 'html.parser')
    product_img_link = soup2.find_all('meta', attrs={'property': 'og:image'})[j]['content']
    ++j

    print("\nproduct ID:") + str(i)
    print("product gender: ") + product_gender
    print ("product name: ") + product_name
    #print ("product price_parse: ") + str(product_price_parse) #this is the main tag for prices, it shows the price whether is on sale or not, uncomment to check if 'product_price' is correct
    print ("product marked-down: ") + marked_down
    print ("product price: ") + product_price + " CAD"
    print ("product link: ") + product_link
    print ("product imgage link: https://") + (product_img_link.replace('//','')) #removes the first '//' from image link
    time.sleep(1.5)  # pause the code for 1.5 sec, so we dont get blocked for spamming
