import requests
import time
from bs4 import BeautifulSoup
import urllib
import json
# from google.cloud import bigquery
# client = bigquery.Client()

table_id = "context-aware-system.clothingData.zara1"


# Set the URL you want to scrape from
URL = 'https://www.zara.com/ca/en/man-jackets-l640.html?v1=1445065'  # men jackets from Zara
#URL = 'https://www.zara.com/ca/en/woman-jeans-l1119.html?v1=1445721'  # men jackets from Zara

proxies = {
    "http": 'http://"58.84.164.230:53281'
}

# Connect to the URL
try:
	page = requests.get(URL,proxies=proxies)
except:
	print("Connnection error")

# Parse HTML and save to BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

#To download the whole data set,  do a for loop through all a tags
for i in range(len(soup.find_all('ul', class_='product-list _productList'))):  # 'a' tags are for items

        if URL.replace('https://www.zara.com/ca/en','').startswith("/woman") is True:
                product_gender = "Female"
        elif URL.replace('https://www.zara.com/ca/en','').startswith("/man") is True:
                product_gender = "Male"
        else: product_gender = "Unisex"

        product_name = soup.find_all('a', attrs={'class': 'name _item'})[i].text
        product_price_parse = soup.find_all("div", {"class": 'price _product-price'})[i].find_all("span", recursive=False)
        product_link = soup.find_all('a', attrs={'class': 'name _item'})[i]['href']
        product_img_link = soup.find_all('div', attrs={'class': 'product-grid-xmedia _product-grid-xmedia'})

        # j = 0
        # visit_for_image = requests.get(product_link)
        # soup2 = BeautifulSoup(visit_for_image.text, 'html.parser')

        dataDict = {
        	"product_ID":str(i),
        	"product_gender":product_gender,
        	"product_name":product_name
        }
        # print("\nproduct ID:") + str(i)
        # print("product gender: ") + product_gender
        # print ("product_name: ") + product_name

        print(dataDict)

        # print ("product_price_parse: ") + str(product_price_parse)
        # print ("product_link: ") + product_link
        print(product_img_link)
        # print ("product_img_link: https://") + (product_img_link.replace('//','')) #removes the first '//' from image link

        # table = client.get_table(table_id)  # Make an API request.
        # rows_to_insert = ["a",product_gender,product_name, str(product_price_parse), product_link, (product_img_link.replace('//',''))]

        # errors = client.insert_rows(table, rows_to_insert)  # Make an API request.
        # if errors == []:
        # 	print("New rows have been added.")


    # time.sleep(1)  # pause the code for a sec, so we dont get blocked for spamming
