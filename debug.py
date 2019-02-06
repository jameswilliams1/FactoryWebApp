from app import *
import requests
import json
from test_app import url, food_headers, textile_headers

get_food = requests.get(url, headers=food_headers)
get_textile = requests.get(url, headers=textile_headers)
print(get_food.json())
print(get_food.status_code)
print(get_textile.json())
print(get_textile.status_code)
