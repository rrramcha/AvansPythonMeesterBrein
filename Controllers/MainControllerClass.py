from flask import render_template
from Models.GameClass import Game
from Models.GuessFormClass import GuessForm
from flask import flash
import sys


class MainController:

    def __init__(self):
        self.game = Game()
        # self.stats = self.read_game_stats()

    def handle_answer(self):
        form = GuessForm()
        if form.validate_on_submit():
            flash('Voer een code in van 4')

        self.game.validate_guess(form.guess.data)
        #print(self.game.guess_results[0], file=sys.stderr)
        return render_template('home.jinja', game=self.game, form=form)

    def read_game_stats(self):
        file = open(".txt", "r")
        data = []
        while 1 < 2:
            line = file.readline()
            print(line)
            if line == "end_stats":
                return data
            else:
                data.append(line.split())

    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, game):
        self._game = game
