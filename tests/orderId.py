from cerinte.list_of_books import submit_an_order, update_an_order

# print(submit_an_order().json())

order_id = submit_an_order().json()
print(order_id)
# print(update_an_order(order_id).json())