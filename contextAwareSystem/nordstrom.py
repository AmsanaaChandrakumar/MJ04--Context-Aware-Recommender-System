# coding: utf-8
import requests
import time
from bs4 import BeautifulSoup
import re
import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


# Harold driver
driver = webdriver.Chrome('/Users/harold/Desktop/Project/WebScrapping/nordstrom/chromedriver')

# # Jas driver
# driver = webdriver.Chrome('/Users/x218850/Documents/capstone/contextAwareSystem/chromedriver')

#####################

switch_counter = 0
product_id = 0
constJSON=[{"store_name":"nordstrom", "clothing":[]}]

def url_link(switch_counter):
    switcher = {
        0:'https://shop.nordstrom.com/c/womens-activewear-shop?origin=topnav&breadcrumb=Home%2FWomen%2FClothing%2FActivewear&offset=3&page=13&sort=CustomerRating',
        # 0:'https://shop.nordstrom.com/c/mens-workout-activewear-clothing?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FActivewear&sort=CustomerRating', #me activewear page 1
        1:'https://shop.nordstrom.com/c/mens-workout-activewear-clothing?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FActivewear&page=2&sort=CustomerRating', #men activewear page 2
        2: 'https://shop.nordstrom.com/c/womens-activewear-shop?origin=topnav&breadcrumb=Home%2FWomen%2FClothing%2FActivewear&offset=3&sort=CustomerRating', #women activewear page 1
        # 3: 'https://shop.nordstrom.com/c/womens-activewear-shop?origin=topnav&breadcrumb=Home%2FWomen%2FClothing%2FActivewear&offset=3&page=2&sort=CustomerRating',#women activewear page 2
        # 4: 'https://shop.nordstrom.com/c/mens-blazers-sportcoats?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FBlazers%20%26%20Sport%20Coats&offset=1&sort=CustomerRating', #men blazers/coats page 1
        # 5: 'https://shop.nordstrom.com/c/mens-blazers-sportcoats?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FBlazers%20%26%20Sport%20Coats&offset=1&page=2&sort=CustomerRating', #men blazers/coats page 2
        # 6: 'https://shop.nordstrom.com/c/womens-coats?origin=topnav&breadcrumb=Home%2FWomen%2FClothing%2FCoats%2C%20Jackets%20%26%20Blazers&offset=1&sort=CustomerRating', #women coats/jackets/blazers page 1
        # 7: 'https://shop.nordstrom.com/c/womens-coats?origin=topnav&breadcrumb=Home%2FWomen%2FClothing%2FCoats%2C%20Jackets%20%26%20Blazers&offset=1&page=2&sort=CustomerRating', #women coats/jackets/blazers page 2
        # 8: 'https://shop.nordstrom.com/c/mens-coats-jackets?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FCoats%20%26%20Jackets&offset=3&sort=CustomerRating', #men coats/jackets page 1
        # 9: 'https://shop.nordstrom.com/c/mens-coats-jackets?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FCoats%20%26%20Jackets&offset=3&page=2&sort=CustomerRating', #men coats/jackets page 2
        # 10: 'https://shop.nordstrom.com/c/womens-jeans-shop?origin=topnav&breadcrumb=Home%2FWomen%2FClothing%2FJeans%20%26%20Denim&offset=3&sort=CustomerRating', #women jeans/denims page 1
        # 11: 'https://shop.nordstrom.com/c/womens-jeans-shop?origin=topnav&breadcrumb=Home%2FWomen%2FClothing%2FJeans%20%26%20Denim&offset=3&page=2&sort=CustomerRating', #women jeans/denims page 2
        # 12: 'https://shop.nordstrom.com/c/mens-jeans?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FJeans&offset=10&sort=CustomerRating', #men jeans page 1
        # 13: 'https://shop.nordstrom.com/c/mens-jeans?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FJeans&offset=10&page=2&sort=CustomerRating', #men jeans page 2

    }
    return switcher.get(switch_counter, "Invalid link")

def ratings_json(rating):
    jsonValue = str(rating).find(".")

    if rating == "N/A":
        return 0 #switched to 0 from "N/A"
    else:
        if jsonValue == 1:
            return float(rating[:3])
        else:
            return float(rating[:1])


