import json 
import pandas as pd
import numpy as np
from pandas.io.json import json_normalize

##weather labels: cold, chilly, warm, hot
##precipitation labels: dry, rain, snow

def getWeather(temperature = 20, precipitation = 'rain'):
    if temperature <= 0 and precipitation == 'dry':
        weatherLabel = "colddry"
    elif temperature <= 0 and precipitation == 'rain':
        weatherLabel = "coldrain"
    elif temperature <= 0 and precipitation == 'snow':
        weatherLabel = "coldsnow"
    elif temperature > 0 and temperature <10 and precipitation == 'dry':
        weatherLabel = "chillydry"
    elif temperature > 0 and temperature <10 and precipitation == 'rain':
        weatherLabel = "chillyrain"
    elif temperature > 0 and temperature <10 and precipitation == 'snow':
        weatherLabel = "chillysnow"
    elif temperature >=10 and temperature <20 and precipitation == 'dry':
        weatherLabel = "warmdry"
    elif temperature >=10 and temperature <20 and precipitation == 'rain':
        weatherLabel = "warmrain"
    elif temperature >20 and precipitation is precipitation == 'dry':
        weatherLabel = "hotdry"
    else: 
        weatherLabel = "warmrain"

    return weatherLabel


def sortclothes():
    getWeather()

    if getWeather() is "colddry": 
        print(top5colddry)
    elif getWeather() is "coldrain": 
        print(top5coldrain)
    elif getWeather() is "coldsnow": 
        print(top5coldsnow)
    elif getWeather() is "chillydry": 
        print(top5chillydry)
    elif getWeather() is "chillyrain": 
        print(top5chillyrain)
    elif getWeather() is "chillysnow": 
        print(top5chillysnow)
    elif getWeather() is "warmdry": 
        print(top5warmdry)
    elif getWeather() is "warmrain": 
        print(top5warmrain)
    elif getWeather() is "hotdry": 
        print(top5hotdry) 
    elif getWeather() is "hotrain": 
        print(top5warmrain)

        
with open('nordstrom.json')  as f: 
    nordsdata = json.load(f) 
df = pd.DataFrame(nordsdata[0]['clothing'])

## FIGURING OUT WEIGHTED RATING
No_Reviews = df['reviews']
Rating = df['rating']
MeanReview = df['rating'].mean()
minReview = df['reviews'].quantile(0.5)

df['weighted_rating'] = ((Rating*No_Reviews)+(MeanReview*minReview))/(No_Reviews + minReview)

#extract each different type of clothing from the dataset
colddry = df[df.name.str.contains('hoodie| pullover| joggers| jacket| sweatshirt',case=False)]
coldrain = df[df.name.str.contains('hoodie| pullover| joggers| jacket| sweatshirt',case=False)]
coldsnow= df[df.name.str.contains('hoodie| pullover| joggers| jacket| sweatshirt',case=False)]
chillydry= df[df.name.str.contains('hoodie| sweatshirt| vest| long sleeve| pants',case=False)]
chillyrain= df[df.name.str.contains('hoodie| sweatshirt| vest| long sleeve| pants',case=False)]
chillysnow= df[df.name.str.contains('hoodie| jacket| sweatshirt| vest| long sleeve| pants',case=False)]
warmdry= df[df.name.str.contains('tights| vest| shorts| polo| top| pants',case=False)]
warmrain = df[df.name.str.contains('tights| vest| shorts| polo| top| pants',case=False)]
hotdry= df[df.name.str.contains('tights| vest| shorts| polo| top| t-shirt',case=False)]
hotrain= df[df.name.str.contains('tights| vest| shorts| polo| top| t-shirt',case=False)]


#Sort clothes according to desired parameters
sort_colddry = colddry.sort_values(by= ['weighted_rating','discount_percent', 'price'], ascending = [False, False, True])
sort_coldrain = coldrain.sort_values(by= ['weighted_rating','discount_percent', 'price'], ascending = [False, False, True])
sort_coldsnow = coldsnow.sort_values(by= ['weighted_rating','discount_percent', 'price'], ascending = [False, False, True])
sort_chillydry = chillydry.sort_values(by= ['weighted_rating','discount_percent', 'price'], ascending = [False, False, True])
sort_chillyrain = chillyrain.sort_values(by= ['weighted_rating','discount_percent', 'price'], ascending = [False, False, True])
sort_chillysnow = chillysnow.sort_values(by= ['weighted_rating','discount_percent', 'price'], ascending = [False, False, True])
sort_warmdry = warmdry.sort_values(by= ['weighted_rating','discount_percent', 'price'], ascending = [False, False, True])
sort_warmrain = warmrain.sort_values(by= ['weighted_rating','discount_percent', 'price'], ascending = [False, False, True])
sort_hotdry = hotdry.sort_values(by= ['weighted_rating','discount_percent', 'price'], ascending = [False, False, True])
sort_hotrain = hotrain.sort_values(by= ['weighted_rating','discount_percent', 'price'], ascending = [False, False, True])

#get top 5 items per weather condition
top5colddry = sort_colddry.head(5)
top5coldrain = sort_coldrain.head(5)
top5coldsnow = sort_coldsnow.head(5)
top5chillydry = sort_chillydry.head(5)
top5chillyrain = sort_chillyrain.head(5)
top5chillysnow = sort_chillysnow.head(5)
top5warmdry = sort_warmdry.head(5)
top5warmrain = sort_warmrain.head(5)
top5hotdry = sort_hotdry.head(5)
top5warmrain = sort_hotrain.head(5)

print("The current weather condition is: " + getWeather())
sortclothes()


   