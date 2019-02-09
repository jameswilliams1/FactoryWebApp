import markdown
import json
from flask_restful import Resource, Api
from project.models import Allergen, Food, Material, Product, ProductAllergen, ProductTag, Tag, Textile
from project import db
from flask import request, Blueprint
from http import HTTPStatus

api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)

class Products(Resource):
    def get(self):
        try:
            api_key = request.headers['X-API-KEY']
        except KeyError:
            return 'No X-API-KEY supplied', HTTPStatus.BAD_REQUEST
        if api_key == 'food':
            query = Product.query.filter_by(product_type='food').all()
            return [q.to_json() for q in query]
        elif api_key == 'textile':
            query = Product.query.filter_by(product_type='textile').all()
            return [q.to_json() for q in query]
        else:
            return 'X-API-KEY not recognised', HTTPStatus.BAD_REQUEST

    def post(self):
        api_key = ''
        try:
            api_key = request.headers['X-API-KEY']
            if api_key != 'food' and api_key != 'textile':
                return 'X-API-KEY not recognised', HTTPStatus.BAD_REQUEST
        except KeyError:
            return 'No X-API-KEY supplied', HTTPStatus.BAD_REQUEST
        json_data = dict(request.get_json(force=True))
        if not json_data:
            return 'No JSON body supplied', HTTPStatus.BAD_REQUEST
        try:
            product = Product(name=json_data["name"], product_type=api_key)
            db.session.add(product)
            db.session.flush()
            product_id = product.id
            materials = json_data.get("billOfMaterials") # Returns None if no materials provided
            tags = json_data.get("tags")
            if api_key == 'food':
                family = json_data["family"]
                customer = json_data["customer"]
                food_entry = Food(product_id=product_id, family=family, customer=customer)
                db.session.add(food_entry)
                allergens = json_data.get("allergens")
                if allergens:
                    for allergen in allergens:
                        allergen_data = Allergen(name=allergen)
                        db.session.add(allergen_data)
                        db.session.flush()
                        allergen_id = allergen_data.id
                        db.session.add(ProductAllergen(allergen_id=allergen_id, product_id=product_id))
            elif api_key == 'textile':
                colour = json_data["colour"]
                product_range = json_data["range"]
                textile_data = Textile(colour=colour, range=product_range)
                db.session.add(textile_data)
            if tags:
                for tag in tags:
                    tag_data = Tag(tag_name=tag)
                    db.session.add(tag_data)
                    db.session.flush()
                    tag_id = tag_data.id
                    db.session.add(ProductTag(tag_id=tag_id, product_id=product_id))
            if materials:
                for material, data in materials.items():
                    material_data = Material(product_id=product_id, material_name=material, quantity=data["quantity"], units=data["units"])
                    db.session.add(material_data)
            db.session.commit()
        except KeyError:
            return 'Invalid JSON body supplied', HTTPStatus.BAD_REQUEST
        return 'Product created', HTTPStatus.CREATED


api.add_resource(Products, '/')
