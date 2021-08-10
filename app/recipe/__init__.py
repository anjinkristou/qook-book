# -*- encoding: utf-8 -*-

from flask import Blueprint

blueprint = Blueprint(
    'recipe_blueprint',
    __name__,
    url_prefix='/recipe',
    template_folder='templates',
    static_folder='static'
)