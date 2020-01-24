import requests
import time
from bs4 import BeautifulSoup

# Set the URL you want to scrape from
URL = 'https://www.zara.com/ca/en/man-jackets-l640.html?v1=1445065' #men jackets from Zara

# Connect to the URL
page = requests.get(URL)

# Parse HTML and save to BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

# To download the whole data set,  do a for loop through all a tags
for i in range(len(soup.find_all('a', class_ = 'item _item'))): #'a' tags are for items


    product_name = soup.findAll('a', attrs={'class': 'name _item'})[i].text
    product_price = soup.findAll('span', attrs={'class': 'main-price'})[i]['data-price']
    product_link = soup.findAll('a', attrs={'class': 'name _item'})[i]['href']

    print("\nProduct ID:") + str(i)
    print ("product_name: ") + product_name
    print ("product_price: ") + product_price
    print ("product_link: ") + product_link
    #time.sleep(1)  # pause the code for a sec, so we dont get blocked for spamming


