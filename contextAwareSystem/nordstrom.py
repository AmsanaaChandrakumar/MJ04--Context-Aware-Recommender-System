import requests
import time
from bs4 import BeautifulSoup
import re
import json
import urllib
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
        0:'https://shop.nordstrom.com/c/mens-workout-activewear-clothing?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FActivewear&sort=CustomerRating',  # men activewear
        # 1:'https://shop.nordstrom.com/c/mens-workout-activewear-clothing?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FActivewear&page=2&sort=CustomerRating' #second page men activewear
        1:'https://shop.nordstrom.com/c/mens-blazers-sportcoats?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FBlazers%20%26%20Sport%20Coats&offset=1&sort=CustomerRating'



    }
    return switcher.get(switch_counter, "Invalid link")

def ratings_json(rating):
    jsonValue = str(rating).find(".")

    if jsonValue == 1:
        return float(rating[:3])
    else:
        return float(rating[:1])


while switch_counter < 2: #switch_counter < (number of url links)

        r = 0
        j=0
        driver.get(url_link(switch_counter))
        try:
            wait = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'dialog-description')))
            print("Page is ready")
        except TimeoutException:
            print("Loading took too much time!")

        selenium_html = driver.page_source
        # page = requests.get(url_link(switch_counter))
        # Parse HTML and save to BeautifulSoup object
        soup = BeautifulSoup(selenium_html, 'html.parser')
        for i in range(len(soup.find_all('article', class_='_1AOd3 QIjwE'))):  # 'a' tags are for items
            try:
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

                    product_price_parse = soup.findAll("div", {"class": 'YbtDD _3bi0z'})[i].findAll("span", recursive=False)
                    # product_price_parse = soup.find_all("article", {"class": '_1AOd3 QIjwE'})[i].find_all("span", recursive=False)

                    if str(product_price_parse).find("Was") != -1:
                        marked_down = ("YES")

                        product_price_parse = str(soup.find_all("div", {"class": 'YbtDD _18N5Q'})[j].find_next().find_next("span", recursive=False))
                        discount_percent_parse = str(soup.find_all("div", {"class": 'YbtDD _18N5Q'})[j].find_next().find_next().find_next("span", recursive=False))
                        discount_percent = (re.sub("[^0123456789\.]", "", discount_percent_parse))[2:].strip()
                        product_price = (re.sub("[^0123456789\.]", "", product_price_parse))[2:].strip()
                        j = j+1
                    else:
                        marked_down = ("NO")

                        discount_percent = 0
                        product_price_parse = str(
                            soup.find_all("div", {"class": 'YbtDD _3bi0z'})[i].find_next().find_next("span", recursive=False))
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
                        number_of_reviews = "N/A"

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
                    print ("discount: ")+str(discount_percent)+"%"
                    print ("price: ") + str(product_price)[:4]+" CAD"
                    print ("rating: ") + str(rating)
                    print ("reviews: ") + number_of_reviews
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
                            "discount_percent": discount_percent,
                            "rating":ratings_json(rating),
                            "reviews":int(number_of_reviews),
                            "img":product_image
                    }

                    product_id += 1

                    constJSON[0]["clothing"].append(dataDict)
                    # #time.sleep(1.5)  # pause the code for 1.5 sec, so we dont get blocked for spamming
            except IndexError:
                print("Index error!")
                constJSON[0]["clothing"].append('null')
                pass

        print(json.dumps(constJSON))
        switch_counter += 1

        if switch_counter > 1:
            with open("nordstrom.json", "w") as f:
                print(json.dumps(constJSON))
                json.dump(constJSON, f)


