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
from datetime import datetime
startTime = datetime.now()


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

        0:'https://shop.nordstrom.com/c/mens-workout-activewear-clothing?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FActivewear&sort=CustomerRating', #me activewear page 1 TO 7
        1: 'https://shop.nordstrom.com/c/mens-workout-activewear-clothing?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FActivewear&page=2&sort=CustomerRating',
        2: 'https://shop.nordstrom.com/c/mens-workout-activewear-clothing?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FActivewear&page=3&sort=CustomerRating',
        3: 'https://shop.nordstrom.com/c/mens-workout-activewear-clothing?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FActivewear&page=4&sort=CustomerRating',
        4: 'https://shop.nordstrom.com/c/mens-workout-activewear-clothing?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FActivewear&page=5&sort=CustomerRating',
        5: 'https://shop.nordstrom.com/c/mens-workout-activewear-clothing?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FActivewear&page=6&sort=CustomerRating',
        6: 'https://shop.nordstrom.com/c/mens-workout-activewear-clothing?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FActivewear&page=7&sort=CustomerRating',

        7: 'https://shop.nordstrom.com/c/womens-activewear-shop?origin=topnav&breadcrumb=Home%2FWomen%2FClothing%2FActivewear&offset=3&sort=CustomerRating', #women active wear page 1 to 7
        8: 'https://shop.nordstrom.com/c/womens-activewear-shop?origin=topnav&breadcrumb=Home%2FWomen%2FClothing%2FActivewear&offset=3&page=2&sort=CustomerRating',
        9: 'https://shop.nordstrom.com/c/womens-activewear-shop?origin=topnav&breadcrumb=Home%2FWomen%2FClothing%2FActivewear&offset=3&page=3&sort=CustomerRating',
        10: 'https://shop.nordstrom.com/c/womens-activewear-shop?origin=topnav&breadcrumb=Home%2FWomen%2FClothing%2FActivewear&offset=3&page=4&sort=CustomerRating',
        11: 'https://shop.nordstrom.com/c/womens-activewear-shop?origin=topnav&breadcrumb=Home%2FWomen%2FClothing%2FActivewear&offset=3&page=5&sort=CustomerRating',
        12: 'https://shop.nordstrom.com/c/womens-activewear-shop?origin=topnav&breadcrumb=Home%2FWomen%2FClothing%2FActivewear&offset=3&page=6&sort=CustomerRating',
        13: 'https://shop.nordstrom.com/c/womens-activewear-shop?origin=topnav&breadcrumb=Home%2FWomen%2FClothing%2FActivewear&offset=3&page=7&sort=CustomerRating',

        14: 'https://shop.nordstrom.com/c/mens-blazers-sportcoats?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FBlazers%20%26%20Sport%20Coats&offset=1&sort=CustomerRating', #men blazers and sport coats page 1 to 7
        15: 'https://shop.nordstrom.com/c/mens-blazers-sportcoats?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FBlazers%20%26%20Sport%20Coats&offset=1&page=2&sort=CustomerRating',
        16: 'https://shop.nordstrom.com/c/mens-blazers-sportcoats?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FBlazers%20%26%20Sport%20Coats&offset=1&page=3&sort=CustomerRating',
        17: 'https://shop.nordstrom.com/c/mens-blazers-sportcoats?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FBlazers%20%26%20Sport%20Coats&offset=1&page=4&sort=CustomerRating',
        18: 'https://shop.nordstrom.com/c/mens-blazers-sportcoats?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FBlazers%20%26%20Sport%20Coats&offset=1&page=5&sort=CustomerRating',
        19: 'https://shop.nordstrom.com/c/mens-blazers-sportcoats?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FBlazers%20%26%20Sport%20Coats&offset=1&page=6&sort=CustomerRating',
        20: 'https://shop.nordstrom.com/c/mens-blazers-sportcoats?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FBlazers%20%26%20Sport%20Coats&offset=1&page=7&sort=CustomerRating',

        21: 'https://shop.nordstrom.com/c/womens-coats?origin=topnav&breadcrumb=Home%2FWomen%2FClothing%2FCoats%2C%20Jackets%20%26%20Blazers&offset=1&sort=CustomerRating', #women coats,jackets and blazers page 1 to 7
        22: 'https://shop.nordstrom.com/c/womens-coats?origin=topnav&breadcrumb=Home%2FWomen%2FClothing%2FCoats%2C%20Jackets%20%26%20Blazers&offset=1&page=2&sort=CustomerRating',
        23: 'https://shop.nordstrom.com/c/womens-coats?origin=topnav&breadcrumb=Home%2FWomen%2FClothing%2FCoats%2C%20Jackets%20%26%20Blazers&offset=1&page=3&sort=CustomerRating',
        24: 'https://shop.nordstrom.com/c/womens-coats?origin=topnav&breadcrumb=Home%2FWomen%2FClothing%2FCoats%2C%20Jackets%20%26%20Blazers&offset=1&page=4&sort=CustomerRating',
        25: 'https://shop.nordstrom.com/c/womens-coats?origin=topnav&breadcrumb=Home%2FWomen%2FClothing%2FCoats%2C%20Jackets%20%26%20Blazers&offset=1&page=5&sort=CustomerRating',
        26: 'https://shop.nordstrom.com/c/womens-coats?origin=topnav&breadcrumb=Home%2FWomen%2FClothing%2FCoats%2C%20Jackets%20%26%20Blazers&offset=1&page=6&sort=CustomerRating',
        27: 'https://shop.nordstrom.com/c/womens-coats?origin=topnav&breadcrumb=Home%2FWomen%2FClothing%2FCoats%2C%20Jackets%20%26%20Blazers&offset=1&page=7&sort=CustomerRating',

        28: 'https://shop.nordstrom.com/c/mens-coats-jackets?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FCoats%20%26%20Jackets&offset=3&sort=CustomerRating', #men coat and jackets
        29: 'https://shop.nordstrom.com/c/mens-coats-jackets?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FCoats%20%26%20Jackets&offset=3&page=2&sort=CustomerRating',
        30: 'https://shop.nordstrom.com/c/mens-coats-jackets?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FCoats%20%26%20Jackets&offset=3&page=3&sort=CustomerRating',
        31: 'https://shop.nordstrom.com/c/mens-coats-jackets?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FCoats%20%26%20Jackets&offset=3&page=4&sort=CustomerRating',
        32: 'https://shop.nordstrom.com/c/mens-coats-jackets?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FCoats%20%26%20Jackets&offset=3&page=5&sort=CustomerRating',
        33: 'https://shop.nordstrom.com/c/mens-coats-jackets?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FCoats%20%26%20Jackets&offset=3&page=6&sort=CustomerRating',
        34: 'https://shop.nordstrom.com/c/mens-coats-jackets?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FCoats%20%26%20Jackets&offset=3&page=7&sort=CustomerRating',

        35: 'https://shop.nordstrom.com/c/womens-dresses-shop?origin=topnav&breadcrumb=Home%2FWomen%2FClothing%2FDresses&offset=3&sort=CustomerRating', #women dresses
        36: 'https://shop.nordstrom.com/c/womens-dresses-shop?origin=topnav&breadcrumb=Home%2FWomen%2FClothing%2FDresses&offset=3&page=2&sort=CustomerRating',
        37: 'https://shop.nordstrom.com/c/womens-dresses-shop?origin=topnav&breadcrumb=Home%2FWomen%2FClothing%2FDresses&offset=3&page=3&sort=CustomerRating',
        38: 'https://shop.nordstrom.com/c/womens-dresses-shop?origin=topnav&breadcrumb=Home%2FWomen%2FClothing%2FDresses&offset=4&page=4&sort=CustomerRating',
        39: 'https://shop.nordstrom.com/c/womens-dresses-shop?origin=topnav&breadcrumb=Home%2FWomen%2FClothing%2FDresses&offset=3&page=5&sort=CustomerRating',
        40: 'https://shop.nordstrom.com/c/womens-dresses-shop?origin=topnav&breadcrumb=Home%2FWomen%2FClothing%2FDresses&offset=3&page=6&sort=CustomerRating',
        41: 'https://shop.nordstrom.com/c/womens-dresses-shop?origin=topnav&breadcrumb=Home%2FWomen%2FClothing%2FDresses&offset=3&page=7&sort=CustomerRating',

        42: 'https://shop.nordstrom.com/c/mens-dress-shirts?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FDress%20Shirts&sort=CustomerRating', #men dress shirts
        43: 'https://shop.nordstrom.com/c/mens-dress-shirts?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FDress%20Shirts&page=2&sort=CustomerRating',
        44: 'https://shop.nordstrom.com/c/mens-dress-shirts?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FDress%20Shirts&page=3&sort=CustomerRating',
        45: 'https://shop.nordstrom.com/c/mens-dress-shirts?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FDress%20Shirts&page=4&sort=CustomerRating',
        46: 'https://shop.nordstrom.com/c/mens-dress-shirts?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FDress%20Shirts&page=5&sort=CustomerRating',
        47: 'https://shop.nordstrom.com/c/mens-dress-shirts?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FDress%20Shirts&page=6&sort=CustomerRating',
        48: 'https://shop.nordstrom.com/c/mens-dress-shirts?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FDress%20Shirts&page=7&sort=CustomerRating',

        49: 'https://shop.nordstrom.com/c/womens-jeans-shop?origin=topnav&breadcrumb=Home%2FWomen%2FClothing%2FJeans%20%26%20Denim&offset=3&sort=CustomerRating', #women jeans and denim
        50: 'https://shop.nordstrom.com/c/womens-jeans-shop?origin=topnav&breadcrumb=Home%2FWomen%2FClothing%2FJeans%20%26%20Denim&offset=3&page=2&sort=CustomerRating',
        51: 'https://shop.nordstrom.com/c/womens-jeans-shop?origin=topnav&breadcrumb=Home%2FWomen%2FClothing%2FJeans%20%26%20Denim&offset=3&page=3&sort=CustomerRating',
        52: 'https://shop.nordstrom.com/c/womens-jeans-shop?origin=topnav&breadcrumb=Home%2FWomen%2FClothing%2FJeans%20%26%20Denim&offset=3&page=4&sort=CustomerRating',
        53: 'https://shop.nordstrom.com/c/womens-jeans-shop?origin=topnav&breadcrumb=Home%2FWomen%2FClothing%2FJeans%20%26%20Denim&offset=3&page=5&sort=CustomerRating',
        54: 'https://shop.nordstrom.com/c/womens-jeans-shop?origin=topnav&breadcrumb=Home%2FWomen%2FClothing%2FJeans%20%26%20Denim&offset=3&page=6&sort=CustomerRating',
        55: 'https://shop.nordstrom.com/c/womens-jeans-shop?origin=topnav&breadcrumb=Home%2FWomen%2FClothing%2FJeans%20%26%20Denim&offset=3&page=7&sort=CustomerRating',

        56: 'https://shop.nordstrom.com/c/mens-jeans?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FJeans&offset=10&sort=CustomerRating', #men jeans
        57: 'https://shop.nordstrom.com/c/mens-jeans?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FJeans&offset=10&page=2&sort=CustomerRating',
        58: 'https://shop.nordstrom.com/c/mens-jeans?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FJeans&offset=10&page=3&sort=CustomerRating',
        59: 'https://shop.nordstrom.com/c/mens-jeans?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FJeans&offset=10&page=4&sort=CustomerRating',
        60: 'https://shop.nordstrom.com/c/mens-jeans?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FJeans&offset=10&page=5&sort=CustomerRating',
        61: 'https://shop.nordstrom.com/c/mens-jeans?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FJeans&offset=10&page=6&sort=CustomerRating',
        62: 'https://shop.nordstrom.com/c/mens-jeans?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FJeans&offset=10&page=7&sort=CustomerRating',
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


