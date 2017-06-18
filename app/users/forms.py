from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class UserCreateForm(FlaskForm):

    username = StringField('Username')
    submit = SubmitField('Create')
