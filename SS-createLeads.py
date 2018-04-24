import json
import requests
from random import *

rand_numb = str(randint(1, 1000) * 1000000)

test_data = {
  "method":"createLeads",
  "params":
    {"objects":
      [
        {"firstName":"Test21","lastName":"fake","emailAddress":"test21@email.com"},
        {"firstName":"Test22","lastName":"fake","emailAddress":"test22@email.com"}
      ]
      
    },
  "id":rand_numb
}

# THIS BELOW creates a lead 'test_data'
response = requests.post('https://api.sharpspring.com/pubapi/v1/?accountID=fgdfgdfgdfgdfg&secretKey=dfgdfgdfgdffgd',
json = test_data)


print(response.text)