while switch_counter < 63: #switch_counter < (number of url links)

        r = 0
        j=0
        driver.get(url_link(switch_counter))
        print("loading page...")
        try:
            wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'dialog-description')))
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

                    if switch_counter >= 0 and switch_counter<= 13:
                        product_category = "ACTIVEWEAR"
                    elif switch_counter >= 14 and switch_counter<=34:
                        product_category = "BLAZERS/COATS/JACKETS"
                    elif switch_counter >= 35 and switch_counter<=41:
                        product_category = "DRESSES"
                    elif switch_counter >= 42 and switch_counter<=48:
                        product_category = "SHIRTS"
                    elif switch_counter >= 49 and switch_counter<=62:
                        product_category = "JEANS/DENIM"
                    else:
                        product_category = "NOT AVAILABLE"

                    #----------PRICE----------
                    no_info = 0 #for when Nordstrom asks to add the product to the shopping cart to know the price

                    product_price_parse = soup.findAll("div", {"class": 'YbtDD _3bi0z'})[i].findAll("span", recursive=False)

                    if (str(soup.findAll("article", {"class": '_1AOd3 QIjwE'})[i].findAll("div", recursive=False)).find(
                            "Add") != -1):  # Nordstrom for some product requires to add item to bag to find price, we have no product info in these cases
                        product_price = 0
                        discount_percent=0
                        marked_down = "NO"
                        no_info = 1
                    else:
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
                                product_price = (re.sub("[^0123456789\.]", "", product_price_parse))[2:].strip()

                                discount_percent_parse = str(soup.find_all("div", {"class": 'YbtDD _18N5Q'})[j].find_next().find_next().find_next("span", recursive=False))
                                discount_percent_text = (re.sub("[^0123456789\.]", "", discount_percent_parse))[2:].strip()

                                if len(discount_percent_text)>2:
                                    discount_percent = 0 #changed to 0 from "N/A" #the item is actually on sale but the page doesn't display the percentage and we get an invalid answer in response
                                else:
                                    discount_percent=discount_percent_text

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

                    #------------RATING----------------
                    item_parse = soup.findAll('article', class_='_1AOd3 QIjwE')[i].find_all("a", recursive=False)

                    if no_info==1:
                        rating = "N/A"
                        number_of_reviews = 0
                    else:
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

                    #----------------------------

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
                    print ("price: ") + str(product_price)[:5]
                    print ("rating: ") + str(rating)
                    print ("reviews: ") + str(number_of_reviews)
                    print ("link: ") + product_link
                    print ("image: ")+product_image
                    print ("currently on page: ")+str(switch_counter)

                    if product_price == 0:
                        product_price_json = 0
                    else:
                        product_price_json = product_price[:5]

                    dataDict = {
                            "product_id":str(product_id),
                            "gender":product_gender,
                            "category":product_category,
                            "name":product_name,
                            "price":float(product_price_json),
                            "link":product_link,
                            "sale": marked_down,
                            "discount_percent": (discount_percent),
                            "rating":ratings_json(rating),
                            "reviews":int(number_of_reviews),
                            "img":product_image
                    }

                    product_id += 1

                    constJSON[0]["clothing"].append(dataDict)
                    # #time.sleep(1.5)  # pause the code for 1.5 sec, so we dont get blocked for spamming
            except IndexError:
                print("Index error!")

        switch_counter += 1

        if switch_counter > 1:
            with open("nordstrom.json", "w") as f:
                print("\nSaved to JSON file\n")
                # print(json.dumps(constJSON))
                json.dump(constJSON, f)
print ("\nExecution time: ")+str(datetime.now() - startTime)


