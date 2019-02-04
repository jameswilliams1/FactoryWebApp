from app import db


class products(db.Model): # Contains all product types
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class food(db.Model): # Food product specific data
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    family = db.Column(db.String(100), nullable=False)
    customer = db.Column(db.String(100), nullable=False)


class allergens(db.Model): # For food products only
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class product_allergens(db.Model): # For food products only
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    allergen_id = db.Column(db.Integer, db.ForeignKey('allergens.id'), nullable=False)


class textiles(db.Model):  # Textile product specific data
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    colour = db.Column(db.String(100), nullable=False)
    range = db.Column(db.String(100), nullable=False)


class tags(db.Model): # Used for all products
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class product_tags(db.Model): # Used for all products
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), nullable=False)


class materials(db.Model): # Used for all products
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    units = db.Column(db.String(100), nullable=False)
