from flask_wtf import FlaskForm
from wtforms import StringField ,PasswordField ,SubmitField ,BooleanField
from wtforms.validators import data_required , length  ,EqualTo
from wtforms import validators

class RegistrationForm(FlaskForm):
    username = StringField('username',validators=[data_required(),length(min=2,max=20)])
    email = StringField('email',validators=[data_required(),validators.Email()])
    password = PasswordField('password',validators=[data_required()])
    confirm_password = PasswordField('confirm_password',validators=[data_required(),EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('email',validators=[data_required(),validators.Email()])
    password = PasswordField('password',validators=[data_required()])
    rember = BooleanField('rember me')
    login = SubmitField('login')