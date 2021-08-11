from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    IntegerField,
    SubmitField,
    SelectField,
    HiddenField,
    ValidationError,
    TextAreaField,
    DateTimeField,
    TimeField,
    FormField,
    Form,
    FieldList,
    FileField,
    BooleanField
)
from wtforms.fields.html5 import SearchField, URLField
from datetime import datetime
from wtforms.fields.core import DateField
from wtforms.validators import (
    InputRequired,
    Email,
    Length,
    Optional
)
from wtforms_sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from app.recipe.models import Recipe, RecipeIngredient, Ingredient, RecipeStep

class RecipeIngredientForm(Form):
    quantity = StringField(
        'quatity',
        validators=[InputRequired()]
    )
    ingredient = QuerySelectField(
        'Ingredient',
        query_factory=lambda: Ingredient.query.all(),
        get_pk=lambda ingedient: ingedient.id,
        get_label=lambda ingedient: ingedient.display(),
        allow_blank=True,
        blank_text="No ingredient"
    )

class RecipeStepForm(Form):
    test = TextAreaField('Details', validators=[Optional()])

    details = TextAreaField('Details', validators=[Optional()])


class RecipeForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    image_url = URLField('Image')
    details = TextAreaField('Details', validators=[Optional()])
    servings = IntegerField('Servings', validators=[InputRequired()])
    difficulty = SelectField(u'Difficulty', choices=[(0, 'Easy'), 
                                                     (1, 'Normal'), 
                                                     (2, 'Difficult')],
                             coerce=int
                             )
    ingredients = FieldList(
        FormField(RecipeIngredientForm, label='Ingredients',
                  default=lambda: RecipeIngredient())
    )
    steps = FieldList(
        FormField(RecipeStepForm, label='Steps',
                  default=lambda: RecipeStep())
    )
    submit = SubmitField('Add Recipe')