# -*- encoding: utf-8 -*-

# Python modules
import os, logging 

# Flask modules
from flask               import render_template, request, url_for, redirect, send_from_directory
from flask_login         import login_user, logout_user, current_user, login_required
from werkzeug.exceptions import HTTPException, NotFound, abort
from jinja2              import TemplateNotFound

# App modules
from app.recipe        import blueprint

# App main route + generic routing
@blueprint.route('/')
def index():
    return render_template('recipe_index.html')

