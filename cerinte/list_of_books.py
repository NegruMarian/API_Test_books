import requests
from cerinte.Get_Authentication import *

def get_books(limit='', type= ''):
    responce = requests.get(f'https://simple-books-api.glitch.me/books?type={type}&limit={limit}')
    return responce

def get_a_book(id):
    response = requests.get(f'https://simple-books-api.glitch.me/books/:bookId{id}')
    return response

def submit_an_order():
    token = get_token()
    header = {'Authorization': token}
    json= {"bookId": 1,
            "customerName": "John"}
    order = requests.post('https://simple-books-api.glitch.me/orders',headers=header,json=json)

    return order.json()

def get_all_orders():
    token = get_token()
    header = {'Authorization': token}
    orders = requests.get('https://simple-books-api.glitch.me/orders',headers=header)
    return orders

def get_an_order(orderId):
    token = get_token()
    header = {'Authorization': token}
    order1 = requests.get(f'https://simple-books-api.glitch.me/orders/{orderId}',headers=header)
    return order1

def update_an_order(order):
    token = get_token()
    header = {'Authorization': token}
    update = requests.patch(f'https://simple-books-api.glitch.me/orders/{order}',headers=header)
    return update


