from app import db


class Product(db.Model): # Contains all product types
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    product_type = db.Column(db.String(100))
    def __repr__(self):
        return '<Product %r>' % self.name



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
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False, primary_key=True)
    material_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    units = db.Column(db.String(100), nullable=False)
