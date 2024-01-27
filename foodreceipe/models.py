from foodreceipe import db


class Category(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(50), unique=True, nullable=False)
    receipes = db.relationship("Receipe", backref="category", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.category_name


class Ingredients(db.Model):
    # schema for the Ingredients model
    id = db.Column(db.Integer, primary_key=True)
    ingredient_name = db.Column(db.String(50), unique=True, nullable=False)
    receipes = db.relationship("Receipe", backref="ingredients", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.ingredient_name



class Receipe(db.Model):
    # schema for the Receipe model
    id = db.Column(db.Integer, primary_key=True)
    receipe_name = db.Column(db.String(50), unique=True, nullable=False)
    receipe_description = db.Column(db.Text, nullable=False)
    prep_method = db.Column(db.Text, nullable=False)
    ingredients_id = db.Column(db.Integer, db.ForeignKey("ingredients.id", ondelete="CASCADE"), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.receipe_name

