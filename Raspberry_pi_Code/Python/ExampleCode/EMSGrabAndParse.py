import datetime
import time
from sys import argv
import requests
import json

### SETTINGS ###

# Could (should?) keep for security reasons
api_key = "NO"
# TODO: Change to the url of our emergency test server
base_url = "http://api.openweathermap.org/data/2.5/weather?"
# TODO: Could keep as a location system, but subject to change in final schema
city_name = "manville,nj,us"  # input("Enter city name : ")
complete_url = base_url + "appid=" + api_key + "&q=" + city_name


### MAIN FUNCTIONALITY ###
# We'll fire this periodically. 

response = requests.get(complete_url)
x = response.json()

if True:
    # May want to add deeper error handling for our own server
    if x["cod"] != "404":
        # Will change based on emergency schema and picture presentation
        current_temperature = x["main"]["temp"]
        current_pressure = x["main"]["pressure"]
        current_humidiy = x["main"]["humidity"]
        wind_speed = x["wind"]["speed"]
        wind_direction = x["wind"]["deg"]
        weather_description = x["weather"][0]["description"]
        current_tem_F = round(((current_temperature - 273.15) * (9/5) + 32), 3)
        info = datetime.datetime.now()
        hr = info.hour % 12
        if hr == 0:
            hr = 12
        else:
            hr = hr
        if info.hour > 12:
            half = "PM"
        else:
            half = "AM"

        print("\nTime = ", hr, ":", info.minute, ":", info.second, half)
        print("Temp = " + str(current_tem_F)+" F")
        print("Pressure = " + str(current_pressure) + " hPa")
        print("Humidity = " + str(current_humidiy) + "%")
        print("Weather descreption = " + str(weather_description))
        print(complete_url)

    else:
        print(" City Not Found ")
