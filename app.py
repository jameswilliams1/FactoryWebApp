import json
from http import HTTPStatus

from flask import Flask, request

app = Flask(__name__)


@app.route('/products', methods=['GET', 'POST'])
def products():
    api_key = request.headers['X-API-KEY']
    if request.method == 'POST':
        json_data = request.get_json()
        if json_data is None:
            return 'No JSON body supplied', HTTPStatus.BAD_REQUEST

        # Create product here

        return 'Product created', HTTPStatus.CREATED
    else:
        # Retrieve all products here
        retrieved_products = []
        return json.dumps(retrieved_products)
