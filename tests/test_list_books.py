from cerinte.list_of_books import *




class Test_ListBooks:

    def test_list_books(self):
        nr = get_books()
        assert len(nr.json()) > 1, 'nr of books is wrong'
        return nr

    def test_a_book(self):
        detail = get_a_book(id)
        return detail

    def test_all_books_type(self):
        book = get_books(type= '', limit= '')
        assert len(book.json()) == 6, 'limit is wrong'
        assert book.json()[0]['id'] == 1, 'id is not the same'
        assert book.json()[0]['type'] == 'fiction', 'type is not ok'
        assert book.json()[0]['available'] == True, 'the status of book 1 is not ok'
        assert book.json()[1]['id'] == 2, 'id 2 is not ok'
        assert book.json()[1]['type'] == 'non-fiction', 'book type 2 is not ok'
        assert book.json()[1]['available'] == False, 'the status of book 2 is not ok'
        assert book.json()[2]['id'] == 3, 'book id 3 is not ok'
        assert book.json()[2]['type'] == 'fiction', 'book type 3 is not ok'

    def test_submit_an_order(self):
        book = submit_an_order()
        assert len(book) == 2, 'order is not ok'

    # def test_get_all_orders(self):
    #     all_orders = get_all_orders()
    #     assert len(all_orders.json())== 1, 'wrong'

    def test_get_an_order(self):
        first_order = get_an_order(orderId= '')
        assert len(first_order.json()) == 0, 'order is not done'


    def test_update_order(self):
        order_id = submit_an_order()['customerName']
        new_customerName = "John Kevin"
        # update_order = update_an_order(order_id).json()
        assert order_id == new_customerName, 'first order is not ok'