import json 
from operator import itemgetter

with open('zara.json')  as f: 
    zaradata = json.load(f) 
    zaradata1 = zaradata[0]
    clothing = zaradata1['clothing']
    for parameters in clothing:
        price_data = parameters['price']
        category_data = parameters['category']
        sale_data = parameters['sale']
        link = parameters['link']
        important_data = [{'category':category_data, 'price':price_data, 'sales':sale_data, 'link':link}]
        #important_data = [category_data, price_data, sale_data, link]
        #def sortbyprice():
        ##price_ascending = sorted(important_data.items(), key = lambda important_data: important_data[1])
        #important_data.sort(key = price_ascending, reverse = False)
        #print(price_ascending)

        #sorted(important_data, key=itemgetter('price'), reverse = False)

        #important_data.sort(key=itemgetter('price'), reverse = False)
        #print(important_data)
    print(sorted(important_data, key=itemgetter('price'), reverse = False))

    #if weather = 'WARM': 
  