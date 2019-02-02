from app import db

class FoodProducts(db.Model):
    id = db.Column(db.Integer, primary_key=True)