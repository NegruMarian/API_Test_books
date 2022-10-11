from random import  randint
import requests



# def login(clientName = None, clientEmail = None ):
#     json = { "clientName": 'Marian',
#             "clientEmail": 'marian@gmail.com'
#                 }
#     responce = requests.post('https://simple-books-api.glitch.me/api-clients/',json=json)
#     return responce

def get_token():
    nr = randint(1,9999999)
    json = { "clientName": "Postman",
            "clientEmail": f"valentin{nr}@example.com"
             }
    response = requests.post('https://simple-books-api.glitch.me/api-clients/', json=json)
    return response.json()["accessToken"]


