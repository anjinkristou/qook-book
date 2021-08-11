# -*- encoding: utf-8 -*-

from app         import db
from app.mixins  import CRUDMixin
from flask_login import UserMixin

class User(UserMixin, CRUDMixin, db.Model):

    id       = db.Column(db.Integer,     primary_key=True)
    user     = db.Column(db.String(64),  unique = True)
    email    = db.Column(db.String(120), unique = True)
    password = db.Column(db.String(500))

    # Relationships
    recipes = db.relationship('Recipe', back_populates='user')

    def __init__(self, user, email, password):
        self.user       = user
        self.password   = password
        self.email      = email

    def __repr__(self):
        return str(self.id) + ' - ' + str(self.user)
