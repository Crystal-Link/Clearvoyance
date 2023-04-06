import datetime
import time
import requests, json





complete_url = "http://10.156.118.103//TestAlert.json"# The url is = http://api.openweathermap.org/data/2.5/weather?appid=eb737582e33e5f2a85cca9abb6e392e0&q=somerset,nj,us

while True:

    response = requests.get(complete_url) 

    x = response.json()


    with open("sample.json", "w") as outfile:
        json.dump(x, outfile)

    print(x["alert"][0]["Dec"])
    time.sleep(5)
