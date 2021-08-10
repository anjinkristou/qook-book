# -*- encoding: utf-8 -*-

from flask_wtf          import FlaskForm
from flask_wtf.file     import FileField, FileRequired
from wtforms            import StringField, TextAreaField, SubmitField, PasswordField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Email, DataRequired

class LoginForm(FlaskForm):
	username    = StringField  	(u'Username'  	, validators=[DataRequired()])
	password    = PasswordField	(u'Password'  	, validators=[DataRequired()])
	rememberme  = BooleanField 	(u'Remember me')
 
	submit 		= SubmitField	(u'Sign in')
  

class RegisterForm(FlaskForm):
	name        = StringField  	(u'Name'      )
	username    = StringField  	(u'Username'  , validators=[DataRequired()])
	password    = PasswordField	(u'Password'  , validators=[DataRequired()])
	email       = EmailField  	(u'Email'     , validators=[DataRequired(), Email()])
	agreeterms  = BooleanField 	(u'Agree Terms')
 
	submit 		= SubmitField	(u'Sign UP')