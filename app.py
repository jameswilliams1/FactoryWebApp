import json
import os
import markdown
from config import Config
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse
from http import HTTPStatus

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
api = Api(app)
food_products = json.load(open('sample_food_products.json', 'r'))
textile_products = json.load(open('sample_textile_products.json', 'r'))



class Product(db.Model): # Contains all product types
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    product_type = db.Column(db.String(100))
    def __repr__(self):
        return '<Product %r>' % self.id
    def to_json(self):
        tag_ids = [r[0] for r in ProductTag.query.with_entities(ProductTag.tag_id).filter_by(product_id=self.id).all()] # Gets ID of matching product tags
        tags = [r[0] for r in Tag.query.with_entities(Tag.tag_name).filter(Tag.id.in_(tag_ids))]

        allergen_ids = [r[0] for r in ProductAllergen.query.with_entities(ProductAllergen.allergen_id).filter_by(product_id=self.id).all()] # Gets ID of matching product tags
        allergens = [r[0] for r in Allergen.query.with_entities(Allergen.name).filter(Allergen.id.in_(allergen_ids))]
        materials = {r[0]: {"quantity": r[1], "units": r[2]} for r in Material.query.with_entities(Material.material_name, Material.quantity, Material.units).filter_by(product_id=self.id).all()}
        return {
            'id': self.id,
            'name': self.name,
            'family': Food.query.with_entities(Food.family).filter_by(product_id=self.id).first()[0],
            'tags': tags,
            'allergens': allergens,
            'customer': Food.query.with_entities(Food.customer).filter_by(product_id=self.id).first()[0],
            'billOfMaterials': materials
            }


class Food(db.Model): # Food product specific data
    __tablename__ = 'foods'
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False, primary_key=True)
    family = db.Column(db.String(100), nullable=False)
    customer = db.Column(db.String(100), nullable=False)


class Allergen(db.Model): # For food products only
    __tablename__ = 'allergens'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)


class ProductAllergen(db.Model): # For food products only
    __tablename__ = 'product_allergens'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    allergen_id = db.Column(db.Integer, db.ForeignKey('allergens.id'), nullable=False)


class Textile(db.Model):  # Textile product specific data
    __tablename__ = 'textiles'
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False, primary_key=True)
    colour = db.Column(db.String(100), nullable=False)
    range = db.Column(db.String(100), nullable=False)


class Tag(db.Model): # Used for all products
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.String(100), unique=True, nullable=False)


class ProductTag(db.Model): # Used for all products
    __tablename__ = 'product_tags'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), nullable=False)


class Material(db.Model): # Used for all products
    __tablename__ = 'materials'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    material_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    units = db.Column(db.String(100), nullable=False)


@app.route('/')
def home_page():
    try:
        with open(os.path.dirname(app.root_path) + '/FactoryWebApp/README.md', 'r') as readme:
            return markdown.markdown(readme.read()) # Render README as HTML
    except FileNotFoundError:
        return "<H1>Factory Web App</H1>"


class Products(Resource):

    def get(self):
        #api_key = request.headers['X-API-KEY']
        #if api_key == 'food':
        query = Product.query.filter_by(product_type='food').all()
        return [i.to_json() for i in query]




        if api_key == 'textiles':
            pass
        else:
            return 'X-API-KEY not recognised', HTTPStatus.BAD_REQUEST




    def post(self):
        api_key = request.headers['X-API-KEY']
        if not api_key:
            return 'No X-API-KEY supplied', HTTPStatus.BAD_REQUEST
        json_data = request.get_json()
        if json_data is None:
            return 'No JSON body supplied', HTTPStatus.BAD_REQUEST

        return 'Product created', HTTPStatus.CREATED




api.add_resource(Products, "/products/") # Search all products

if __name__ == '__main__':
    app.run(debug=True)
