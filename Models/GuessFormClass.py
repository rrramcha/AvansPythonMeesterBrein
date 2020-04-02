from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class GuessForm(FlaskForm):
    guess = StringField('Guess', validators=[DataRequired(), Length(min=6, max=6)])
    submit = SubmitField('Submit guess')

    def makeform(self, codelength):
        GuessForm.guess = StringField('Guess', validators=[DataRequired(), Length(min=codelength, max=codelength)])
        GuessForm.submit = SubmitField('Submit guess')
        print(codelength)

