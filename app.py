import json
import os
import markdown
from config import Config
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse
from http import HTTPStatus


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
api = Api(app)

@app.route('/')
def home_page():
    try:
        with open(os.path.dirname(app.root_path) + '/FactoryWebApp/README.md', 'r') as readme:
            return markdown.markdown(readme.read()) # Render README as HTML
    except FileNotFoundError:
        return "<H1>Factory Web App</H1>"

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

if __name__ == '__main__':
    app.run(debug=True)