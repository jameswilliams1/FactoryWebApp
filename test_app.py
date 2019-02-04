import unittest
import requests
from app import app

food_products = json.load(open('sample_food_products.json', 'r'))
textile_products = json.load(open('sample_textile_products.json', 'r'))

class TestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_get_food(self):
        headers = {X-API-KEY: "food"}
        response = requests.get('http://localhost:5000/products', headers=headers).json()
        self.assertEqual(response, food_products)

    def test_post_food(self):
        headers = {X-API-KEY: "food"}

    def test_textile_products(self):
            headers = {X-API-KEY: "textile"}
            response = requests.get('http://localhost:5000/products', headers=headers).json()
            self.assertEqual(response, textile_products)

    def test_post_textile(self):
        headers = {X-API-KEY: "textile"}


if __name__ == "__main__":
    unittest.main()
