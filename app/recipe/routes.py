# -*- encoding: utf-8 -*-

# Python modules
import os, logging 

# Flask modules
from flask               import render_template, request, url_for, redirect, send_from_directory, flash
from flask_login         import login_user, logout_user, current_user, login_required
from werkzeug.exceptions import HTTPException, NotFound, abort
from jinja2              import TemplateNotFound

# App modules
from app.recipe        import blueprint
from app.recipe.forms import RecipeForm, RecipeIngredientForm, RecipeStepForm
from app.recipe.models import Recipe

@blueprint.route('/')
@login_required
def index():
    recipes = Recipe.query.all()
    return render_template('recipe_index.html', recipes=recipes)


@blueprint.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    recipe = Recipe(user=current_user)
    form = RecipeForm(obj=recipe)
    ingredient_template_form = RecipeIngredientForm(prefix='ingredients-_-')
    step_template_form = RecipeStepForm(prefix='steps-_-')
    if form.validate_on_submit():
        form.populate_obj(recipe)
        recipe.save()
        
        print(form.ingredients.data)

        flash('Recipe created successfully!', category='success')
        return redirect(url_for('recipe_blueprint.index'))

    return render_template('recipe.html',
                           form=form,
                           _ingredient_template=ingredient_template_form,
                           _step_template=step_template_form,
                           )
    
    
@blueprint.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    recipe = Recipe.query.get_or_404(id)
    form = RecipeForm(obj=recipe)
    ingredient_template_form = RecipeIngredientForm(prefix='ingredients-_-')
    step_template_form = RecipeStepForm(prefix='steps-_-')
    
    if form.validate_on_submit():
        form.populate_obj(recipe)
        recipe.update()
        
        flash('Recipe created successfully!', category='success')
        return redirect(url_for('recipe_blueprint.index'))

    return render_template('recipe.html',
                           form=form,
                           _ingredient_template=ingredient_template_form,
                           _step_template=step_template_form,
                           recipe=recipe,
                           )

@blueprint.route('/delete/<int:id>')
@login_required
def delete(id):
    recipe = Recipe.query.get_or_404(id)
    recipe.delete()
    return redirect(url_for('recipe_blueprint.index'))
