from django.test import TestCase, Client


class TestStringMethods(TestCase):
    def test_length(self):
        self.assertEqual(len('yatube'), 6)


class TestIndexPost(TestCase):
    def test_index_available(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
