from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class   UserCreateForm(FlaskForm):

    username = StringField('Username')
    submit = SubmitField('Create')

class UserDeleteForm(FlaskForm):

    username = StringField('Username')
    submit = SubmitField('Delete')
