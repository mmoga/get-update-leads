import json
import requests
from random import *

new_dudes = {
  "method":"subscribeToLeadUpdates",
  "params":
  {
    "url": "https://hooks.zapier.com/hooks/catch/2155359/fk5ze8/"
  },
  "id": rand_numb
}

requests.post('https://api.sharpspring.com/pubapi/v1/?accountID=sdfsdfsdfsfgfsg&secretKey=sfgfdgfgdf', 
json = new_dudes)