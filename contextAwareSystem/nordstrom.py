import requests
import time
from bs4 import BeautifulSoup
import re
import json
import urllib
from selenium import webdriver

# Harold driver
# driver = webdriver.Chrome('/Users/harold/Desktop/Project/WebScrapping/nordstrom/chromedriver')

# Jas driver
driver = webdriver.Chrome('/Users/x218850/Documents/capstone/contextAwareSystem/chromedriver')

#####################

switch_counter = 0
product_id = 0
constJSON=[{"store_name":"nordstrom", "clothing":[]}]

def url_link(switch_counter): #getting the first two pages sorted by customer rating
    switcher = {
        0: 'https://shop.nordstrom.com/c/mens-workout-activewear-clothing?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FActivewear&sort=CustomerRating',  # men activewear
        1: 'https://shop.nordstrom.com/c/mens-workout-activewear-clothing?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FActivewear&page=2&sort=CustomerRating'  # second page men activerwear
    }
    return switcher.get(switch_counter, "Invalid link")

while switch_counter < 2: #switch_counter < (number of url links)
        r = 0
        driver.get(url_link(switch_counter))
        selenium_html = driver.page_source
        # page = requests.get(url_link(switch_counter))
        # Parse HTML and save to BeautifulSoup object
        soup = BeautifulSoup(selenium_html, 'html.parser')

        for i in range(len(soup.find_all('article', class_='_1AOd3 QIjwE'))):  # 'a' tags are for items

            if url_link(switch_counter).replace('https://shop.nordstrom.com/c/', '').startswith("womens") is True:
                product_gender = "FEMALE"
            elif url_link(switch_counter).replace('https://shop.nordstrom.com/c/', '').startswith("mens") is True:
                product_gender = "MALE"
            else:
                product_gender = "UNISEX"

            if switch_counter == 0:
                product_category = "ACTIVEWEAR"
            elif switch_counter == 1:
                product_category = "ACTIVEWEAR"
            else:
                product_category = "NOT AVAILABLE"

            ############## PRICE #################
            j = 0
            product_price_parse = soup.find_all("div", {"class": 'YbtDD _3bi0z'})[i].find_all("span", recursive=False)

            if str(product_price_parse).find("Was") != -1:
                marked_down = ("YES")

                product_price_parse = str(soup.find_all("div", {"class": 'YbtDD _18N5Q'})[j].find_next().find_next("span", recursive=False))
                discount_percent_parse = str(soup.find_all("div", {"class": 'YbtDD _18N5Q'})[j].find_next().find_next().find_next("span", recursive=False))
                discount_percent = (re.sub("[^0123456789\.]", "", discount_percent_parse))[2:].strip()
                product_price = (re.sub("[^0123456789\.]", "", product_price_parse))[2:].strip()
                ++j
            else:
                marked_down = ("NO")

                discount_percent = 0
                product_price_parse = str(
                    soup.find_all("div", {"class": 'YbtDD _3bi0z'})[i].find_next().find_next("span", recursive=False))
                product_price = (re.sub("[^0123456789\.]", "", product_price_parse))[2:].strip()

            ##############
            ############## RATING #################


            item_parse = soup.findAll('article', class_='_1AOd3 QIjwE')[i].find_all("a", recursive=False) #gets all a tags from each item's class

            if str(item_parse).find("stars") != -1: #searching each item's class to find if a review exists, keyword is 'stars'

                number_of_reviews = (re.sub("[^0123456789\.]", "", soup.find_all('span', attrs={'class': '_3slKc'})[r].text)).strip()
                rating_parse = str(
                    soup.find_all("span", {"class": '_3slKc'})[r].find_next("span", recursive=False))

                start = '<span aria-label="'
                end = ' stars'
                rating = re.search('%s(.*)%s' % (start, end), rating_parse).group(1)
                r = r+1
            else:
                rating = "N/A"
                number_of_reviews = "N/A"

            ##############

            product_name = soup.find_all('h3', attrs={'class': 'Dawzg _28b4r'})[i].text
            product_link = "https://shop.nordstrom.com"+soup.find_all('a', attrs={'class': '_1av3_'})[i]['href']

            # print ("parse: ")+str(item_parse)
            print("\nproduct ID:") + str(product_id)
            print("gender: ") + product_gender
            print("category: ") + product_category
            print ("name: ") + product_name
            print ("marked-down: ") + marked_down
            print ("discount: ")+str(discount_percent)+"%"
            print ("price: ") + str(product_price)[:4]+" CAD"
            print ("rating: ") + str(rating)
            print ("reviews: ") + number_of_reviews
            print ("link: ") + product_link

            product_price_json = product_price[:4]

            # product_id += 1


            dataDict = {
                    "id":str(product_id),
                    "gender":product_gender,
                    "category":product_category,
                    "name":product_name,
                    "marked-down": marked_down,
                    "discount percent": discount_percent,
                    "price":float(product_price_json),
                    "rating":str(rating),
                    "reviews":number_of_reviews,
                    "link":product_link,
                    #"img":(product_img_link.replace('//',''))
            }

            product_id += 1

            constJSON[0]["clothing"].append(dataDict)
            # #time.sleep(1.5)  # pause the code for 1.5 sec, so we dont get blocked for spamming

        print(json.dumps(constJSON))
        switch_counter += 1

        if switch_counter > 1:
            with open("nordstrom.json", "w") as f:
                print(json.dumps(constJSON))
                json.dump(constJSON, f)


