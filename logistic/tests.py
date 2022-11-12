from django.test import TestCase, Client


class TestMyCase(TestCase):
    def test_view(self):
        client = Client()
        response = client.get('api/v1/stocks/')
        self.assertEqual(response.status_code, 200)
