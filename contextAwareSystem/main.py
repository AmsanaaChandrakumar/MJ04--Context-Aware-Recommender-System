from flask import Flask, jsonify, request, render_template
import numpy as np
import pandas as pd
import requests
import json
import os 
from pandas.io.json import json_normalize
# import configparser

app = Flask(__name__)
# app.config.from_envvar('APP_SETTINGS')

# config = configparser.ConfigParser()
# config.read('config.cfg')
# print(config['GOOGLE.MAPS']['SECRET_KEY'])

@app.route("/", methods=['GET', 'POST'])
def index():

    return render_template("index.html")

@app.route('/hello', methods=['GET', 'POST'])
def hello():
	# POST request: goes from browser to flask
    if request.method == 'POST':
    	# print('Incoming..')
    	jsonData = request.get_json(force=True)
    	# print(jsonData.get('greeting'))  # parse as JSON
    	return str(jsonData.get('greeting')), 200

    # GET request: goes from flask to browser
    else :
        message = {'greeting':'Hello from Flask!'}
        return jsonify(message)  # serialize and use JSON headers

@app.route('/cityWeather', methods=['GET', 'POST'])
def cityWeather():
    if request.method == 'POST':
    	jsonData = request.get_json(force=True)
    	city = str(jsonData.get('city'))
    	url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=3739750b9f8a52c079de7d8292030d35&units=metric'.format(city)
    	res = requests.get(url)
    	data = res.json()
    	return data, 200 

@app.route('/recommendation', methods=['GET', 'POST'])
def getWeather():
    if request.method == 'POST':
        jsonData = request.get_json(force=True)
        temperature = int(jsonData.get('temperature'))
        precipitation = str(jsonData.get('precipitation'))

        if temperature <= 0 and precipitation == 'clear sky' or precipitation == 'few clouds' or precipitation == 'scattered clouds' or precipitation == 'broken clouds':
            weatherLabel = "colddry"
        elif temperature <= 0 and precipitation == 'rain' or precipitation == 'shower rain' or precipitation == 'thunderstorm' or precipitation == 'mist':
            weatherLabel = "coldrain"
        elif temperature <= 0 and precipitation == 'snow':
            weatherLabel = "coldsnow"
        elif temperature > 0 and temperature <10 and precipitation == 'clear sky' or precipitation == 'few clouds' or precipitation == 'scattered clouds' or precipitation == 'broken clouds' or precipitation == 'overcast clouds':
            weatherLabel = "chillydry"
        elif temperature > 0 and temperature <10 and precipitation == 'rain' or precipitation == 'shower rain' or precipitation == 'thunderstorm' or precipitation == 'mist' or precipitation == 'light intensity drizzle':
            weatherLabel = "chillyrain"
        elif temperature > 0 and temperature <10 and precipitation == 'snow':
            weatherLabel = "chillysnow"
        elif temperature >=10 and temperature <20 and precipitation == 'clear sky' or precipitation == 'few clouds' or precipitation == 'scattered clouds' or precipitation == 'broken clouds':
            weatherLabel = "warmdry"
        elif temperature >=10 and temperature <20 and precipitation == 'rain' or precipitation == 'shower rain' or precipitation == 'thunderstorm' or precipitation == 'mist':
            weatherLabel = "warmrain"
        elif temperature >=20 and precipitation == 'clear sky' or precipitation == 'few clouds' or precipitation == 'scattered clouds' or precipitation == 'broken clouds':
            weatherLabel = "hotdry"
        else: 
            weatherLabel = "warmrain"

        sortclothes(weatherLabel)
        paulsMainFunction()
        return weatherLabel

def sortclothes(weatherLabel):
    print (weatherLabel)
    return ""    

def paulsMainFunction():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "nordstrom.json")
    nordsdata = json.load(open(json_url))

    df = pd.DataFrame(nordsdata[0]['clothing'])
    print (df)
    return ""
# @app.route('/googleMaps', methods=['GET', 'POST'])
# def googleMaps():
#     if request.method == 'POST':
#         print("POST request")

#     else:
#         googleMapsAPI = config['GOOGLE.MAPS']['SECRET_KEY']
#         return googleMapsAPI
        
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080)
