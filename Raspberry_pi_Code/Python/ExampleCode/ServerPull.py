import datetime

import time

from sys import argv

import requests, json





complete_url = "http://10.156.97.106//TestAlert.json"# The url is = http://api.openweathermap.org/data/2.5/weather?appid=eb737582e33e5f2a85cca9abb6e392e0&q=somerset,nj,us

 

response = requests.get(complete_url) 



x = response.json()



#print(x)



print(x["alert"][0]["Dec"])