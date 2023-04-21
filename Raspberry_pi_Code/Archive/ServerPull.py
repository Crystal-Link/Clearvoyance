import datetime
import time
import requests, json





complete_url = "http://10.156.0.236//TestAlert.json"

while True:

    response = requests.get(complete_url) 

    x = response.json()


    with open("sample.json", "w") as outfile:
        json.dump(x, outfile)

    print(x["alerts"][0]["Description"])
    time.sleep(5)
