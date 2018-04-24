import json
import requests
import os, sys


from random import *
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

SS_SECRET_KEY = os.getenv("SS_SECRET_KEY")
SS_ACCOUNT_ID = os.getenv("SS_ACCOUNT_ID")

url = 'https://api.sharpspring.com/pubapi/v1/?accountID=%s&secretKey=%s' % (SS_ACCOUNT_ID, SS_SECRET_KEY)

print(url)

# sys.exit()

rand_numb = str(randint(1, 1000) * 1000000)

find_dude = {
  "method":"getLead",
  "params":
    {
        "id": 588430111747
      
    },
  "id":rand_numb
}

## THIS BELOW pulls a single lead's data. Notice that find_dude has no object
## as it is one single lead
r2 = requests.post(url, json = find_dude)

returned_data = r2.json()
result = returned_data["result"]["lead"]

print(returned_data["result"]["lead"][0]["id"])

dude_id = result[0]["id"]
print(dude_id)
  

update_dude = {
  "method":"updateLeadsV2",
  "params":
  {
    "objects":
    [
      {"id": dude_id, "lastName":"SUCCESS!" }
    ]
  },
  "id": rand_numb
}

requests.post('https://api.sharpspring.com/pubapi/v1/?accountID=dsfdfsdfsdfsdfds&secretKey=sdfsdfsdfds', 
json = update_dude)

# Need to add success/failure message