while switch_counter < 3: #switch_counter < (number of url links)

        r = 0
        j=0
        driver.get(url_link(switch_counter))
        print("loading page...")
        try:
            wait = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'dialog-description')))
            print("page is ready")
        except TimeoutException:
            print("loading took too long!")

        selenium_html = driver.page_source
        soup = BeautifulSoup(selenium_html, 'html.parser')
        for i in range(len(soup.find_all('article', class_='_1AOd3 QIjwE'))):  # 'a' tags are for items
            try:
                    if url_link(switch_counter).replace('https://shop.nordstrom.com/c/', '').startswith("womens") is True:
                        product_gender = "FEMALE"
                    elif url_link(switch_counter).replace('https://shop.nordstrom.com/c/', '').startswith("mens") is True:
                        product_gender = "MALE"
                    else:
                        product_gender = "UNISEX"

                    if switch_counter == 0 or switch_counter == 1 or switch_counter == 2 or switch_counter == 3:
                        product_category = "ACTIVEWEAR"
                    elif switch_counter == 4 or switch_counter == 5 or switch_counter == 6 or switch_counter == 7 or switch_counter == 8  or switch_counter == 9:
                        product_category = "BLAZERS/COATS/JACKETS"
                    elif switch_counter == 10 or switch_counter == 11 or switch_counter == 12 or switch_counter == 13:
                        product_category = "JEANS/DENIMS"
                    else:
                        product_category = "NOT AVAILABLE"

                    ############## PRICE #################

                    product_price_parse = soup.findAll("div", {"class": 'YbtDD _3bi0z'})[i].findAll("span", recursive=False)
                    # product_price_parse = soup.find_all("article", {"class": '_1AOd3 QIjwE'})[i].find_all("span", recursive=False)

                    if str(product_price_parse).find("Was") != -1:
                        marked_down = ("YES")
                        product_price_parse = str(soup.find_all("div", {"class": 'YbtDD _18N5Q'})[j].find_next().find_next("span", recursive=False))

                        if str(product_price_parse).find('–') != -1:
                            # discount_percent = None
                            # product_price = None
                            discount_percent_parse = str(
                                soup.find_all("div", {"class": 'YbtDD _18N5Q'})[j].find_next().find_next().find_next(
                                    "span", recursive=False))
                            discount_percent = 0 #changed to 0 from "N/A"
                            product_price = ((re.sub("[^0123456789\.]", "", product_price_parse))[2:].strip()).partition("–")[0] #when an item is on sale but there is no fixed price but a range instead, here we get
                        else:
                            discount_percent_parse = str(soup.find_all("div", {"class": 'YbtDD _18N5Q'})[j].find_next().find_next().find_next("span", recursive=False))
                            discount_percent = (re.sub("[^0123456789\.]", "", discount_percent_parse))[2:].strip()

                            if len(discount_percent)>2:
                                discount_percent=0 #changed to 0 from "N/A" #the item is actually on sale but the page doesn't display the percentage and we get an invalid answer in response

                            product_price = (re.sub("[^0123456789\.]", "", product_price_parse))[2:].strip()
                        j = j+1
                    else:
                        marked_down = ("NO")

                        discount_percent = 0
                        product_price_parse = str(
                            soup.find_all("div", {"class": 'YbtDD _3bi0z'})[i].find_next().find_next("span", recursive=False))

                        if str(product_price_parse).find('–') != -1:
                            product_price = ((re.sub("[^0123456789\.]", "", product_price_parse))[2:].strip()).partition("–")[0]
                        else:
                            product_price = (re.sub("[^0123456789\.]", "", product_price_parse))[2:].strip()

                    ##############
                    ############## RATING #################


                    item_parse = soup.findAll('article', class_='_1AOd3 QIjwE')[i].find_all("a", recursive=False)

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
                        number_of_reviews = 0

                    ##############

                    product_name = soup.find_all('h3', attrs={'class': 'Dawzg _28b4r'})[i].text
                    product_link = "https://shop.nordstrom.com"+soup.find_all('a', attrs={'class': '_1av3_'})[i]['href']
                    product_image = soup.find_all('img', attrs={'name': 'product-module-image'})[i][
                        'src']

                    print("\nproduct ID:") + str(product_id)
                    print("gender: ") + product_gender
                    print("category: ") + product_category
                    print ("name: ") + product_name
                    print ("marked-down: ") + marked_down
                    print ("discount: ")+str(discount_percent)
                    print ("price: ") + str(product_price)[:4]
                    print ("rating: ") + str(rating)
                    print ("reviews: ") + str(number_of_reviews)
                    print ("link: ") + product_link
                    print ("image: ")+product_image

                    product_price_json = product_price[:4]

                    dataDict = {
                            "product_id":str(product_id),
                            "gender":product_gender,
                            "category":product_category,
                            "name":product_name,
                            "price":float(product_price_json),
                            "link":product_link,
                            "sale": marked_down,
                            "discount_percent": float(discount_percent), #added float
                            "rating":ratings_json(rating),
                            "reviews":int(number_of_reviews),
                            "img":product_image
                    }

                    product_id += 1

                    constJSON[0]["clothing"].append(dataDict)
                    # #time.sleep(1.5)  # pause the code for 1.5 sec, so we dont get blocked for spamming
            except IndexError:
                print("\nIndex error!\nSwitching to next case...")
                # constJSON[0]["clothing"].append(None)
                pass

        switch_counter += 1

        if switch_counter > 1:
            with open("nordstrom.json", "w") as f:
                print("\nSaved to JSON file\n")
                # print(json.dumps(constJSON))
                json.dump(constJSON, f)


