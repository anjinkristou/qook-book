# -*- encoding: utf-8 -*-

from app         import db
from app.mixins  import CRUDMixin
from app.auth.models import User

class Recipe(CRUDMixin, db.Model):

    id          = db.Column(db.Integer,     primary_key=True)
    name        = db.Column(db.Unicode(64))
    details     = db.Column(db.Text)
    image_url   = db.Column(db.String(255))
    servings    = db.Column(db.Integer)
    difficulty  = db.Column(db.Integer)
    
    # Foreign keys
    user_id   = db.Column(db.Integer, db.ForeignKey(User.id))

    # Relationships
    user = db.relationship('User', back_populates='recipes')
    ingredients = db.relationship('RecipeIngredient', back_populates='recipe', cascade="all, delete-orphan")
    steps = db.relationship('RecipeStep', back_populates='recipe', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Recipe {self.id}>"
    
class Ingredient(CRUDMixin, db.Model):
    
    id          = db.Column(db.Integer,     primary_key=True)
    name        = db.Column(db.Unicode(64))
    unit        = db.Column(db.Unicode(64))
    image_url   = db.Column(db.String(255))
    

    # Relationships
    recipes = db.relationship('RecipeIngredient', back_populates='ingredient')

    def __repr__(self):
        return f"<Ingredient {self.id}>"
    
    def display(self):
        return f"{self.name} [{self.unit}]"


class RecipeIngredient(CRUDMixin, db.Model):
    
    id          = db.Column(db.Integer,     primary_key=True)
    quantity    = db.Column(db.Unicode(64))
    shape       = db.Column(db.Unicode(64))
    
    # Foreign keys
    recipe_id   = db.Column(db.Integer, db.ForeignKey(Recipe.id))
    ingredient_id   = db.Column(db.Integer, db.ForeignKey(Ingredient.id))

    # Relationships
    recipe = db.relationship('Recipe', back_populates='ingredients')
    ingredient = db.relationship('Ingredient', back_populates='recipes')

    def __repr__(self):
        return f"<RecipeIngredient {self.id}>"
    
class RecipeStep(CRUDMixin, db.Model):
    
    id          = db.Column(db.Integer,     primary_key=True)
    details = db.Column(db.Text)
    
    # Foreign keys
    recipe_id   = db.Column(db.Integer, db.ForeignKey(Recipe.id))

    # Relationships
    recipe = db.relationship('Recipe', back_populates='steps')

    def __repr__(self):
        return f"<RecipeStep {self.id}>"