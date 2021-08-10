# -*- encoding: utf-8 -*-

import os
from importlib          import import_module

from flask              import Flask
from flask_sqlalchemy   import SQLAlchemy
from flask_login        import LoginManager
from flask_bcrypt       import Bcrypt
from flask_migrate      import Migrate

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy  () # flask-sqlalchemy
bc = Bcrypt      () # flask-bcrypt
lm = LoginManager() # flask-loginmanager
mg = Migrate(db=db, render_as_batch=True)    # flask-migrate


def register_extensions(app):
    db.init_app(app)
    bc.init_app(app)
    lm.init_app(app)
    mg.init_app(app)

def register_blueprints(app):
    for module_name in ('auth', 'home', 'recipe'):
        module = import_module('app.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)

def configure_database(app):

    # @app.before_first_request
    # def initialize_database():
    #     db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)
    configure_database(app)
    return app