from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class GuessForm(FlaskForm):
    guess = StringField('Guess', validators=[DataRequired(), Length(min=4, max=4, message='Voer getal in van 4')])
    submit = SubmitField('Submit guess')
