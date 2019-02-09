from project import db


class Product(db.Model): # Contains all product types
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    product_type = db.Column(db.String(100))
    def __repr__(self):
         return '<Product %r>' % (self.name)

    def to_json(self): # Performs SQL queries on appropriate tables and generates API JSON output
        tag_ids = [r[0] for r in ProductTag.query.with_entities(ProductTag.tag_id).filter_by(product_id=self.id).all()]
        tags = [r[0] for r in Tag.query.with_entities(Tag.tag_name).filter(Tag.id.in_(tag_ids))]
        materials = {r[0]: {"quantity": r[1], "units": r[2]} for r in Material.query.with_entities(Material.material_name, Material.quantity, Material.units).filter_by(product_id=self.id).all()}
        output_json = {
            "id": self.id,
            "name": self.name,
            "tags": tags,
            "billOfMaterials": materials
        }
        if self.product_type == 'food':
            allergen_ids = [r[0] for r in ProductAllergen.query.with_entities(ProductAllergen.allergen_id).filter_by(product_id=self.id).all()]
            allergens = [r[0] for r in Allergen.query.with_entities(Allergen.name).filter(Allergen.id.in_(allergen_ids))]
            food_details = {
                'family': Food.query.with_entities(Food.family).filter_by(product_id=self.id).first()[0],
                'allergens': allergens,
                'customer': Food.query.with_entities(Food.customer).filter_by(product_id=self.id).first()[0],
                }
            output_json = {**output_json, **food_details}
        elif self.product_type == 'textile':
            textile_details = Textile.query.filter_by(product_id=self.id).first().to_json()
            output_json = {**output_json, **textile_details}
        return output_json


class Food(db.Model): # Food product specific data
    __tablename__ = 'foods'
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False, primary_key=True)
    family = db.Column(db.String(100), nullable=False)
    customer = db.Column(db.String(100), nullable=False)
    def __repr__(self):
        return '<Food %r>' % (self.product_id)


class Allergen(db.Model): # For food products only
    __tablename__ = 'allergens'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    def __repr__(self):
        return '<Allergen %r>' % (self.name)


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
    def __repr__(self):
        return '<Food %r>' % (self.product_id)

    def to_json(self):
        return {"colour": self.colour, "range": self.range}


class Tag(db.Model): # Used for all products
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.String(100), unique=True, nullable=False)
    def __repr__(self):
        return '<Food %r>' % (self.tag_name)


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
    quantity = db.Column(db.Float, nullable=False)
    units = db.Column(db.String(100), nullable=False)
    def __repr__(self):
        return '<Food %r>' % (self.material_name)
