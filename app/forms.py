from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField

class searchPokemon(FlaskForm):
    name = StringField('username', validators=[DataRequired()])
    submit = SubmitField()