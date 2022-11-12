from django.test import TestCase, Client


class TestMyCase(TestCase):
    def test_view(self):
        client = Client()
        response = client.get('http://127.0.0.1:8000/api/v1/stocks/')
        self.assertEqual(response.status_code, 200)
