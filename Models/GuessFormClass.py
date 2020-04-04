from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp


class GuessForm(FlaskForm):
    guess = StringField('Guess', validators=[DataRequired(),
                                             Length(min=6, max=6),
                                             Regexp("^[0-9]*$",
                                                    message="Can only use numbers LOL")])
    submit = SubmitField('Submit guess')

    def makeform(self, codelength):
        GuessForm.guess = StringField('Guess',
                                      validators=[DataRequired(),
                                                  Length(min=codelength, max=codelength),
                                                  Regexp("^[0-9]*$",
                                                         message="Can only use numbers LOL XDXDDDXXD")])
        GuessForm.submit = SubmitField('Submit guess')

