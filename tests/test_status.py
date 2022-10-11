from cerinte.get_status import get_status


class TestStatus:
    def test_status(self):
        assert get_status().status_code ==200,'status_code is not the same'
        # assert get_status().json()['status'] =='ok', 'status is not ok'
            # la rulare da eroare la status == ok
