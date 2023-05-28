from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import data_required, email


class RegisterForm(FlaskForm):
    first_name = StringField('first_name', validators=[data_required()])
    last_name = StringField('last_name', validators=[data_required()])
    password = PasswordField('Password', validators=[data_required()])
    email = StringField('Email', validators=[data_required(), email()])
