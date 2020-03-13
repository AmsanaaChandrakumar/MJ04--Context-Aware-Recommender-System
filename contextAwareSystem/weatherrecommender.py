import json 
import pandas as pd
import numpy as np
from pandas.io.json import json_normalize


def getWeather(temperature = -1):
    if temperature < 0:
        weatherLabel = "cold"
    else:
        weatherLabel = "warm"

    return weatherLabel


def sortclothes():
    getWeather()

    if getWeather() is "cold": 
        print(top5blazers)
    else:
        getWeather() is "warm"
        print(top5skirts)

        
with open('zara.json')  as f: 
    zaradata = json.load(f) 
df = pd.DataFrame(zaradata[0]['clothing'])

#sortskirts = df.sort_values(by = ['category','sale', 'price'], ascending= [False, False, True])
#sortblazers = df.sort_values(by= ['category', 'sale', 'price'], ascending = [True, False, True])
sort_clothes = df.sort_values(by= ['sale', 'price'], ascending = [False, True])
getskirts = sort_clothes.loc[sort_clothes['category']=='SKIRTS']
getblazers = sort_clothes.loc[sort_clothes['category']=='BLAZERS']
top5skirts = getskirts.head(5)
top5blazers = getblazers.head(5)

sortclothes()



    #if weather = 'WARM': 
   